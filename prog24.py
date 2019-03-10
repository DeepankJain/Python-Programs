#Program to calculate sum of digits of a number
num = int(input("Enter any number: "))
sum = 0
while num > 0:
    dig = num%10
    sum = sum+dig
    num = num//10
print(sum)
