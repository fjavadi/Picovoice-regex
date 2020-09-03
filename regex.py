def match(s, p):
    frst_char_match = False
    #   Firstly, we check the first character of s
    if (len(p) == 0 and len(s) == 0):
        return True
    elif (len(p) == 0 and len(s) != 0):
        return False
    elif (len(s) != 0) and (p[0] == s[0] or p[0] == "."):
        frst_char_match = True
    else:
        frst_char_match = False

    # print(s, p, frst_char_match)


    # Check if the pattern has *, if so, if the character is starting a new pattern we skip p by 2, else if the character is continuing the previous patter we skip s by 1.
    if (len(p) > 1) and (p[1] == "*"):
        return (match(s, p[2:]) or (frst_char_match and match(s[1:], p)))

    # if pattern doesn't have * we check if the first char of s and p matches and if so we can check the rest of the s and p omitting the first char
    else:
        return frst_char_match and match(s[1:], p[1:])


x = match("aaabbb", "aa*b*")
print(x)

x = match("aabbb", "a*b*")
print(x)

x = match("aaabbb", ".*b")
print(x)

x = match("acbbb", "aa*b*")
print(x)

x = match("abbb", "a*b")
print(x)