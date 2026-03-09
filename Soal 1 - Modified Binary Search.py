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