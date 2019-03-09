#Python function to check whther a string is palindrome or not
str = input("Enter any string: ")
def checkPalindrome(teststring):
    i = 0
    j = len(teststring)-1
    while i < j:
        if teststring[i] != teststring[j]:
            print("Not a palindrome")
            break
        else:
            i = i+1
            j = j-1
    if i >= j:
        print("It is a palindrome")
print(checkPalindrome(str))
