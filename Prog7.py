#Validity of a traingle by sides
x = int(input("Enter the first side: "))
y = int(input("Enter the second side: "))
z = int(input("Enter the third side: "))
if(x+y > z and x+z > y and y+z > x):
    print("Valid triangle")
else:
    print("Invalid triangle")
