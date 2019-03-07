#Python Function to sum all numbers in list
def sum(myList):
    if len(myList) == 1:
        return myList[0]
    else:
        return myList[0] + sum(myList[1:])
print(sum([1,3,5,7,9]))
