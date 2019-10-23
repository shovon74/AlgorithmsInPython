# Selection  Sort  Algorithm
#Time complexity O(n^2)

def selection_sort(L):
    n = len(L)
    for i in range(0, n-1):
        index_min = i
        # print('for1')

        for j in range(i+1, n):
            if L[j] < L[index_min]:
                index_min = j
                # print('for2')

        if L[index_min] != i:
            L[index_min], L[i]  = L[i], L[index_min]


if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]
    print("Before sort: ",L)
    selection_sort(L)
    print("After sort:",L)