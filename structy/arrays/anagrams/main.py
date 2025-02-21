def anagrams(s1, s2):
    if(len(s1) != len(s2)):
        return False
    d1, d2 = count_chars(s1, s2)
    for k1 in d1:
        if k1 not in d2:
            return False
        else:
            if d1[k1] != d2[k1]:
                return False
    return True

def count_chars(s1, s2):
    d1,d2 = {},{}
    for c in s1:
        if c not in d1:
            d1[c] = 1;
        else :
            d1[c] = d1[c]+1
    for c in s2:
        if c not in d2:
            d2[c] = 1;
        else :
            d2[c] = d2[c]+1
    return d1, d2


assert anagrams("fluster", "restful") == True
assert anagrams("cats", "cots") == False
assert anagrams('monkeyswrite', 'newyorktimes') == True
assert anagrams('paper', 'reapa') == False
assert anagrams('elbow', 'below') == True
assert anagrams('pp', 'oo') == False
assert anagrams('po', 'popp') == False
