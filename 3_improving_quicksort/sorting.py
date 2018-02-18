# Uses python3
import sys
import random


def partition3(a, l, r):
    """Three way parittion for faster sorting of lists with repeated elemenets.

    param:
    a: list - Unsorted elements
    l: int - index of first value of the array
    r: int - index of last value of the array
    """
    pivot = a[l]
    i = l
    while i <= r:
        if a[i] < pivot:
            a[l], a[i] = a[i], pivot
            l += 1
            i += 1
        elif a[i] > pivot:
            temp_i = a[i]
            a[i] = a[r]
            a[r] = temp_i
            r -= 1
        else:
            i += 1
    return a, l, r

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    a, m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
