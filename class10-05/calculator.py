#get the first number
#get the second number

#make an individual function to add, subtract, multiply and divide
#return from each function
#template for add function

def add(num1, num2):
    return (num1+num2)

def sub(num1, num2):
    return (num1-num2)

def multiply(num1, num2):
    return (num1*num2)

def division(num1, num2):
    return (num1/num2)

num1 = int(input("Enter the First Number"))
num2 = int(input("Enter the Second Number"))

option = int(input("Enter 1 for Addition \n Enter 2 for Subtration \n Enter 3 for Multiplication \n Enter 4 for Division"))

if (option == 1):
    print("The sum is: ", add(num1,num2))
elif (option == 2):
    print("The difference is: ", sub(num1,num2))
elif (option == 3):
    print("The product is: ", multiply(num1,num2))
elif (option == 4):
    print("the quotient is: ", division(num1,num2))