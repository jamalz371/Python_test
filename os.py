import os

print 'current working directory	: ', os.getcwd()
print 'login				: ', os.getlogin()
print 'uid				: ', os.getuid()
print 'uname				: ', os.uname()
print 'times				: ', os.times()
print 'current directory		: ', os.curdir
print 'parent directory		: ', os.pardir
print 'separator			: ', os.sep
print 'list directories 		: ', os.listdir("/home") 

if os.path.exists("file.txt"):
	os.remove("file.txt")
	print 'The file has been successfully removed'
else:
	print 'The file does not exist'

if os.path.exists("folder"):
	os.rmdir("folder")
	print 'The folder has been successfully removed'
else:
	print 'The folder does not exist'

