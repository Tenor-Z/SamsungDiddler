#!  /usr/bin/python

import sys
import socket
import base64
import time, datetime

#It is important to note that for now, both devices (the sender and reciever) MUST be on
#the same network in order for this to work. You will need to enter in the information related
#to your situation so this works properly.

target = "192.168.0.17"     #This is the IP address of the TV which to send requests to

sender = ""                 #This is the IP of the device running this script

mymac = ""                  #The Mac address of the sending device



appstring = "iphone..iapp.samsung"      #The iphone string used for the iPhone app

tvappstring = "iphone.UE40ES5500.iapp.samsung"    #The string of the app

remotename = "Samsung Plugin"    #Name of the remote in case it needs permission. Don't give the secret away

# Function to send keys
#Thanks to Julien Leticher for this
def sendKey(skey, dataSock, appstring):
 messagepart3 = chr(0x00) + chr(0x00) + chr(0x00) + chr(len(
base64.b64encode(skey))) + chr(0x00) + base64.b64encode(skey);
 part3 = chr(0x00) + chr(len(appstring)) + chr(0x00) \
+ appstring + chr(len(messagepart3)) + chr(0x00) + messagepart3
 dataSock.send(part3);

def banner():
	print("S A M S U N G   D I D D L E R")
	print("By Tenor-Z")
	print("Special Thanks to Julien Leticher")

#Here is where the socket gets opened
print("Initalizing socket connection with the TV....")
print("Make sure the TV's IP and your IP are added to the script....")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Initiate the socket connection
sock.connect((target, 55000))               #Specify to communicate with the TV under the port number

#Now to communicate with the TV, we got to encode our details in base64
ipencoded = base64.b64encode(sender)        #Encode both our IP and MAC
macencoded = base64.b64encode(mymac)
messagepart1 = chr(0x64) + chr(0x00) + chr(len(ipencoded)) \
+ chr(0x00) + ipencoded + chr(len(macencoded)) + chr(0x00) \
+ macencoded + chr(len(base64.b64encode(remotename))) + chr(0x00) \
+ base64.b64encode(remotename)      #And send it as the first message

part1 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring \
+ chr(len(messagepart1)) + chr(0x00) + messagepart1
sock.send(part1)        #Send it

messagepart2 = chr(0xc8) + chr(0x00)
part2 = chr(0x00) + chr(len(appstring)) + chr(0x00) + appstring \
+ chr(len(messagepart2)) + chr(0x00) + messagepart2
sock.send(part2)

banner()

#Now here is where we send requests such as the keys to activate.
#I wrote this to solely mess with my relatives

# Now send the keys as you like, e.g.,
print("HERE COMES THE PAIN!!")
loop = 0
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
sendKey("KEY_VOLUP",sock,tvappstring)
loop += 1           #Repeatedly power the TV off lmaoooo

while loop > 0:
	sendKey("KEY_POWEROFF",sock,tvappstring)

#There is also an option to allow an argument to be added as a command to send to the TV

if len(sys.argv) > 1:
	sendKey(sys.argv[1], sock, tvappstring)

# Close the socket when done
sock.close()