A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

result_str = [i for i in result]

x = [0 for i in range(10)]

for num in result:
    for i in range(10):
        if str(i) == num:
           x[i] += 1

for i in x:
    print(i)