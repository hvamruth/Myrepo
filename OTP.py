import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("your Gmail Account", "You app Password")
    emailid = input ("Enter yout Email:")
    s.sendmail('&&&&&&&&&&' ,emailid,msg)
    a = input("Enter Your OTP >>:")
    if a == OTP:
        print("Verified")

        else:
            print("Invalid OTP, Please Check your OTP again")  
