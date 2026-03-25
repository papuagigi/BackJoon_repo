import sys
input = sys.stdin.readline

N = int(input().strip())
M = list(map(int, input().split()))
L = int(input().strip())

# 1. 배열 정렬 (O(N log N))
M.sort()

x = 0
left = 0
right = N - 1

# 2. 투 포인터 탐색 (O(N))
while left < right:
    current_sum = M[left] + M[right]
    
    if current_sum == L:
        x += 1
        left += 1
        right -= 1
    elif current_sum < L:
        left += 1
    else:
        right -= 1

print(x)