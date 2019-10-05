#create a program to sort even and odd numbers
# 1. Prompt user for a number
# 2. Evaluate if number is even or odd
# 3. Return even or odd

#number = int(input("Please Enter a Number"))
def isEvenOdd(number):
    if(number%2 == 0):
        return("This is an even number")
    else:
        return("This is an odd number")

for i in range(10):
    number = int(input("Please Enter a Number"))
    print(isEvenOdd(number))
