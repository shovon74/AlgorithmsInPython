def remove_duplicate(A, new):
    size = len(A)

    print(new)
    for i in range (size):
        k = i+1
        for j in range (k, size):
            if A[i] == A[j] and A[i] in new:
                del new[i]


    return(new)













A = [1, 2, 3, 4, 4, 5, 3, 6]
new = A[:]
result = remove_duplicate(A, new)
print(new)
