#opens or Creates the .txt file, sharing the directory of the scripts#
text_file = open ("Greet.txt" ,"w")
Greet = input ("")
text_file.write(Greet)

#writes the variable into the .txt file#

text_file.close()

#close the .txt file#
