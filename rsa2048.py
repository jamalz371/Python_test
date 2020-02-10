import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(2048, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

messageToEncrypt = raw_input("Enter the message to encrypt : ")
encrypted = publickey.encrypt(messageToEncrypt, 32)
#message to encrypt is in the above line 'encrypt this message'

print 'encrypted message:', encrypted #ciphertext
f = open ('test_rsa.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('test_rsa.txt', 'r')
message = f.read()


decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print 'decrypted message : ', decrypted

f = open ('test_rsa.txt', 'w')
f.write(str(message))
f.write('\n')
f.write(str(decrypted))
f.write('\n')
f.close()
