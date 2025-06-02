# Write a function, pairSum, that takes in an array and a target sum as arguments. The function should return an array containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.



def pair_sum(numbers, target_sum):
    pair_sum_hash = {}
    index = 0
    for number in numbers:
        complement = target_sum - number
        if(complement in pair_sum_hash):
            return (pair_sum_hash[complement], index)
        else:
            pair_sum_hash[number] = index
            index = index + 1
    return


assert(pair_sum([3, 2, 5, 4, 1], 8) ==  (0, 2))
assert(pair_sum([4, 7, 9, 2, 5, 1], 5) == (0, 5))
assert(pair_sum([4, 7, 9, 2, 5, 1], 3) == (3, 5))
assert(pair_sum([1, 6, 7, 2], 13) == (1, 2))
assert(pair_sum([9, 9], 18) == (0, 1))
assert(pair_sum([6, 4, 2, 8 ], 12) == (1, 3))

