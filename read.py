import os

nameFile = raw_input("Enter the file to read : ")

if os.path.exists(nameFile):
	f = open(nameFile,"r")
	print f.read()
else:
	print 'The file does not exist'


