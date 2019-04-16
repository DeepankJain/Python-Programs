def rsum(n):
    if n <= 1:
        return n
    else:
        return n + rsum(n-1)
num = int(input("Enter any number: "))
ttl = rsum(num)
print("the sum is ", ttl)
