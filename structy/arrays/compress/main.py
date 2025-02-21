def compress(run):
    prev_char = ""
    char_count = 0
    result = ""
    for curr_char in run:
        if prev_char != "":
            if prev_char == curr_char:
                char_count = char_count + 1
            else:
                if(char_count != 1):
                    result = result + str(char_count) +  prev_char
                else:
                    result = result +  prev_char
                char_count = 1
        else:
            char_count = 1
        prev_char = curr_char

    # last run of characters is not accounted for.
    if(char_count != 1):
        result = result + str(char_count) +  prev_char
    else:
        result = result +  prev_char
    return result

assert compress('ccaaatsss') == '2c3at3s'
assert compress('ssssbbz') == '4s2bz'
assert compress('ppoppppp') == '2po5p'
assert compress('nnneeeeeeeeeeeezz') == '3n12e2z'
assert compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy') == '127y'

