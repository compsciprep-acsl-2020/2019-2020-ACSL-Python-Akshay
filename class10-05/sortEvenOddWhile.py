def isEvenOdd(number):
    if(number%2 == 0):
        return("This is an even number")
    else:
        return("This is an odd number")

i = 0
while (i < 10):
    number = int(input("Please Enter a Number"))
    print(isEvenOdd(number))