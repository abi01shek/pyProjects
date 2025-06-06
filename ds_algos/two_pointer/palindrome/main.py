"""
is palindrome
Write a function, is_palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.
"""

def is_palindrome(s):
  startp = 0
  endp = len(s)-1
  flag = True
  while(startp < endp):
      if(s[startp] != s[endp]):
          flag = False
          break
      startp = startp + 1
      endp = endp - 1
      pass
  return(flag)



assert(is_palindrome("pop") == True)
assert(is_palindrome("kayak") == True)
assert(is_palindrome("pops") == False)
assert(is_palindrome("boot") == False)
assert(is_palindrome("rotator") == True)
assert(is_palindrome("abcbca") == False)
assert(is_palindrome("") == True)

