import time
import statistics
from scipy.stats import gmean
from random import randint
def classic_multiply(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2
    A = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    B = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    C = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    D = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return A, B, C, D


def merge_matrices(C11, C12, C21, C22):
    n = len(C11)
    return [C11[i] + C12[i] for i in range(n)] + [C21[i] + C22[i] for i in range(n)]


def strassen_8(a, b, threshold=128):
    n = len(a)
    if n <= threshold:
        return classic_multiply(a, b)

    A, B, C, D = split_matrix(a)
    E, F, G, H = split_matrix(b)

    M1 = strassen_8(A, E, threshold)
    M2 = strassen_8(B, G, threshold)
    M3 = strassen_8(A, F, threshold)
    M4 = strassen_8(B, H, threshold)
    M5 = strassen_8(C, E, threshold)
    M6 = strassen_8(D, G, threshold)
    M7 = strassen_8(C, F, threshold)
    M8 = strassen_8(D, H, threshold)

    C11 = add_matrix(M1, M2)
    C12 = add_matrix(M3, M4)
    C21 = add_matrix(M5, M6)
    C22 = add_matrix(M7, M8)

    return merge_matrices(C11, C12, C21, C22)


def strassen_7(a, b, threshold=128):
    n = len(a)
    if n <= threshold:
        return classic_multiply(a, b)

    A, B, C, D = split_matrix(a)
    E, F, G, H = split_matrix(b)

    P1 = strassen_7(A, sub_matrix(F, H), threshold)
    P2 = strassen_7(add_matrix(A, B), H, threshold)
    P3 = strassen_7(add_matrix(C, D), E, threshold)
    P4 = strassen_7(D, sub_matrix(G, E), threshold)
    P5 = strassen_7(add_matrix(A, D), add_matrix(E, H), threshold)
    P6 = strassen_7(sub_matrix(B, D), add_matrix(G, H), threshold)
    P7 = strassen_7(sub_matrix(A, C), add_matrix(E, F), threshold)

    Q1 = add_matrix(sub_matrix(add_matrix(P5, P4), P2), P6)
    Q2 = add_matrix(P1, P2)
    Q3 = add_matrix(P3, P4)
    Q4 = sub_matrix(sub_matrix(add_matrix(P1, P5), P3), P7)

    return merge_matrices(Q1, Q2, Q3, Q4)


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

def benchmark(alg1, alg2, alg3, data, iterations=10):
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

def generate_matrix(n, min_val=0, max_val=10):
    return [[randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
data = [
    (generate_matrix(16), generate_matrix(16)),
    (generate_matrix(32), generate_matrix(32)),
    (generate_matrix(64), generate_matrix(64)),
    (generate_matrix(128), generate_matrix(128)),
    (generate_matrix(256), generate_matrix(256)),
    (generate_matrix(512), generate_matrix(512))
]

benchmark(classic_multiply, strassen_8, strassen_7, data)
