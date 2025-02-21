def anagrams(s1, s2):
    if(len(s1) != len(s2)):
        return False
    for c1 in s1:
        if c1 in s2:
            idx = s2.index(c1)
            s2 = s2[:idx] + s2[idx+1:]
        else:
            return False

    if s2 != "":
        return False
    return True

anagrams("fluster", "restful")
anagrams("cats", "cots")
anagrams('monkeyswrite', 'newyorktimes')
anagrams('paper', 'reapa')
anagrams('elbow', 'below')
anagrams('pp', 'oo')
anagrams('po', 'popp')
