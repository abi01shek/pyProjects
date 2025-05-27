"""
Print all subarrays with 0 sum
Given an integer array, print all subarrays with zero-sum.
https://www.techiedelight.com/find-sub-array-with-0-sum/

Input:  { 4, 2, -3, -1, 0, 4 }

Subarrays with zero-sum are
{ -3, -1, 0, 4 }
{ 0 }

Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

Subarrays with zero-sum are
{ 3, 4, -7 }
{ 4, -7, 3 }
{ -7, 3, 1, 3 }
{ 3, 1, -4 }
{ 3, 1, 3, 1, -4, -2, -2 }
{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
"""

# O(n^2)
def subarray_sum_0(numbers):
    sublist_total = 0
    sublist = []
    for head_idx in range(len(numbers)):
        sublist_total = numbers[head_idx]
        sublist.clear()
        sublist.append(numbers[head_idx])

        # if head itself is zero no need to iterate over tail
        if(sublist_total == 0):
            print(sublist)
            continue

        for tail_idx in range(head_idx+1, len(numbers)):
            sublist_total = sublist_total + numbers[tail_idx]
            if(sublist_total != 0):
                sublist.append(numbers[tail_idx])
            else:
                sublist.append(numbers[tail_idx])
                print(sublist)

        # all tail indices parsed, no sum 0 found
        # continue with next head index
    pass

subarray_sum_0([4, 2, -3, -1, 0, 4])
subarray_sum_0([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
