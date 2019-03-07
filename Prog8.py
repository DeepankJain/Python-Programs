#To calculate percentage and grade
Phy = int(input("Enter the marks of Physics: "))
Chem = int(input("Enter the marks of Chemistry: "))
Bio = int(input("Enter the marks of Biology: "))
Math = int(input("Enter the marks of Mathematics: "))
Comp = int(input("Enter the marks of Computer: "))
# Avg = (Phy+Chem+Bio+Math+Comp)/5
if((Phy+Chem+Bio+Math+Comp)/5) >= 90:
    print("Grade A")
elif((Phy+Chem+Bio+Math+Comp)/5) >= 80:
    print("Grade B")
elif((Phy+Chem+Bio+Math+Comp)/5) >= 70:
    print("Grade C")
elif((Phy+Chem+Bio+Math+Comp)/5) >= 60:
    print("Grade D")
elif((Phy+Chem+Bio+Math+Comp)/5) >= 40:
    print("Grade E")
else:
    print("Grade F")
