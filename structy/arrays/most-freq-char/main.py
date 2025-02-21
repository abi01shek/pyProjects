def most_frequent_char(s1):
    d1 = {}
    maxv = 0
    mfc = ""
    for c in s1:
        if c not in d1:
            d1[c] = 1;
        else:
            d1[c] = d1[c] + 1
        if d1[c] > maxv:
            maxv = d1[c]
            mfc = c
    print(s1, mfc)
    return mfc

assert most_frequent_char('bookeeper') == "e"

assert most_frequent_char('david') == 'd'
assert most_frequent_char('abby') == 'b'
assert most_frequent_char('mississippi') == 's'
assert most_frequent_char('potato') == 't'
assert most_frequent_char('eleventennine') == 'e'
assert most_frequent_char('riverbed') == 'r'
