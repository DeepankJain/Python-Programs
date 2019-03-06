#To check whether the triangle is valid or not
x = int(input("Enter the first  side: "))
y = int(input("Enter the second side: "))
z = int(input("Enter the third side: "))
if x + y + z == 180:
    print("It is a valid triangle")
else:
    print("It is not a valid triangle")
