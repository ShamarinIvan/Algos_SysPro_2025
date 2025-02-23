import numpy as np
import time
import math
import statistics
from scipy.stats import gmean

def classic_multiply(a,b):
    return np.dot(a,b)

def strassen_8(a, b, threshold=128):
    n = len(a)
    if n <= threshold:
        return classic_multiply(a, b)
    mid = n // 2
    A, B, C, D = a[:mid, :mid], a[:mid, mid:], a[mid:, :mid], a[mid:, mid:]
    E, F, G, H = b[:mid, :mid], b[:mid, mid:], b[mid:, :mid], b[mid:, mid:]

    M1 = strassen_8(A, E, threshold)
    M2 = strassen_8(B, G, threshold)
    M3 = strassen_8(A, F, threshold)
    M4 = strassen_8(B, H, threshold)
    M5 = strassen_8(C, E, threshold)
    M6 = strassen_8(D, G, threshold)
    M7 = strassen_8(C, F, threshold)
    M8 = strassen_8(D, H, threshold)

    C11 = M1 + M2
    C12 = M3 + M4
    C21 = M5 + M6
    C22 = M7 + M8
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

def strassen_7(a, b, threshold=128):
    n = len(a)
    if n <= threshold:
        return classic_multiply(a, b)

    mid = n // 2
    A, B, C, D = a[:mid, :mid], a[:mid, mid:], a[mid:, :mid], a[mid:, mid:]
    E, F, G, H = b[:mid, :mid], b[:mid, mid:], b[mid:, :mid], b[mid:, mid:]

    P1 = strassen_7(A, F - H, threshold)
    P2 = strassen_7(A + B, H, threshold)
    P3 = strassen_7(C + D, E, threshold)
    P4 = strassen_7(D, G - E, threshold)
    P5 = strassen_7(A + D, E + H, threshold)
    P6 = strassen_7(B - D, G + H, threshold)
    P7 = strassen_7(A - C, E + F, threshold)

    Q1 = P5 + P4 - P2 + P6
    Q2 = P1 + P2
    Q3 = P3 + P4
    Q4 = P1 + P5 - P3 - P7
    C = np.vstack((np.hstack((Q1, Q2)), np.hstack((Q3, Q4))))
    return C


def format_table(benchmarks, algos, results):
    len1 = max([len(el) for el in benchmarks])
    len2 = max([len(el) for el in algos])
    a = "| Benchmark" + " "*(len1-9)+" |"
    tempArr = [[len(str(el)) for el in list(column)] for column in zip(*results)]
    maximums = [max(el) for el in tempArr]
    for i in range(len(algos)):
        a += " " + str(algos[i]) + " "*(maximums[i]-len(algos[i]) if maximums[i] >= len(algos[i]) else 0) +" |"
    print(a)
    print("|" + (len(a)-2)*"-" + "|")
    for i in range(len(benchmarks)):
        a = "| " + str(benchmarks[i]) + " "*(len1-len(benchmarks[i]) if len1 >= 9 else 9-len(benchmarks[i]))+" |"
        for j in range(len(algos)):
            a += " " + str(results[i][j]) + ((maximums[j]-len(str(results[i][j]))) if maximums[j] >= len(algos[j]) else len(algos[j])-len(str(results[i][j])))*" " + " |"
        print(a)

def benchmark(alg1, alg2, alg3, data, iterations=100):
    n = len(data)
    for i in range(n):
        a, b = data[i]
        print(f"Test Case №{i}:\n")

        times_alg1 = []
        times_alg2 = []
        times_alg3 = []

        for _ in range(iterations):
            start = time.time()
            alg1(a, b)
            times_alg1.append(time.time() - start)

            start1 = time.time()
            alg2(a, b)
            times_alg2.append(time.time() - start1)

            start2 = time.time()
            alg3(a, b)
            times_alg3.append(time.time() - start2)

        results = [
            [statistics.mean(times_alg1), statistics.mean(times_alg2), statistics.mean(times_alg3)],
            [statistics.stdev(times_alg1), statistics.stdev(times_alg2), statistics.stdev(times_alg3)],
            [gmean(times_alg1), gmean(times_alg2), gmean(times_alg3)]
        ]

        format_table(
            ["sample mean", "sample standard deviation", "geometric mean"],
            ["classic_multiply", "strassen-8", "strassen-7"],
            results
        )
        print("\n")

a4 = np.random.randint(0,10, (16,16))
b4 = np.random.randint(0,10, (16,16))
a5 = np.random.randint(0,10, (32,32))
b5 = np.random.randint(0,10, (32,32))
a6 = np.random.randint(0,10, (64,64))
b6 = np.random.randint(0,10, (64,64))
a7 = np.random.randint(0,10, (128,128))
b7 = np.random.randint(0,10, (128,128))
a8 = np.random.randint(0,10, (256,256))
b8 = np.random.randint(0,10, (256,256))
a9 = np.random.randint(0,10, (512,512))
b9 = np.random.randint(0,10, (512,512))
data = [[a4,b4],[a5,b5],[a6,b6],[a7,b7],[a8,b8],[a9,b9]]
benchmark(classic_multiply, strassen_8, strassen_7, data)