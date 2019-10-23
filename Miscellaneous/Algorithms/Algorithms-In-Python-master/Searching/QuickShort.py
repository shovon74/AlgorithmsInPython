def quick_short(A, start, end):
    if start >= end:
        return
    else:
        pivot = partition(A, start, end)
        quick_short(A, start, pivot - 1)
        quick_short(A, pivot + 1, end)


def partition(A, start, end):
    pivot_index = (start+end)//2

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


A = [1, 3, 5, 2, 4, 7, 6]

result = quick_short(A, 0, len(A) - 1)
print(result)
