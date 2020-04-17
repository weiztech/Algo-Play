# Tim's Sort Algorithm

k = [9, 2, 5, 6, 8, 10]

# Version 1 (loop idx from end of the list)
for i, v in enumerate(k):
    if (i == 0):
        continue

    for icv in range(i-1, -1, -1):
        cv = k[:i][icv]
        if v > cv:
            k.insert(icv+1, k.pop(i))
            break
        elif v < cv and not icv:
            k.insert(0, k.pop(i))

print(k == [2, 5, 6, 8, 9, 10])

k = [9, 20, 2, 5, 6, 8, 10]
# Version 2 (loop idx from start of the list)
for i, v in enumerate(k):
    if (i == 0):
        continue

    for icv in range(i):
        cv = k[:i][-icv-1]
        if v > cv:
            k.insert(i-icv, k.pop(i))
            break
        elif v < cv and -(-icv-1) == i:
            k.insert(0, k.pop(i))

print(k == [2, 5, 6, 8, 9, 10, 20])
