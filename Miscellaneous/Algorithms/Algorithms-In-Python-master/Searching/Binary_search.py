#Python3 code to Binary search a given element in L
#If x is present then return its location
#otherwise return -1

def binary_search(L, x):
    n = len(L)
    m = n//2

    if (L[m] >= x):
        for i in range(0, m):
            if L[i] == x:
                return i


    elif (L[m] < x):
        for i in range(m+1, n-1):
            if L[i] == x:
                return i

    else:
        return -1




if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6]
    x = 3
    result = binary_search(L, x)
    if (result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)