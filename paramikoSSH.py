import paramiko

user_name = "monUsername"
passwd = "monPass"
ip = "monIP"

print "Creating SSH client ....."

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = ip, username = user_name, password = passwd)

print "Connecting with the remote server ....."

cmd = "python /root/code/sha3_final.py"

print "Executing the command ....."

stdin, stdout, stderr = ssh_client.exec_command(cmd)
stdout = stdout.readlines()

print "Results of the command executed :"

print stdout

cmd2= "ls -l"

print "Executing the second command ....."

stdin, stdout, stderr = ssh_client.exec_command(cmd2)
stdout = stdout.readlines()

print "Results of the second command executed :"

print stdout

cmd3= "whoami"

print "Executing the third command ....."

stdin, stdout, stderr = ssh_client.exec_command(cmd3)
stdout = stdout.readlines()

print "Results of the third command executed :"

print stdout


ssh_client.close()

