# reverse string recursive
# Write a function, reverse_string, that takes in a string as an argument. The function should return the string with its characters in reverse order. You must do this recursively.

def reverse_string(s):
  if(len(s) == 0):
    return ""
  curr_char = s[0]
  remain = "".join(s[1:])
  result = reverse_string(remain) + curr_char
  return(result)

assert reverse_string("hello") == "olleh"
assert reverse_string("abcdefg") == "gfedcba"
assert reverse_string("stopwatch") == "hctawpots"
assert reverse_string("") == ""
