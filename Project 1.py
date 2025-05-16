# Project1: 
# If user give 1 prg print all desktop files 
# If 2 make file by some name 
# 3 make a folder
# 4 friend ko WhatsApp msg Krna hai
# 5 shutdown computer

import os
import pywhatkit
import datetime
a=int(input("Enter a number: "))
if a==1:
    #show all files and folders on my computer
    print(os.listdir("C:\\Users\\HANWANT SINGH\\Desktop"))
elif a==2:
    #create a file on desktop with name "test.txt"
    file = open("C:\\Users\\HANWANT SINGH\\Desktop\\test.txt", "w")
    file.write("Hello World")
    file.close()
elif a==3:
    #Create a folder on desktop with name "test"
    os.mkdir("C:\\Users\\HANWANT SINGH\\Desktop\\test")
elif a==4:
    #sent a whatapp message within 5 seconds to a number
    phone_number = "+919933756273"
    message = "Hello"
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute + 2
    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        print("WhatsApp message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")
   
elif a==5:
    #shutdoun the computer
    os.system("shutdown /s /t 1")