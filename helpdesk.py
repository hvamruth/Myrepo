import time

#opens or Creates the .rtf file, sharing the directory of the scripts#
text_file = open ("Ticket.rtf" ,"w")
#writes the variable into the .rtf file#

welcome = print ("OFFICIAL TECHNICAL SUPPORT")
O = print ("Select the Device")
l = print ("1. Laptop")
d = print ("2. Desktop")
option = int(input("\nEnter Your Option : "))

print ("Device Details")

import random
print ("Ticket Number")
x1 = random.randrange(0,10000000)
num = print (x1)

if option == 1:
    print ("Enter Device Serial Number")
    sl = input ("")
    text_file.write(sl + '\n')
    print ("Enter Your Name")
    na = input ("")
    text_file.write(sl + '\n')
    print ("Enter Your Email ID")
    em = input ("")
    text_file.write(em + '\n')
    print ("Enter Your Mobile Number")
    mo = input ("")
    text_file.write(mo + '\n')
    print ("Enter Model Number")
    mg = input ("")
    text_file.write(mg + '\n')
    print ("Enter Device Issue")
    di = input ("")
    text_file.write(di + '\n')
    print ("Address")
    ad = input ("")
    text_file.write(ad + '\n')
    print ("Your Details Below")
    print (sl)
    print (em)
    print (mo)
    print (di)
    print (mg)
    print ("please Wait.....!")

elif option == 2:
    print ("Enter Device Serial Number")
    sl1 = input ("")
    text_file.write(sl1 + '\n')
    print ("Enter Your Email ID")
    em1 = input ("")
    text_file.write(em1 + '\n')
    print ("Enter Your Mobile Number")
    mo1 = input ("")
    text_file.write(mo1 + '\n')
    print ("Enter Model Number")
    mg1 = input ("")
    text_file.write(mg1 + '\n')
    print ("Enter Device Issue")
    di1 = input ("")
    text_file.write(di1 + '\n')
    print ("You Details Below")
    print (sl1)
    print (em1)
    print (mo1)
    print (di1)
    print (mg1)
    print ("please Wait.....!")

text_file.close()
#close the .rtf file#
print ("Thank You. for Writing to us, We we will Contact You in 48 Hours")



