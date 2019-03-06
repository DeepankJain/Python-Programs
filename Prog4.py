#To check whether a number is divisible by 5 and 11 or not
num1 = int(input("Enter any number:"))
if num1%5 == 0 and num1%11 != 0:
    print("Number is divisible by 5 but not by 11")
elif num1%5 != 0 and num1%11 == 0:
    print("Number is not divisible by 5 but by 11")
else:
    print("Number is divisible by both 5 and 11")
