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