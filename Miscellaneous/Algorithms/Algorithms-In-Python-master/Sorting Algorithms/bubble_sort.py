# #bubble sort algorithm
# #time complexity O(n^2)
#
# def bubble_sort(L):
#     n = len(L)
#     for i in range (0, n-1):
#         flag = 0
#         for j in range (0, n-1):
#             if L[j] > L[j + 1]:
#                 L[j], L[j+1] = L[j+1], L[j]
#
#
# if __name__ == "__main__":
#     L = [5, 2, 3, 1, 4]
#     print("Before sort: ",L)
#     bubble_sort(L)
#     print("After sort:",L)

from random import randint
from time import time


# unsorted_list = [20, 15, 14, 10, 2, 5, 1, 7, 6]


def bubble_sort(L):
    swap = True
    while swap:
        swap = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swap = True

    return L

# random array generator


def generate_random_array(n):
    L = []
    for j in range(n):
        L.append(randint(1, 100))
    return L


if __name__ == "__main__":
    # L = [5, 2, 3, 1, 4]

    generate_random_array(10)
    print("Before sort: ",generate_random_array(10))
    bubble_sort(generate_random_array(10))
    print("After sort:",generate_random_array(10))