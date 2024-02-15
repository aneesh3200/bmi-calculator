weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in centimetres: "))
height_in_metres = height/100
height_squared = height_in_metres * height_in_metres

bmi = weight / height_squared
string_bmi = str(bmi)
first_digit = string_bmi[0]
second_digit = string_bmi[1]
bmmi = int(first_digit+second_digit)

print(f"Your Body Mass Index (BMI) is {bmi}")

if bmi < 18.5:
    print("You are underweight")
for i in range(18, 24):
    if i == bmmi:
        print("you are normal weight")
for k in range(25, 29):
    if k == bmmi:
        print("you are overweight")
if bmi > 29:
    print("you are having obesity")