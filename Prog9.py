#To count total number of notes in given amount
amt = int(input("Enter the amount: "))
notes = 0
notes += (amt//2000)
amt = amt % 2000

notes += (amt//500)
amt = amt % 500

notes += (amt//200)
amt = amt % 200

notes += (amt//100)
amt = amt % 100

notes += (amt//50)
amt = amt % 50

notes += (amt//20)
amt = amt % 20

notes += (amt//10)
amt = amt % 10

notes += (amt//5)
amt = amt % 5

notes += (amt//2)
amt = amt % 2

notes += (amt//1)
amt = amt % 1

print(notes)
