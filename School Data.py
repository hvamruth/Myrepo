import tkinter
#opens or Creates the .txt file, sharing the directory of the scripts#
text_file = open ("candidate.txt" ,"w")
text_file.write("")

#writes the variable into the .txt file#

print ("DIGITAL FILE ENCRYPTION SYSTEM")
print ("Admission Enroll form")

print ("Name")
Name = input ("")
text_file.write(Name + '\n')
print ("Surname")
Surname = input ("")
text_file.write(Surname + '\n')
print ("Age")
Age = input ("")
text_file.write(Age + '\n')
print ("Sex")
Sex = input ("")
text_file.write(Sex + '\n')
print ("Father Name")
Father = input ("")
text_file.write(Father + '\n')
print ("Mother Name")
Mother = input ("")
text_file.write(Mother + '\n')
print ("Caste")
Caste = input ("")
text_file.write(Caste + '\n')
print ("Average Marks from last class")
Marks = input ("")
text_file.write(Marks + '\n')
print ("School Name")
School = input ("")
text_file.write(School + '\n')
print ("Address")
Address = input ("")
text_file.write(Address + '\n')
print ("Permanent Address")
paddress = input ("")
text_file.write(paddress + '\n')

print ("please Wait Your Information is adding in our Database.....!")
print ("please wait")

text_file.close()
#close the .txt file#
