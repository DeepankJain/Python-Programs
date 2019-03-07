#Python function to check whether a number is prime or not
n = int(input("Enter any number"))
def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")

print(isprime(n))
