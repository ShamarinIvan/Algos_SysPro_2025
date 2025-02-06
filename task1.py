import unittest
def division(n, m, a, b):
    ans = ''
    c = 0
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
        self.assertEqual(division(4, 2, 5000, 37), 135)
        self.assertEqual(division(5, 5, 25625, 24), 1067)
        self.assertEqual(division(3, 4, 345, 2222), 0)
if __name__ == "__main__":
    unittest.main()