import sys

N = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline())
n=0

for i in l:
    if v==i:
        n+=1
print(n)