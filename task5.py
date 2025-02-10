import unittest.case


def mergeSort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid
    N1 = [0] * n1
    N2 = [0] * n2
    for i in range(n1):
        N1[i] = arr[l + i]
    for i in range(n2):
        N2[i] = arr[mid + 1 + i]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if N1[i] < N2[j]:
            arr[k] = N1[i]
            i += 1
        else:
            arr[k] = N2[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = N1[i]
        k += 1
        i += 1
    while j < n2:
        arr[k] = N2[j]
        k += 1
        j += 1

def wiggleSort(nums):
    n = len(nums)
    mergeSort(nums, 0, n - 1)
    left = nums[:n // 2 + n % 2]
    right = nums[n // 2 + n % 2:]
    nums[::2] = left[::-1]
    nums[1::2] = right[::-1]
    return nums

class TestWiggleSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(wiggleSort([1,5,1,1,6,4]), [1,6,1,5,1,4])
        self.assertEqual(wiggleSort([1,3,2,2,3,1]), [2,3,1,3,1,2])

if __name__ == "__main__":
    unittest.main()