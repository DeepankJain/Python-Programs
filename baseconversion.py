num = int(input("Enter a number: "))
rem = []
while num > 0:
    remainder = num%2
    rem.append(remainder)
    num = num//2

for i in range(len(rem)-1,-1,-1):
    print(rem[i], end = "")
