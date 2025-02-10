import unittest
def hIndex(citations):
    n = len(citations)
    gaps = []
    k = 1
    while 2**k-1 < n:
        gaps.append(2**k-1)
        k += 1
    gaps.reverse()
    for gap in gaps:
        for i in range(gap, n):
            temp = citations[i]
            j = i
            while j >= gap and citations[j-gap] > temp:
                citations[j] = citations[j-gap]
                j -= gap
            citations[j] = temp
    h_index = 0
    for i in range(n-1, -1, -1):
        if n-i <= citations[i]:
            h_index = n-i
    return h_index
class TestShellSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(hIndex([3,0,6,1,5]), 3)
        self.assertEqual(hIndex([1,3,1]), 1)

if __name__ == "__main__":
    unittest.main()