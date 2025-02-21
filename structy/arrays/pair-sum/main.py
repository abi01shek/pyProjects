def pair_sum(numbers, target_sum):
    d1 = {}
    for i in range(len(numbers)):
        chosen = numbers[i]
        complement = target_sum - chosen
        if complement in d1:
            return(d1[complement], i)
        else:
            d1[chosen] = i

# O(nlogn)
def pair_sum_slow(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return((i,j))

assert pair_sum([3, 2, 5, 4, 1], 8) == (0, 2)
assert pair_sum([4, 7, 9, 2, 5, 1], 5) == (0, 5)
assert pair_sum([4, 7, 9, 2, 5, 1], 3) == (3, 5)
assert pair_sum([1, 6, 7, 2], 13) == (1, 2)
assert pair_sum([9, 9], 18) == (0, 1)
assert pair_sum([6, 4, 2, 8 ], 12) == (1, 3)
