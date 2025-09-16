num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if num1 <= num2:
    lowest = num1
else:
    lowest = num2
    
print("the lowest number is " + str(lowest))
