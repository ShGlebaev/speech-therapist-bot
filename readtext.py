import random

def randomtext():
    n = 31
    text = open('text.txt', 'r', encoding='utf-8')
    A = []
    for i in range(n):
        A.append(text.readline(-1))
    for j in range(n):
        A[j] = A[j][0:-2]
    random.shuffle(A)
    return A


# print(randomtext())