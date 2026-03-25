import sys

input = sys.stdin.readline

N = map(int,input().split())
l = list(map(int,input().split()))
v = int(input())
n=0

for i in l:
    if v==i:
        n+=1
print(n)
