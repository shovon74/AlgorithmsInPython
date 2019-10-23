def findMultipleDuplicate(A):
    initial = []
    final = []
    size = len(A)
    for i in range (size):
        k = i+1
        for j in range (k, size):
            if A[i] == A[j]:
                initial.append(A[i])
                len_initial = len(initial)
                for n in range (len_initial):
                    if A[i] == initial[n] and A[i] in initial:
                        final.append(A[i])
    return final









A = [1,2,3,4,4,4,2,2,5,6,1,1]
result = findMultipleDuplicate(A)
print(result)