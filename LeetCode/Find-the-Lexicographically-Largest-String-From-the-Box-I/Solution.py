i, j, n = 0, 1, len(s)
while j < n:
    k = 0
    while j + k < n and s[i + k] == s[j + k]:
        k += 1
    if j + k < n and s[i + k] < s[j + k]:
        i, j = j, max(j + 1, i + k + 1)
    else:
        j = j + k + 1
return s[i:]