"""
Sort binary array in linear time
Given a binary array, sort it in linear time and constant space. The output should print all zeros, followed by all ones.

For example,

Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
Output: { 0, 0, 0, 0, 1, 1, 1, 1 }
"""

def sort_bin_array(bin_array):
    head = 0
    tail = head + 1
    bin_len = len(bin_array)
    while(tail < bin_len):
        if (bin_array[head] == 1 and bin_array[tail] == 0):
            # exchange
            bin_array[tail] = 1
            bin_array[head] = 0
            head = head + 1
            tail = tail + 1
        elif (bin_array[head] == 1 and bin_array[tail] == 1):
            tail = tail + 1
        elif (bin_array[head] == 0 and bin_array[tail] == 0):
            head = head + 1
            tail = tail + 1
        else : # head 0 tail 1
            head = head + 1
            tail = tail + 1
    return bin_array

print(sort_bin_array([1, 0, 1, 0, 1, 0, 0, 1]))
