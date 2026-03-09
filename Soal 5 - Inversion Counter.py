import random
import time

def brute_inversion(arr):
    total = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                total += 1

    return total


def merge_count(left, right):

    merged = []
    i = j = 0
    inv = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged, inv


def merge_sort_inv(arr):

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr)//2

    L, invL = merge_sort_inv(arr[:mid])
    R, invR = merge_sort_inv(arr[mid:])

    merged, invM = merge_count(L,R)

    return merged, invL + invR + invM


def fast_inversion(arr):
    _, inv = merge_sort_inv(arr)
    return inv


sizes = [1000,5000,10000]

print("Ukuran\tNaive\tSmart\tSama?")

for s in sizes:

    data = [random.randint(0,10000) for _ in range(s)]

    t1 = time.time()
    inv1 = brute_inversion(data)
    t1 = time.time() - t1

    t2 = time.time()
    inv2 = fast_inversion(data)
    t2 = time.time() - t2

    print(s,"\t",round(t1,4),"\t",round(t2,4),"\t",inv1==inv2)