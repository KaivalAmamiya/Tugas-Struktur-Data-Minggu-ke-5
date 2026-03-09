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
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

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