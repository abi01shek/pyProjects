# sum of lengths
# Write a function sumOfLengths that takes in a list of strings and returns the total length of the strings.

# You must solve this recursively.

def sum_of_lengths(strings):
    if(len(strings)) == 0:
        return 0
    chosen = strings[0]
    remain = strings[1:]
    sum_o_len = len(chosen) + sum_of_lengths(remain)
    return(sum_o_len)

assert sum_of_lengths(['goat', 'cat', 'purple']) == 13
assert sum_of_lengths(['bike', 'at', 'pencils', 'phone']) == 18
assert sum_of_lengths([]) == 0
assert sum_of_lengths(['', ' ', '  ', '   ', '    ', '     ']) == 15
assert sum_of_lengths(['0', '313', '1234567890']) == 14

