score = int(input("Enter your score: "))

grade = 0

if score >= 50:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
else:
    grade = "F"
    print("แดก F แล้วไปลงเรียนใหม่")

print("Your grade is", grade)