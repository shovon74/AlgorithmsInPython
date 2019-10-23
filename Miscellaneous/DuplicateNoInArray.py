def getDuplicate(A):
    size = len(A)
    repeat = []
    for i in range (size):
        k = i+1
        for j in range (k, size):
            if A[i] == A[j] and A[i] not in repeat:
                repeat.append(A[i])
    return repeat






A = [1,2,3,4,5,2,5]
result = getDuplicate(A)
print(result)