# palindrome recursive
# Write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.

# You must solve this recursively.

def palindrome(s1):
    if(len(s1) == 0):
        return True
    if(len(s1) == 1):
        return True
    first = s1[0]
    last = s1[-1]
    remaining = s1[1:-1]
    if(first == last):
        return (True and palindrome(remaining))
    else:
        return False

assert palindrome("pop") == True
assert palindrome("kayak") == True
assert palindrome("pops") == False
assert palindrome("boot") == False
assert palindrome("rotator") == True
assert palindrome("abcbca") == False
assert palindrome("") == True


