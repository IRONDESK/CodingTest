import sys
input = sys.stdin.readline
N = int(input())
lineup = list(map(int, input().split()))

lineup.sort()
tmp = 0
answer = 0
for i in lineup:
    tmp = tmp + i
    answer += tmp 
    
print(answer)
