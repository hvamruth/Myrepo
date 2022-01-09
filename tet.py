#opens or Creates the .txt file, sharing the directory of the scripts#
text_file = open ("Student01.txt" ,"w")

text_file.write("")
#writes the variable into the .txt file#

print ("Admission Enroll form")


print ("Name")
Name = input ("")
text_file.write(Name)
print ("Surname")
Surname = input ("")
text_file.write(Surname)
print ("Age")
Age = input ("")
text_file.write(Age)
print ("Sex")
Sex = input ("")
text_file.write(Name)
print ("Father Name")
Father = input ("")
text_file.write(Father)
print ("Mother Name")
Mother = input ("")
text_file.write(Mother)
print ("Average Marks from last class")
Marks = input ("")
text_file.write(Marks)
print ("School Name")
School = input ("")
text_file.write(School)
print ("Address")
Address = input ("")
text_file.write(Address)
print ("Permanent Address")
paddress = input ("")
text_file.write(paddress)

print ("please Wait Your Information is adding in our Database.....!")

text_file.close()
#close the .txt file#
