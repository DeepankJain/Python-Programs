#Program to count number of digits in a number
num = int(input("Enter any number: "))
count = 0
while num > 0:
    count += 1
    num = num//10
print("Number of digits in the number are: ", count)
