import paramiko

user_name = "monUsername"
passwd = "monPass"
ip = "monIP"

print "Creating SSH client ....."

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = ip, username = user_name, password = passwd)

print "Connecting with the remote server ....."

cmd = "blabla"

while cmd != "salut" :
	cmd = raw_input("shell > ")
	print "Executing the command ....."
	stdin, stdout, stderr = ssh_client.exec_command(cmd)
	stdout = stdout.readlines()

	print "Results of the command executed :"
	print stdout

ssh_client.close()

