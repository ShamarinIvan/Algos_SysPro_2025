import math
import random

class BloomFilter:
    def __init__(self, n, p):
        self.m = self.calculate_m(n, p)
        self.k = self.calculate_k(n, self.m)
        self.bit_array = [0] * self.m
        self.hash_functions = self.generate_hash_functions()

    @staticmethod
    def calculate_m(n, p):

        if p <= 0 or p >= 1:
            raise ValueError("Probability p must be between 0 and 1")
        m = n*((math.log(p, 0.5))/math.log(2))
        return int(math.ceil(m))

    @staticmethod
    def calculate_k(n, m):
        k = (m / n) * math.log(2)
        return int(math.ceil(k))

    def generate_hash_functions(self):
        functions = []
        for _ in range(self.k):
            a = random.randint(0, self.m - 1)
            b = random.randint(0, self.m - 1)
            c = random.randint(0, self.m - 1)
            d = random.randint(0, self.m - 1)
            functions.append((a, b, c, d))
        return functions

    def hash_ip(self, ip_parts, coefficients):

        a, b, c, d = coefficients
        part1, part2, part3, part4 = ip_parts
        return (a * part1 + b * part2 + c * part3 + d * part4) % self.m

    def add(self, ip_address):
        ip_parts = list(map(int, ip_address.split('.')))
        for coeffs in self.hash_functions:
            index = self.hash_ip(ip_parts, coeffs)
            self.bit_array[index] = 1

    def contains(self, ip_address):
        ip_parts = list(map(int, ip_address.split('.')))
        for coeffs in self.hash_functions:
            index = self.hash_ip(ip_parts, coeffs)
            if self.bit_array[index] == 0:
                return False
        return True

if __name__ == "__main__":
    bloom = BloomFilter(n=1000, p=0.01)

    bloom.add("192.168.1.1")
    bloom.add("10.0.0.1")
    bloom.add("172.16.0.1")

    print(bloom.contains("192.168.1.1"))
    print(bloom.contains("10.0.0.1"))
    print(bloom.contains("8.8.8.8"))