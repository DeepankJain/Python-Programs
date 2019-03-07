#Function to calculate uppercase and lowercase letters
str = input("Enter any string: ")
def checkCase(s):
    if str.isalpha() == False:
        print("Invalid String")
    d = {"UPPER_CASE":0, "lower_case":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["lower_case"] += 1
        else:
            pass
    print("Original String: ", str)
    print("No. of upper case letters",d["UPPER_CASE"])
    print("No of lower case letters",d["lower_case"])
checkCase(str)
