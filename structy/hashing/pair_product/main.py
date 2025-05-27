# Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.


def pair_product(numbers, target):
    pair_product_hash = {}
    index = 0
    for n in numbers:
        if (target % n == 0):
            other = target / n
            if(other in pair_product_hash):
                return (pair_product_hash[other], index)
            else:
                pair_product_hash[n] = index
                index = index + 1
        else:
            index = index + 1
assert(pair_product([3, 2, 5, 4, 1], 8) == (1, 3))
assert(pair_product([3, 2, 5, 4, 1], 8) == (1, 3))
assert(pair_product([4, 7, 9, 2, 5, 1], 5) == (4, 5))
assert(pair_product([4, 7, 9, 2, 5, 1], 35) == (1, 4))
