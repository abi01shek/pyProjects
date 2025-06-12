"""
Develop a streaming JSON parser

I follow the JSON spec in https://www.json.org/json-en.html with following assumptions:
* The supplied string is the serialization of a single JSON object and there are no 
  further characters after the serialized object. 
* Strings do not contain nested quotes, control characters or white spaces.
* Keys are always strings.
* Values are either strings or nested JSON object (no numbers, arrays, booleans or NULL).
* whitespaces include tabulations, carriage returns and linefeeds.

The generator and coroutine mechanism is very interesting. I would assume internally it connects 
the coroutines via named-pipes with the ends connected to an epoll/poll/select system call to identify
when data is ready to be read/written. One coroutine would write to the pipe and the epoll would indicate
that data is available on the pipe for subsequent coroutine to read.

Tests done with Python version 3.12.7 and cover following scenarios:
* Test cases provided as part of the challenge
* Consuming empty stream
* Whether whitespaces are in accordance with JSON spec
* No partial key strings are returned
* Partial value strings are returned 
* Nested objects as values are consumed correctly

Useful references:
* JSON spec: https://www.json.org/json-en.html
* How to write a streaming parser: https://jsoneditoronline.org/indepth/parse/streaming-parser/ 
* LL(1) parser design in python: https://www.geeksforgeeks.org/compiler-design-ll1-parser-in-python/
"""

from collections import deque

class StreamingJsonParser:
    """
    Class to parse streaming JSON data incrementally.
    
    Attributes
        buffer      (deque): Buffer to store incoming stream.
        char        (str)  : Next available character in the buffer.
        result_dict (dict) : Dictionary that stores parsed JSON object from incoming stream.
        parser      (coroutine) : Coroutine that parses incoming stream.

    Methods:
        __init__(self)
            Initialize the parser and its attributes.
        consume(self, buffer:str = '')
            Coroutine that parses a chunk of JSON data incrementally.
            Parameter buffer holds incoming chunk.
        get(self)
            Returns the current state of the parsed JSON object as a dict.
            Partially consumed keys are not part of the results but 
            partially consumed value strings are. 

    """
    def __init__(self):
        self.buffer = deque()    # O(1) performance for popleft and append
        self.char = None
        self.result_dict = {}
        self.parser = self.parse_object(self.result_dict)
        next(self.parser) # Start the coroutine 

    def next_char(self):
        """
        Coroutine that pauses (non-block wait) till next character is available in the buffer.
        """
        while not self.buffer:
            yield # pause (non-block wait) here if buffer is empty
        self.char = self.buffer.popleft()
        return # next character is available

    def skip_whitespace(self):
        """
        Couroutine that pauses till a non-whitespace character is available in the buffer.
        """
        if self.char == None:
            yield from self.next_char() # pause till next char is available in buffer
        while self.char and self.char.isspace():
            yield from self.next_char()
        return # next non white space character is available

    def parse_key(self):
        """
        Coroutine that pauses till a full key is read from the buffer.
        key is of type string without any spaces, control characters and nested quotes.
        """
        token = ""
        token_chars_list = []
        stop_chars = {':', ',', '}', '"'}
        if self.char == '"':
            yield from self.next_char()
        else:
            raise ValueError("Expected '\"' at start of string")
        while self.char and not self.char.isspace() and self.char not in stop_chars:
            token_chars_list.append(self.char)
            yield from self.next_char() # pause here if key is partial
        if self.char == '"':
            yield from self.next_char()
        else:
            raise ValueError("Expected '\"' at end of string")
        token = ''.join(token_chars_list)
        return token # full key is available


    def parse_object(self, local_result_dict:dict):
        """
        Coroutine that parses a JSON object and stores it in the input dictionary argument.

        The JSON object of format {key:value} where key is string and value can be 
        a string or nested JSON object.

        This method ensures that a key is added to dictionary only when it is fully parsed 
        but value-strings are added to the dictionary as they arrive in the input buffer.
        """
        yield from self.skip_whitespace()
        if self.char == '{':
            yield from self.next_char() # pause till next character is available in buffer
        else:
            raise ValueError("Expected '{' at start of JSON object")

        while True:
            yield from self.skip_whitespace() # pause till next non-whitespace character is available in buffer
            if self.char == '}':
                break

            key = yield from self.parse_key() # pause till full key is read from buffer
            yield from self.skip_whitespace()

            if self.char != ':':
                raise ValueError("Expected ':' after key")
            yield from self.next_char()
            yield from self.skip_whitespace()

            # Read the value from buffer
            if self.char == '"': # Value is a string
                local_result_dict[key] = "" 
                yield from self.next_char()
                while self.char and not self.char.isspace() and self.char not in [':', ',', '}', '\"']:
                    local_result_dict[key] += self.char # Add partial value strings as they arrive
                    yield from self.next_char()
                if self.char == '"':
                    yield from self.next_char()
                else:
                    raise ValueError("Expected '\"' at end of string")
            elif self.char == '{': # Value is JSON object
                local_result_dict[key] = {}
                yield from self.parse_object(local_result_dict[key]) # recursive
            else:
                raise ValueError("Expected '{' or '\"' at start of JSON value")

            yield from self.skip_whitespace()
            if self.char == ',':
                yield from self.next_char()
            elif self.char == '}':
                break
            else:
                raise ValueError("Expected ',' or '}' after key-value pair")

    def consume(self, buffer:str = ''):
        """
        Coroutine that adds incoming stream into local buffer and initiates parse coroutine.
        """
        self.buffer.extend(buffer)
        try:
            next(self.parser)
        except StopIteration:
            pass

    def get(self):
        """
        Return JSON object that has been parsed from incoming stream.
        """
        return self.result_dict


# Test functions
def test_streaming_json_parser():
    parser = StreamingJsonParser()
    parser.consume('{"foo": "bar"}')
    assert parser.get() == {"foo": "bar"}

def test_chunked_streaming_json_parser():
    parser = StreamingJsonParser()
    parser.consume('{"foo":')
    parser.consume('"bar')
    assert parser.get() == {"foo": "bar"}

def test_partial_streaming_json_parser():
    parser = StreamingJsonParser()
    parser.consume('{"foo": "bar')
    assert parser.get() == {"foo": "bar"}

def test_empty_consume():
    parser = StreamingJsonParser()
    parser.consume()
    assert parser.get() == {}

def test_whitspace():
    """
    json.org suggests whitespace can be space, linefeed, carriage return and horizontal tab.
    Check if all of these work.
    """
    parser = StreamingJsonParser()
    parser.consume('{  "foo"\t: \n \r "bar" }')
    assert parser.get() == {"foo":"bar"}

def test_partial_key():
    """
    Test if keys are NOT consumed until they are fully streamed.
    """
    parser = StreamingJsonParser()
    parser.consume('{"foo1":"bar1", "fo')
    assert parser.get() == {"foo1":"bar1"} #fo is not consumed
    parser.consume('o2":"bar2"}')
    assert parser.get() == {"foo1":"bar1","foo2":"bar2"} #foo2 is consumed

def test_partial_string_value():
    """
    Test if string values ARE consumed incrementally as they streamed in.
    """
    parser = StreamingJsonParser()
    parser.consume('{"foo1":"bar1", "foo2":"b')
    assert parser.get() == {"foo1":"bar1", "foo2":"b"}
    parser.consume('a')
    assert parser.get() == {"foo1":"bar1", "foo2":"ba"}
    parser.consume('r2"')
    assert parser.get() == {"foo1":"bar1", "foo2":"bar2"}
    # Example in challenge 
    parser = StreamingJsonParser()
    parser.consume('{"test": "hello", "country": "Switzerl')
    assert parser.get() == {"test": "hello", "country": "Switzerl"}


def test_nested_object_value():
    """
    Test nested JSON objects as values.
    """
    parser = StreamingJsonParser()
    parser.consume('{"foo1": \
                            {"foo2": \
                                    {"foo3":"bar3"} \
                            } \
                    }')
    assert parser.get() == {"foo1":{"foo2":{"foo3":"bar3"}}}


def test_string_with_spaces():
    """
    String types (keys and value string) should not have spaces.
    """
    # Key string has space (not allowed)
    parser = StreamingJsonParser()
    try:
        parser.consume('{"fo o":"bar"}')
        assert 0
    except ValueError:
        assert 1

    # value string has space (not allowed)
    parser = StreamingJsonParser()
    try:
        parser.consume('{"foo":"ba r"}')
        assert 0
    except ValueError:
        assert 1

# Running test cases
test_streaming_json_parser()
test_chunked_streaming_json_parser()
test_partial_streaming_json_parser()
test_empty_consume()
test_whitspace()
test_partial_key()
test_partial_string_value()
test_nested_object_value()
test_string_with_spaces()
print("All tests pass")
