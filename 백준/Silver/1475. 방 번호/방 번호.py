import sys

input = sys.stdin.readline

N = input().strip()

l = [0] * 10

for i in N:
    l[int(i)] += 1

l[6] = (l[6] + l[9] + 1) // 2
l.pop()

print(max(l))
