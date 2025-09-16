#Esto es una funcion
def lower_num(num1, num2):
    if num1 <= num2 :
        lowest = num1
    else:
        lowest = num2
    return lowest
#Esto es una llamada a una funcion
first_num= int(input("enter the first number: "))
second_num= int(input("enter the second number: "))

print("The lowest number is: " + str(lower_num(first_num,second_num)))
