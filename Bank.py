import time

#opens or Creates the .txt file, sharing the directory of the scripts#
text_file = open ("Account" ,"w")
#writes the variable into the .txt file#

print("STATE BANK OF INDIA")
print ('ACCOUNT OPENING WIZARD')

print ("Enter your Mobile Number")
mob = input ("")    
text_file.write(mob + '\n')

print ("Email")
mail = input ("")
text_file.write(mail + '\n')

print ("Ref")
ref = input ("")
text_file.write(ref +'\n')

print("Enter your Name")
Name = input ("")
text_file.write(Name + '\n')

print("Enter Your Father Name")
Father = input ("")
text_file.write(Father + '\n')

print("Nominee for the account holder from this relavent bank")
nominee = input("")
text_file.write(nominee + '\n')

print("Any Loans Pending from Previous Bank")
Loan = input("")
text_file.write(Loan + '\n')

print ("Do You Hold any Other Accounts")
print ("if there Please Mention")
Bank = input("")
text_file.write(Bank + '\n')

print ("Enter you Aadhar Card Number")
aadhar = input ("")
print ("Enter Your Pan Card Number")
pan = input ("")

print ("checking PAN Details, Please Wait")
time.sleep(6)

print ("Please Wait for a while......!")
time.sleep(5)

print ("please Wait Your Information is adding in our Database.....")
time.sleep(5)

print ("Checking for existing Account")
time.sleep(7)

print ("Generating Account Number Please Wait")
time.sleep(4)

import random
x = random.randrange(0,10000000)
num = print (x)

print ("Enter above number to Save in our Database")
num = input("")
text_file.write(num + '\n')

text_file.close()
#close the .txt file#

print ("You are Done, Thank You")


