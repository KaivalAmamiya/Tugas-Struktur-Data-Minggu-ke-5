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
    a = arr[:]
    comp = 0
    swap = 0

    if len(a) <= limit:

        for i in range(1, len(a)):
            key = a[i]
            j = i-1

            while j >= 0 and a[j] > key:
                comp += 1
                a[j+1] = a[j]
                swap += 1
                j -= 1

            a[j+1] = key
            swap += 1

    else:

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


sizes = [50,100,500]

print("Ukuran\tHybrid\tInsertion\tSelection")

for s in sizes:
    arr = [random.randint(0,1000) for _ in range(s)]

    _,c1,s1 = hybrid(arr)
    _,c2,s2 = insertion_ops(arr)
    _,c3,s3 = selection_ops(arr)

    print(s, "\t", c1+s1, "\t", c2+s2, "\t", c3+s3)