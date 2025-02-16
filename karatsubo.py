import unittest
import math

def karatsuba(a: int, b: int) -> int:
    if a < 10**9 or b < 10**9:
        return a * b
    
    l1 = math.floor(math.log10(a)) + 1
    l2 = math.floor(math.log10(b)) + 1
    l = max(l1, l2)
    mid = l // 2

    p = 10 ** mid
    a1, a2 = divmod(a, p)
    b1, b2 = divmod(b, p)

    z1 = karatsuba(a1, b1)
    z2 = karatsuba(a2, b2)
    z3 = karatsuba(a1 + a2, b1 + b2)
    
    return (10**(2 * mid)) * z1 + (10 ** mid) * (z3 - z1 - z2) + z2

class TestKaratsuba(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(karatsuba(2, 3), 6)

    def test_large_numbers(self):
        self.assertEqual(karatsuba(1234567891337228, 9876543214443434), 12193263129956437967298024360952)
        self.assertEqual(karatsuba(999999999933399494848848, 98723498126234912835691834659826345), 98723498119659877990195781527561627242338570018193703300560)

    def test_numbers_diff_len(self):
        self.assertEqual(karatsuba(1234, 567), 699678)

    def test_edge_cases(self):
        self.assertEqual(karatsuba(0, 12345), 0)
        self.assertEqual(karatsuba(1, 12345), 12345)

if __name__ == "__main__":
    unittest.main()
