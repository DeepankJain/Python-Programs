#Python Function to find maximum of three numbers
def max(x,y,z):
    if x>y and x>z:
        print("x is greater")
    elif y>z and y>x:
        print("y is greater")
    else:
        print("z is greater")
res = max(1,5,4)
print(res)
