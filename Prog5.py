#To check whether enetered character is vowel or not
Ch = input("Enter any character")
if Ch.isalpha() == False:
    print("Invalid Character")
elif(Ch == 'A' or Ch == 'a' or Ch == 'E' or Ch == 'e' or Ch == 'I' or Ch== 'i' or Ch == 'O' or Ch == 'o' or Ch == 'U' or Ch== 'u'):
    print("Entered Character is a vowel")
else:
    print("Entered Character is a consonant")
