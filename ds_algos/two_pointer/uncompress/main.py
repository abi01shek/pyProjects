"""
uncompress
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
"""
def uncompress(s):
    i = 0
    curr_count = 0
    result = ""
    while(True):
        if(i == len(s)):
            break
        if(s[i].isnumeric()):
            curr_count = curr_count * 10 + int(s[i])
        else:
            for j in range(curr_count):
                result = result + s[i]
            curr_count = 0
        i = i + 1
    return result


assert(uncompress("2c3a1t") == 'ccaaat')
assert(uncompress("4s2b") == 'ssssbb')
assert(uncompress("2p1o5p") == 'ppoppppp')
assert(uncompress("3n12e2z") == 'nnneeeeeeeeeeeezz')
assert(uncompress("127y") == 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
