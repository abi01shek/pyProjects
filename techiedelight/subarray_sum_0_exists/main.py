#https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/
#Check if a subarray with 0 sum exists or not
#Given an integer array, check if it contains a subarray having zero-sum.

#For example,
# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
# Output: Subarray with zero-sum exists The subarrays with a sum of 0 are:
#{ 3, 4, -7 }
#{ 4, -7, 3 }
#{ -7, 3, 1, 3 }
#{ 3, 1, -4 }
#{ 3, 1, 3, 1, -4, -2, -2 }
#{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }


"""
use a hash to store the total from the start
as we keep adding new numbers we will encounter a previous total
only if adding the new number results in a zero sum
"""
def subarray_sum_0(numbers):
    total_set = set()
    total = 0
    total_set.add(0)
    for i in numbers:
        total = total + i
        if total in total_set:
            # a previous value of total will be encountered only
            # if some sum adds up to 0
            return True
        total_set.add(total)
    return False

subarray_sum_0([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
