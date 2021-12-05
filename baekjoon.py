getMoney = 1000 - int(input())
answer = 0
amount500 = 0
amount100 = 0
amount50 = 0
amount10 = 0
amount5 = 0
amount1 = 0

if getMoney >= 500:
    amount500 = getMoney // 500
    getMoney = getMoney - (500 * amount500)
if getMoney >= 100:
    amount100 = getMoney // 100
    getMoney = getMoney - (100 * amount100)
if getMoney >= 50:
    amount50 = getMoney // 50
    getMoney = getMoney - (50 * amount50)
if getMoney >= 10:
    amount10 = getMoney // 10
    getMoney = getMoney - (10 * amount10)
if getMoney >= 5:
    amount5 = getMoney // 5
    getMoney = getMoney - (5 * amount5)
if getMoney >= 1:
    amount1 = getMoney // 1
    getMoney = getMoney - (1 * amount1)

print(amount500+amount100+amount50+amount10+amount5+amount1)