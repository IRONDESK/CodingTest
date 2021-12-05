n = int(input())
알파벳 = []
for i in range(n) :
    알파벳.append(input())
알파벳.sort(key=lambda x:-len(x)) ## 길이 내림차순 정렬

## 중복 제거
순수알파벳 = [] ## 중복 제거된 알파벳 종류
for i in list("".join(알파벳)) :
    if i not in 순수알파벳:
        순수알파벳.append(i)

print(알파벳)

정답배열 = {}
tmp = []
s = 0 ## 9, 8, 7, 6 ... 만들기 위한 숫자

for i in range(len(알파벳)) :
    j = 0
    m = 0
    while j <= len(알파벳[i]) -1 :
        if i != len(알파벳) - 1:
            자릿수차이 = len(알파벳[i]) - len(알파벳[i+1]) ## 2
        
        if 알파벳[i][j] not in tmp :
            if 자릿수차이 - s > 0 or 자릿수차이 - s < 0:
                tmp.append(알파벳[i][j])
                정답배열[알파벳[i][j]] = 9 - s
                s += 1
                j += 1

            elif 자릿수차이 - s == 0 and i != len(알파벳) - 1:
                tmp.append(알파벳[i + 1][m])
                정답배열[알파벳[i + 1][m]] = 9 - s
                s += 1
                
        else :
            j += 1

            
print(정답배열)


알파벳복제 = 알파벳[:]
for i in range(len(알파벳복제)):
    for k in 정답배열:
        알파벳복제[i] = 알파벳복제[i].replace(k, str(정답배열[k]))
        

알파벳복제 = list(map(int,알파벳복제))
print(sum(알파벳복제))
