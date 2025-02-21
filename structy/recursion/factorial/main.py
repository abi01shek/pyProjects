# factorial
# Write a function, factorial, that takes in a number n and returns the factorial of that number. The factorial of n is the product of all the positive numbers less than or equal to n. You must solve this recursively.


def factorial(n):
  if(n == 0):
    return 1
  if(n == 1):
    return 1
  prod = n * factorial(n-1)
  return(prod)

assert factorial(3) == 6
assert factorial(6) == 720
assert factorial(18) == 6402373705728000
assert factorial(1) == 1
assert factorial(13) == 6227020800
assert factorial(0) == 1
