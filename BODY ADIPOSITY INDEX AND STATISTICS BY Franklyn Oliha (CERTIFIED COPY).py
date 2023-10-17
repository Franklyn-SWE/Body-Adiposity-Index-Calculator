"""
Author: Franklyn Oliha
Title: Body Adiposity Index and Statics Machine
Date: 05 - 11 - 2020 
"""

import statistics

#FEMALE LIST
Fheight = []
Fhip = []
wbai_list =[]
fAge_list =[]


#MALE LIST
Mheight =[]
Mhip = []
mbai_list =[]
mAgelist =[]

print("                        WELCOME!")
print("THIS PROGRAM WILL CALCULATE  BODY ADIPOSITY INDEX AND  STATISTICS.")
print("                  (MEN AND WOMEN)")

def continueChoice():
    print("Would you like to continue? (Y/N):" ,end ="")
    choice = str(input()).upper()
    if choice =='Y':
        return gender_menu()
        
            
        
    elif choice =='N':
    
        print("Thanks for using this program.")

    else:
        choice != 'Y' and choice != 'N'

        print("Invalid Option. Please enter 'Y'or 'N' ")
        return continueChoice()
    
    
def gender_menu():
    print("Please enter gender (F for Female or M for Male:" ,end ="")
    genderEntered = str(input()).upper()

    if genderEntered=='F':
        return female_menu()
        
    elif genderEntered=='M':
        return male_menu()
    else:
        genderEntered != 'F' and genderEntered != 'M'
        print("Invalid input. Please enter (F or M )")
        return gender_menu()


def female_menu():
    
    while True:
        print("Please enter option 1 - Height in Centimetre")
        print("Please enter option 2 - Height in Metres")
        print("Please enter option 3 - Height in Feet")
        print("Please enter option 4 - Height in Inches")

        fHchoice= str(input())
        if fHchoice=='1':
            print("Enter Height in cm:",end ="")
            fHCM = float(input())
            fHM = fHCM
            print("Height in centimetres is",fHM,"(cm)")
        
        elif  fHchoice=='2':
            print("Enter Height in cm:",end ="")
            fHCM = float(input())
            fHM = (fHCM/100)
            print("Height in metres is",fHM,"(m)")
        
        elif fHchoice=="3":
            print(" Enter Height in cm:", end ="")
            fHCM = float(input())
            fHM = (fHCM/30.48)
            print("Height in Feet is",fHM,"(ft)")

        elif fHchoice=='4':
           print("Enter Height in cm:",end="")
           fHCM = float(input())
           fHM = (fHCM/2.54)
           print("Height in Inches is",fHM,"(in)")

        else:
            fHchoice!= 1 and fHchoice != 2 and fHchoice != 3 and fHchoice != 4
            print("Invalid Input! Please choose from option 1-4")
            
   
        Fheight.append(fHM)
        print(Fheight)
    

        print("Please enter option 1 - Hip in Centimetre")
        print("Please enter option 2 - Hip in Metres")
        print("Please enter option 3 - Hip in Feet")
        print("Please enter option 4 - Hip in Inches")

        fHipchoice= str(input())
        if fHipchoice=='1':
            print("Enter Hip in cm:",end ="")
            fHC = float(input())
            fHC = fHC
            print("Hip in centimetres is",fHC,"(cm)")
        
        elif  fHipchoice=='2':
            print("Enter Hip in cm:",end ="")
            fHC = float(input())
            fHC = (fHC/100)
            print("Hip in metres is",fHC,"(m)")
        
        elif fHipchoice=="3":
            print(" Enter Hip in cm:", end ="")
            fHC = float(input())
            fHC = (fHC/30.48)
            print("Hip in Feet is",fHC,"(ft)")

        elif fHipchoice=='4':
            print("Enter Hip in cm:",end="")
            fHC = float(input())
            fHC = (fHC/2.54)
            print("Hip in Inches is",fHC,"(in)")

        else:
            fHipchoice!= 1 and fHipchoice != 2 and fHipchoice != 3 and fHipchoice != 4
            print("Invalid Input! Please choose from option 1-4")
            
   
        
        Fhip.append(fHC)
        print(Fhip)

        print("Please enter age:",end="")
        wAgeValue = int(input())
        fAge_list.append(wAgeValue)
        print(fAge_list)

    
        wbai = (fHC / (fHM)**1.5)-18
        wbai_list.append(wbai)
        print(wbai_list,"%")
        
   

        if wAgeValue >= 20 and wAgeValue <= 39 and wbai < 21:
            print("You are Underweight")

        elif wAgeValue >=20 and wAgeValue <= 39 and wbai > 21 and wbai <= 33:
            print(" You are Healthy")
    
        elif wAgeValue >=20 and wAgeValue <= 39 and wbai > 33:
            print("You are Overweight")
    
        elif wAgeValue >=20 and wAgeValue <= 39 and wbai > 41:
            print(" You are Obese")


        elif wAgeValue >= 40 and wAgeValue <= 59 and wbai < 23:
            print("You are Underweight")

        elif wAgeValue >= 40 and wAgeValue <= 59 and wbai > 23 and wbai <= 35:
            print("You are Healthy")

        elif wAgeValue >= 40 and wAgeValue <= 59 and wbai > 35:
            print("You are Overweight")

        elif wAgeValue >= 40 and wAgeValue <= 59 and wbai > 41:
            print("You are Obese")


        elif wAgeValue >= 60 and wAgeValue <= 79 and wbai < 25:
            print("You are Underweight")

        elif wAgeValue >= 60 and wAgeValue <= 79 and wbai >=25 and wbai <= 38:
            print("You are Healthy")

        elif wAgeValue >= 60 and wAgeValue <= 79 and wbai > 38:
            print("You are Overweight")

        elif wAgeValue >= 60 and wAgeValue <= 79 and wbai > 43:
            print("You are Obese")

        
        else :
            ("Enter age within the range given")

        return continueChoice()

    

def male_menu():
    
    while True:
        
        print("Please enter option 1 - Height in Centimetre")
        print("Please enter option 2 - Height in Metres")
        print("Please enter option 3 - Height in Feet")
        print("Please enter option 4 - Height in Inches")

        Hchoice= str (input())
        if Hchoice=='1':
            print("Enter Height in cm:",end ="")
            HCM = float(input())
            HM = HCM
            print("Height in centimetres is",HM,"(cm)")
        
        elif  Hchoice=='2':
            print("Enter Height in cm:",end ="")
            HCM = float(input())
            HM = (HCM/100)
            print("Height in metres is",HM,"(m)")
        
        elif Hchoice=="3":
            print(" Enter Height in cm:", end ="")
            HCM = float(input())
            HM = (HCM/30.48)
            print("Height in Feet is",HM,"(ft)")

        elif Hchoice=='4':
           
          print("Enter Height in cm:",end="")
          HCM = float(input())
          HM = (HCM/2.54)
          print("Height in Inches is",HM,"(in)")

        else:
          Hchoice!= 1 and Hchoice != 2 and Hchoice != 3 and Hchoice != 4
          print("Invalid Input! Please choose from option 1-4")
    
           
        
        
        Mheight.append(HM)
        print(Mheight)
    
        
    
        print("Please enter option 1 - Hip in Centimetre")
        print("Please enter option 2 - Hip in Metres")
        print("Please enter option 3 - Hip in Feet")
        print("Please enter option 4 - Hip in Inches")

        mHipchoice= str(input())
        if mHipchoice=='1':
            print("Enter Hip in cm:",end ="")
            mHC = float(input())
            mHC = mHC
            print("Hip in centimetres is",mHC,"(cm)")
        
        elif  mHipchoice=='2':
            print("Enter Hip in cm:",end ="")
            mHC = float(input())
            mHC = (mHC/100)
            print("Hip in metres is",mHC,"(m)")
        
        elif mHipchoice=="3":
            print(" Enter Hip in cm:", end ="")
            mHC = float(input())
            mHC = (mHC/30.48)
            print("Hip in Feet is",mHC,"(ft)")

        elif mHipchoice=='4':
            print("Enter Hip in cm:",end="")
            mHC = float(input())
            mHC = (mHC/2.54)
            print("Hip in Inches is",mHC,"(in)")

        else:
            mHipchoice!= 1 and mHipchoice != 2 and mHipchoice != 3 and mHipchoice != 4
            print("Invalid Input! Please choose from option 1-4")
            
            
   
        Mhip.append(mHC)
        print(Mhip)

    
        print("Please enter age:",end="")
        mAgeValue = int(input())
        mAgelist.append(mAgeValue)
        print(mAgelist)

        mbai = (mHC / (HM)**1.5)-18
        mbai_list.append(mbai)
        print(mbai_list,"%")



        if mAgeValue >=20 and mAgeValue <=39 and mbai < 8:
            print("You are Underweight")

        elif mAgeValue >=20 and mAgeValue <= 39 and mbai >= 8 and mbai <=21:
            print("You are Healthy")

        elif mAgeValue >=20 and mAgeValue <=39 and mbai > 21:
            print("You are Overweight")

        elif mAgeValue >=20 and mAgeValue <= 39 and mbai > 26:
            print("You are Obese")


        elif mAgeValue >=40 and mAgeValue <= 59 and mbai <11:
            print("You are Underweight")
    
        elif mAgeValue >= 40 and mAgeValue <= 59 and mbai >=11 and mbai <=23:
            print("You are Healthy")

        elif mAgeValue >= 40 and mAgeValue <= 59 and mbai > 23:
            print("You are Overwieght")

        elif mAgeValue >= 40 and mAgeValue <= 59 and mbai > 29:
            print("You are Obese")


        elif mAgeValue >= 60 and mAgeValue <= 79 and mbai <13:
            print("You are Underweight")

        elif mAgeValue >= 60 and mAgeValue <= 79 and mbai >=13 and mbai <=25:
            print("You are Healthy")

        elif mAgeValue >= 60 and mAgeValue <= 79 and mbai >25:
            print("You are Underweight")

        elif mAgeValue >= 60 and mAgeValue < 79 and mbai > 31:
            print("You are Obese")

        return continueChoice()


        


continueChoice()


print("Male Age", (mAgelist))
print("Male Height", (Mheight))
print("Male Hip", (Mhip))
print("Male BAI", (mbai_list))

print("Female Age", (fAge_list))
print("Female Height", (Fheight))
print("Female Hip", (Fhip))
print("Female BAI", (wbai_list))

print("The mean height of men is  ",sum(Mheight)/(len(Mheight) or 1))
print("The mean hip of men is",sum(Mhip)/(len(Mhip) or 1))
print("The mean age of men is",sum(mAgelist)/(len(mAgelist) or 1))
print("The mean of men BAI is",sum(mbai_list)/(len(mbai_list) or 1)) 

print("The mean height of women is  ",sum(Fheight)/(len(Fheight) or 1))     
print("The mean hip of women is",sum(Fhip)/(len(Fhip) or 1))
print("The mean age of women is",sum(fAge_list)/(len(fAge_list) or 1))
print("The mean of women BAI is",sum(wbai_list)/(len(wbai_list) or 1)) 



print("The range  height of men is", max(Mheight,default=0)- min(Mheight,default=0 ))
print("The range hip of men is", max(Mhip,default=0) - min(Mhip,default=0))
print("The range age of men is", max(mAgelist,default=0)- min(mAgelist,default=0))
print("The range of men BAI is", max(mbai_list,default=0)- min(mbai_list,default=0)) 

print("The range height of women is", max(Fheight,default=0)-min(Fheight,default=0))     
print("The range hip circumference of women is", max(Fhip,default=0) - min(Fhip,default=0))
print("The range age of women is ", max(fAge_list,default=0) - min(fAge_list,default=0))
print("The range of women BAI is", max(wbai_list,default=0) - min(wbai_list,default=0))


try:
    print("The mode height of men is", statistics.mode(Mheight))
except statistics.StatisticsError:
    print("There is no mode  recorded for height of men")

try:
    print("The mode hip of men is ", statistics. mode(Mhip))
except statistics.StatisticsError:
    print("There is no mode recorded  for hip of men")

try:
    print("The mode age of men is ", statistics.mode(mAgelist))
except statistics.StatisticsError:
    print("There is no mode recorded for men age")

try:
    print("The mode of men BAI is ", statistics.mode(mbai_list))
except statistics.StatisticsError:
    print("There is no mode recorded for men BAI")


try:
    print("The mode height of women is", statistics.mode(Fheight))
except statistics.StatisticsError:
    print("There is no mode  recorded for height of women")
    
try:
    print("The mode hip circumference of women is ", statistics.mode(Fhip))
except statistics.StatisticsError:
    print("There is no mode  recorded for women hip circumference")

try:
    print("The mode age of women is", statistics.mode(fAge_list))
except statistics.StatisticsError:
    print("There is no mode recorded for women age")

try:
    print("The mode of women BAI is", statistics.mode(wbai_list))
except statistics.StatisticsError:
    print("There is no mode  recorded for women BAI")
    
print("GOOD BYE")
    



    
   

