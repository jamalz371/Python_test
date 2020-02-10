import time


a = raw_input("Enter the first number : ")
b = raw_input("Enter the second number : ")

if a == b :
	print "The numbers are equals"
elif a < b :
	print "The first number is lower than the second number"
elif a > b :
	print "The first number is greater than the second number"
else :
	print "Please enter a number"

c = 0

while c < 10 :
	print "Value of c : ", c
	c += 1

date = raw_input("Do you want to know the current date (Y/N) : ")

if date == "Y" :
	print "date : ", time.asctime(time.localtime())
elif date == "N" :
	print "OK, you do not want to know the current date"
else :
	print "Please chose between Y or N"
