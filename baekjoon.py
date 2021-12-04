order = int(input())
amount3kg = 0
amount5kg = 0

if order % 5 == 0 :
    amount5kg = order / 5
elif (order % 5) % 3 == 0 :
    amount5kg = order // 5
    amount3kg = (order % 5) // 3
else :
    i = 0
    while (order//5)-i >= 0:
        if (order-((order//5)-i)*5) % 3 == 0:
            amount5kg = (order//5)-i
            amount3kg = (order-((order//5)-i)*5) // 3
            break
        else: i += 1

if amount3kg == amount5kg == 0:
    amount3kg = 0
    amount5kg = -1

print(int(amount3kg + amount5kg))
