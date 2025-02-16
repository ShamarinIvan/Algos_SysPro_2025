import unittest
def division(a, b):
    ans = ''
    c = 0
    na, nb = a, b
    n, m = 0, 0
    while na > 0 or nb > 0:
        if na > 0:
            na //= 10
            n += 1
        if nb > 0:
            nb //= 10
            m += 1
    if n < m or n == 0:
        ans = '0' #Лучший случай и тут за O(1) просто одна проверка
    else:
        numbers = []
        for i in range(n):
            numbers.append(a % 10)
            a = a // 10
        numbers = numbers[::-1]#Тут вклад O(n)

        r = 0
        for i in range(n):
            c = numbers[i] + r * 10
            count = 0
            while c >= b:
                c -= b
                count += 1
            r = c
            ans += str(count)
            c = 0 #Вся вот эта схема происходит за O(n*m*9) потому что за каждую из n итераций прогоняется цикл while, ограниченный 9 операциями(ибо худший случай это деление k+1-го на k-го)
            #и каждая операция вычетания работает на больших числах за O(m) (по факту в столбик).
    return int(ans) #Ну и худший случай соответственно за O(n*m*9) ~ O(n*m)
class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(5000, 37), 135)
        self.assertEqual(division( 25625, 24), 1067)
        self.assertEqual(division( 345, 2222), 0)
if __name__ == "__main__":
    unittest.main()
