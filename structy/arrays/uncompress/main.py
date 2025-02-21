# order of N time complexity
def uncompress(s1):
    s2 = ""
    curr_num_str = ""
    curr_num = 0
    curr_char = ""
    for i in range(len(s1)):
        if s1[i].isdigit():
            # accumulate number as a string
            curr_num_str = curr_num_str + s1[i]
        else :
            # found a character
            # convert curr_num to integer
            curr_num = int(curr_num_str)
            for j in range(curr_num):
                s2 = s2 + s1[i]
            curr_num_str = ""
    return s2


assert uncompress("2c3a1t") == 'ccaaat'
assert uncompress("4s2b") == 'ssssbb'
assert uncompress("2p1o5p") == 'ppoppppp'
assert uncompress("3n12e2z") == 'nnneeeeeeeeeeeezz'
assert uncompress("127y") == 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
