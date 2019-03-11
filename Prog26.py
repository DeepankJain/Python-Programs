#Program to check whether a number is prime or not
num = int(input("Enter any number"))
def checkPrime(n):
    for i in range(2,n):
        if num % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
checkPrime(num)
