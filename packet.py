#!/bin/python

from scapy.all import *
from Crypto.Cipher import AES


def chat(msg):

	message = msg
	packet = IP(src="23.56.98.18",dst="172.217.20.195")/ICMP()/message
	srloop(packet)
	packet.show()

def encrypt(msgToEncrypt,pl) :

	message = msgToEncrypt
	padlen = pl
	key = "my secret key 16"
	iv = "my secret iv 16 "
	obj = AES.new(key, AES.MODE_CBC, iv)

	if not (padlen%16) == 0:
		message += padlen * chr(padlen)	
	ciphertext = obj.encrypt(message)
	return ciphertext

def decrypt(msgToDecrypt,pl):

	messageToDecrypt = msgToDecrypt
	padlen = pl
	key = "my secret key 16"
	iv = "my secret iv 16 "
	obj2 = AES.new(key, AES.MODE_CBC, iv)
     
	plaintext = obj2.decrypt(messageToDecrypt)
	if not (padlen%16) == 0:
		plaintext = plaintext[:-padlen]
	return plaintext

def main():

	messageToEncrypt = "This is a test !"
	bs = 16
	padding_length = bs - (len(messageToEncrypt) % bs)

	messageEncrypted = encrypt(messageToEncrypt,padding_length)
	messageDecrypted = decrypt(messageEncrypted,padding_length)
	chat(messageEncrypted)
	
	print "Message initial : ", messageToEncrypt
	print "Message encrypted : ", messageEncrypted
	print "Message decrypted : ", messageDecrypted

main()



