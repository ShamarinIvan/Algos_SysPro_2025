import unittest
def karatsubo(a, b) -> int:
    l1 = len(str(a))
    l2 = len(str(b))
    l = max(l1, l2)
    a = '0' * (l - l1) + str(a)
    b = '0' * (l - l2) + str(b)
    if l == 1:
        return int(a)*int(b)
    mid = l//2
    z1 = karatsubo(int(a[:mid]), int(b[:mid]))
    z2 = karatsubo(int(a[mid:]), int(b[mid:]))
    z3 = karatsubo(int(a[:mid]) + int(a[mid:]), int(b[:mid]) + int(b[mid:]))
    return (10**(2*(l-mid)))*z1+(10**(l - mid))*(z3-z2-z1)+z2
class TestKaratsubo(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(karatsubo(2,3), 6)
    def test_large_numbers(self):
        self.assertEqual(karatsubo(12345, 6789), 83810205)
        self.assertEqual(karatsubo(123456, 789012), 97408265472)
    def test_numbers_diff_len(self):
        self.assertEqual(karatsubo(1234, 567), 699678)
    def test_edge_cases(self):
        self.assertEqual(karatsubo(0,12345), 0)
        self.assertEqual(karatsubo(1, 12345), 12345)
if __name__ == '__main__':
    unittest.main()