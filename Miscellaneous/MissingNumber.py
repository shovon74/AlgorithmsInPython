
def getMissingNo(A):
    n = len(A)
    total = n * (n+1)/2
    sum_of_A = sum(A)
    return sum_of_A - total


A = [1,2,4,5,6]

result = getMissingNo(A)
print(result)