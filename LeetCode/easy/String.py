# input: "AAABBCCB", k=3
# output: "CC"


def string(s, k):
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    result = ''
    for c in s:
        if dic[c] != k:
            result += c
    return result

print(string("AAABBCCB", 3))

    