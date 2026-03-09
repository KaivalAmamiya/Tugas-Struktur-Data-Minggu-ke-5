# 📚 Python Algorithms Implementation

Repository ini berisi implementasi beberapa algoritma dasar dalam Python, meliputi Searching, Sorting, dan Array Analysis.
Setiap soal dilengkapi dengan deskripsi soal, kode program, contoh penggunaan, dan output hasil program.

📂 Daftar Soal

Modified Binary Search

Bubble Sort dengan Analisis Langkah

Hybrid Sort

Merge Tiga Sorted Lists

Inversions Counter

1️⃣ Modified Binary Search
📝 Soal

Buatlah program menggunakan Binary Search yang dimodifikasi untuk menghitung jumlah kemunculan suatu nilai dalam list yang sudah terurut.

Program harus dapat:

menemukan kemunculan pertama

menemukan kemunculan terakhir

menghitung total kemunculan nilai tersebut.

💻 Kode Program
def find_first(data, x):
    left = 0
    right = len(data) - 1
    pos = -1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == x:
            pos = mid
            right = mid - 1
        elif data[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return pos


def find_last(data, x):
    left = 0
    right = len(data) - 1
    pos = -1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == x:
            pos = mid
            left = mid + 1
        elif data[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return pos


def count_target(data, x):
    start = find_first(data, x)

    if start == -1:
        return 0

    end = find_last(data, x)

    return end - start + 1


print(count_target([1,2,4,4,4,4,7,9,12],4))
print(count_target([1,2,4,4,4,4,7,9,12],5))
📥 Contoh Input
[1,2,4,4,4,4,7,9,12], 4
[1,2,4,4,4,4,7,9,12], 5
📤 Output
4
0
2️⃣ Bubble Sort dengan Analisis Langkah
📝 Soal

Buatlah program Bubble Sort yang tidak hanya mengurutkan data tetapi juga menampilkan:

jumlah comparisons

jumlah swaps

jumlah passes

Program juga harus menampilkan kondisi array pada setiap pass.

💻 Kode Program
def bubble_sort_analysis(nums):
    arr = nums[:]
    n = len(arr)

    comp = 0
    swap = 0
    step = 0

    for end in range(n-1):
        changed = False
        step += 1

        for i in range(n-1-end):
            comp += 1

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

                swap += 1
                changed = True

        print("Pass", step, ":", arr)

        if not changed:
            break

    return arr, comp, swap, step


data1 = [5,1,4,2,8]
data2 = [1,2,3,4,5]

print("Input:", data1)
r1 = bubble_sort_analysis(data1)
print("Sorted:", r1[0], "Comparisons:", r1[1], "Swaps:", r1[2], "Passes:", r1[3])

print()

print("Input:", data2)
r2 = bubble_sort_analysis(data2)
print("Sorted:", r2[0], "Comparisons:", r2[1], "Swaps:", r2[2], "Passes:", r2[3])
📥 Contoh Input
[5,1,4,2,8]
[1,2,3,4,5]
📤 Output
Input: [5, 1, 4, 2, 8]
Pass 1 : [1, 4, 2, 5, 8]
Pass 2 : [1, 2, 4, 5, 8]
Sorted: [1, 2, 4, 5, 8] Comparisons: 7 Swaps: 4 Passes: 2

Input: [1, 2, 3, 4, 5]
Pass 1 : [1, 2, 3, 4, 5]
Sorted: [1, 2, 3, 4, 5] Comparisons: 4 Swaps: 0 Passes: 1
3️⃣ Hybrid Sort
📝 Soal

Buatlah algoritma Hybrid Sort yang menggabungkan dua metode sorting:

Insertion Sort untuk array kecil

Selection Sort untuk array besar

Program juga harus membandingkan performa antara:

Hybrid Sort

Insertion Sort

Selection Sort

💻 Kode Program
import random

def insertion_ops(arr):
    a = arr[:]
    comp = 0
    move = 0

    for i in range(1, len(a)):
        value = a[i]
        j = i - 1

        while j >= 0 and a[j] > value:
            comp += 1
            a[j+1] = a[j]
            move += 1
            j -= 1

        a[j+1] = value
        move += 1

    return a, comp, move


def selection_ops(arr):
    a = arr[:]
    comp = 0
    swap = 0

    for i in range(len(a)-1):
        m = i

        for j in range(i+1, len(a)):
            comp += 1
            if a[j] < a[m]:
                m = j

        if m != i:
            a[i], a[m] = a[m], a[i]
            swap += 1

    return a, comp, swap


def hybrid(arr, limit=10):
    if len(arr) <= limit:
        return insertion_ops(arr)
    else:
        return selection_ops(arr)


sizes = [50,100,500]

for s in sizes:
    arr = [random.randint(0,1000) for _ in range(s)]

    _,c1,s1 = hybrid(arr)
    _,c2,s2 = insertion_ops(arr)
    _,c3,s3 = selection_ops(arr)

    print(s, c1+s1, c2+s2, c3+s3)
4️⃣ Merge Tiga Sorted Lists
📝 Soal

Buatlah program yang dapat menggabungkan tiga list yang sudah terurut menjadi satu list terurut.

💻 Kode Program
def merge_three(a, b, c):

    i = j = k = 0
    result = []

    while i < len(a) or j < len(b) or k < len(c):

        vals = []

        if i < len(a):
            vals.append((a[i], 'a'))
        if j < len(b):
            vals.append((b[j], 'b'))
        if k < len(c):
            vals.append((c[k], 'c'))

        value, src = min(vals)

        result.append(value)

        if src == 'a':
            i += 1
        elif src == 'b':
            j += 1
        else:
            k += 1

    return result


print(merge_three([1,5,9], [2,6,10], [3,4,7]))
📥 Contoh Input
A = [1,5,9]
B = [2,6,10]
C = [3,4,7]
📤 Output
[1,2,3,4,5,6,7,9,10]
5️⃣ Inversions Counter
📝 Soal

Buatlah program untuk menghitung jumlah inversions dalam sebuah array.

Inversion terjadi jika:

i < j
arr[i] > arr[j]

Program harus menggunakan dua metode:

Naive Method

Merge Sort Method

💻 Kode Program
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
🎯 Tujuan Repository

Repository ini dibuat untuk:

memahami konsep algoritma dasar

mempelajari analisis kompleksitas

membandingkan performa algoritma

melatih implementasi algoritma menggunakan Python
