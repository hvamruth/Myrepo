#opens or Creates the .txt file, sharing the directory of the scripts#
text_file = open ("Contact.xlsx","w")
print ("Mobile Contact")

#writes the variable into the .txt file#
print ("Enter Your Details")
print ("Name")
Name = input ("")
text_file.write(Name + '\n')

print ("Mobile")
Mobile = input ("")
text_file.write(Mobile + '\n')

print ("Email")
email = input ("")
text_file.write(email + '\n')

print ("Home")
home = input ("")
text_file.write(home + '\n')

print ("Address")
addre = input ("")
text_file.write(addre + '\n')


text_file.close()

#close the .txt file#



