#creating a file object
# read_object = open("testing.txt","a")
# #writing content into a file
# read_object.write("this is the content\ni want to write in the file")
# #closing the file
# read_object.close()
#reading the content
# extract = read_object.read(5)
# print(extract)
# read_object.close()
#append into file
# import csv
# file_object = open('test.csv', 'r')
# file = csv.reader(file_object)
#
# for row in file:
#     print(row[2])
#
# file_object.close()
import csv
file_object = open('test.csv','a')
file = csv.writer(file_object)
file.writerow(['Gholu','Mr.','22','0','True'])
file_object.close()
