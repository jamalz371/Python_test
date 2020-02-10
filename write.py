
nameFile = raw_input("Enter the file name : ")
message = raw_input("Enter the message to write in the file : ")

f = open(nameFile, "w")
f.write(message)
f.close()


