name = str("Bala")
age = int(30)
height = float(5.9)
print("Hello, my name is", name, "I am", age, "years old and my height is", height, "meters tall")
age = age + 5
print("In 5 years, I will be", age, "years old")
width = int(input("Enter the width of the rectangle: "))
length = int(input("Enter the length of the rectangle: "))
area = width * length
print("The area of the rectangle is:", area)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2 
elif operation == "*":
    result = num1 * num2
print("The result is:", float(result))
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
concatenated = str1 + " " + str2
print("The concatenated string is:", concatenated)
