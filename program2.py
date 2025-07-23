member = input("Enter your Member: ")
price = int(input("Enter your price: "))
date = int(input("Enter your date: "))

discount = 0
deli_price = 0
promo_date = date % 2 != 0

if member == "G":
    if price >= 1000 :
        discount = 15
    else:
        discount = 10
elif member == "S":
    if price >= 1000 :
        discount = 10
    else:
        discount = 5
elif member == "N":
    discount = 0

sum =  price - (price * discount / 100)
 
if promo_date:
    if sum > 500:
        sum = sum - (sum * 5 / 100)
    else:
        sum = sum

if sum >= 800:
    deli_price = 0
else:
    deli_price = 50

total = sum + deli_price
print(total)