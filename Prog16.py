#Python funtion to check whether a number is perfect or not
def is_perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        print("Number is perfect")
    else:
        print("number is not perfect")
print(is_perfect(6))
