
print("\n\nTicket Booking System\n")
restart = ('Y')
 
while restart != ('N','NO','n','no'):

print("1.Check PNR status")
print("2.Ticket Reservation")
option = int(input("\nEnter your option : "))
 
if option == 1:
print("Your PNR status is t3")
exit(0)
 
elif option == 2:
people = int(input("\nEnter no. of Ticket you want : "))
name_l = &#91;]
age_l = &#91;]
sex_l = &#91;]
for p in range(people):
name = str(input("\nName : "))
name_l.append(name)
age  = int(input("\nAge  : "))
age_l.append(age)
sex  = str(input("\nMale or Female : "))
sex_l.append(sex)
 
restart = str(input("\nDid you forgot someone? y/n: "))
if restart in ('y','YES','yes','Yes'):
restart = ('Y')
else :
x = 0
print("\nTotal Ticket : ",people)
for p in range(1,people+1):
print("Ticket : ",p)
print("Name : ", name_l&#91;x])
print("Age  : ", age_l&#91;x])
print("Sex : ",sex_l&#91;x])
x += 1
