#Python3 code to linearly search a given element in L
#If x is present then return its location
#otherwise return -1
#Space Complexity O(1)
#Time Complexity O(n)



def linear_search(L, x):
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return -1


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    x = 4
    result = linear_search(L, x)
    if (result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)