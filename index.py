num1 = int(input("ระยะทาง : "))
# num2 = int(input("Enter the second number: "))

# sum = int(num1) + int(num2)
# print(sum)

# if num1 > num2:
#     print(num1,">",num2)
# elif num1 < num2:
#     print(num2,">",num1)
# elif num1 == num2:
#     print(num1,"=",num2)


# result = 0
# if num1 > num2:
#     print(num1,">",num2)
#     result = num1 * num2
# elif num1 < num2:
#     print(num2,">",num1)
#     result = num2 / num1
# elif num1 == num2:
#     print(num1,"=",num2)
#     result = num1 + num2

# print(result)

price = 0

if num1 >= 5 and num1 <= 50:
    price = 10
elif num1 > 50 and num1 <= 100:
    price = 15
elif num1 > 100 and num1 <= 300:
    price = 25
elif num1 > 300 and num1 <= 500:
    price = 35
elif num1 > 500:
    price = 45
else:
    print("ส่งฟรี")
    

Vat = price * 0.07 
print("ค่าส่ง",price,"บาท")
print("ภาษี",Vat,"บาท")
print("ราคารวม",price+Vat,"บาท")


