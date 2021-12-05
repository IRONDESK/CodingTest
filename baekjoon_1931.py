import sys
input = sys.stdin.readline
N = int(input())
timetable = []
answer = 0

for i in range(N):
    timetable.append(list(map(int, input().split())))
    
timetable.sort(key=lambda x:(x[1], x[0])) ## x[1] 오름차순, 같다면 x[2] 오름차순

nexttime = 0
for i, v in enumerate(timetable):
    if i == 0 or nexttime <= v[0] :
        nexttime = v[1]
        answer += 1

print(answer)
