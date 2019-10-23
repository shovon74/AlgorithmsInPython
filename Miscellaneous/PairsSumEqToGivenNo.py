def pairs(A,s):
    print(s)
    size = len(A)
    pair = []
    for i in range(size):
        first = A[i]
        k = i + 1;
        for j in range(k, size):
            second = A[j]
            if first + second == s:
                pair.extend((first, second))

    return pair




A=[1,2,3,4,5]

s = 6
result = pairs(A, s)
print(result)
