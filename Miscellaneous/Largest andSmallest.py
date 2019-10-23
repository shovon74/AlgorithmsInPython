def getLargestSmallest(A):
    A.sort()
    res = [A[0], A[-1]]
    return res



A = [1,2,10,4,5,8,9,6,7,3]
result = getLargestSmallest(A)
print(result)