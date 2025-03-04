def merge(array, i, m, j, n, buffer):
    while i < m and j < n:
        if array[i] < array[j]:
            array[buffer], array[i] = array[i], array[buffer]
            i += 1
        else:
            array[buffer], array[j] = array[j], array[buffer]
            j += 1
        buffer += 1
    while i < m:
        array[buffer], array[i] = array[i], array[buffer]
        buffer += 1
        i += 1
    while j < n:
        array[buffer], array[j] = array[j], array[buffer]
        buffer += 1
        j += 1
def inPlaceMergeSort(array, l, u):
    m, n, w = 0, 0, 0
    if u - l > 1:
        m = l + (u - l) // 2
        w = l + u - m
        wsort(array, l, m, w)
        while w - l > 2:
            n = w
            w = l + (n - l + 1) // 2
            wsort(array, w, n, l)
            merge(array, l, l + n - w, n, u, w)
        i = w
        while i > l:
            j = i
            while j < u and array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j += 1
            i -= 1
def wsort(array, l, u, w):
    m = 0
    if u - l > 1:
        m = l + (u - l) // 2
        inPlaceMergeSort(array, l, m)
        inPlaceMergeSort(array, m, u)
        merge(array, l, m, m, u, w)
    else:
        while l < u:
            array[l], array[w] = array[w], array[l]
            l += 1
            w += 1
a = [3,2,1,4,2,1,2]
inPlaceMergeSort(a, 0, len(a))
print(a)