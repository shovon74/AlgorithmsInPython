def quick_short(A, low, high):
    if low >= high:
        return

    pivot = partition(A, low, high)
    quick_short(A, low, pivot - 1)
    quick_short(A, pivot + 1, high)


def partition(A, low, high):
    pivot_index = A[high]
    i = low - 1

    for j in range(low, high):
        if A[j] < pivot_index:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1


if __name__ == "__main__":
    A = [1, 3, 5, 2, 4, 7, 6]

    quick_short(A, 0, len(A) - 1)
    print(A)
