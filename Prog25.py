#Program to enter a number and print its reverse
num = int(input("Enter any number: "))
rev = 0
while num > 0:
    rem = num%10
    rev = (rev*10) + rem
    num = num//10
print("reverse number is", rev)
