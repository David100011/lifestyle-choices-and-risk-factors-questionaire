# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:44:10 2019

@author: David Normoyle
"""

#login or signup will require you to select the option 2 times
while True :
    LogIn_SignUp = input("1) SignUp 2) Login ")
    if LogIn_SignUp == "1":
        print ("Do you accept the terms and conditions")
        You_accept_terms_and_conditions = input ("1) No 2) Yes ")
    if You_accept_terms_and_conditions == "1" :
        continue
    if You_accept_terms_and_conditions == "2" :
            print ("SignUp")
            print ("You accept the terms and conditions. Please enter SignUp again.")
            
    LogIn_SignUp = input("1) SignUp 2) Login ")
    if LogIn_SignUp == "1":  
        
        Enter_Username = input ("Full Name ")
        Enter_Password = input ("Please choose a password ")
        Enter_DOB = input ("Enter Date of Birth ")
        Enter_Sex = input ("Male/Female ")
        Enter_Living_Location= input ("1) Rural/ 2)Town/ 3)City ")
        break
    
    else: 
        if LogIn_SignUp == "2":
            print ("LogIn")
            print ("You accept the terms and conditions, please enyer Login again.")
        while True :
            Username = input ("Username ")
            break
        while True :
            password = input ("Password ")
            break
        break
#This first section will deal with lungs and questions relating to a persons lungs health/condition
print ("")
print ("")
print ("")  
print ("This section will ask questions about your lungs, please answer truthfully.")
while True :
    
    print ("Do you have Asthma?")
    Do_you_have_Asthma = input (" 1) No / 2) Yes ")
    if Do_you_have_Asthma == "1" :
        break
#score 0 and move onto next question, need to find a way to add a score 
    if Do_you_have_Asthma == "2" :
        break
#score 1 and move on 
while True :    
    print ("Do you suffer from chest infections? ")
    Do_you_suffer_from_chest_infections = input (" 1) No / 2 )Yes ")
    if Do_you_suffer_from_chest_infections == "1" :
        break
#score 0 and onto next question
    if Do_you_suffer_from_chest_infections == "2" :
        break
#score 1 and move to next question
while True :    
    print ("Do you smoke? ")
    Do_you_smoke = input (" 1) No / 2) Yes ")
    if Do_you_smoke == "1":
        break
#score 0 and move onto next question
    if Do_you_smoke == "2" :
        print ("How many per day")
        Ciggerettes_Per_Day = input (" 1)0 / 2)1-10 / 3) 10+ ")
    break
#score 0, 1, 2 based on answer
while True :     
    print ("Do you suffer from a smokers cough?")
    Do_you_suffer_from_a_smokers_cough = input (" 1) No / 2) Yes ")
    if Do_you_suffer_from_a_smokers_cough == "1":
        break
#socre 0 and move o
    if Do_you_suffer_from_a_smokers_cough == "2":
        break
#score 1 and move on
while True :    
    print ("Do you cough up phlegm?")
    Do_You_cough_up_Phlegm = input ("1) No / 2) Yes ")
    if Do_You_cough_up_Phlegm == "1" :
        break
#score 0 and move on
    if Do_You_cough_up_Phlegm == "2" :
        break
#score 1 and move on
while True :   
    print ("Is there a histroy of lung diease in your family ")
    History_of_Lung_Disease = input (" 1) No / 2) Yes ")
    if History_of_Lung_Disease == "1":
        break
#score 0 and move on
    if History_of_Lung_Disease == "2":
        break
#score 1 and move on
    break
    
# sectioon 2 will deal with heart/diabetes
    
while True: 
    
    print ("Do you consume sugary drinks?")
    Do_you_consume_sugary_drinks = input ("1) No / 2) Yes ")
    if Do_you_consume_sugary_drinks == "1" :
        break
    if Do_you_consume_sugary_drinks == "2" :
        print ("How often do you consume them?")
    How_often_do_you_consume_them = input ("1) Less thena once a week / 2)/ More than once a week 3)/ Daily ")
    break
#add score
while True :  
    print ("Do you consume sugary snacks?")
    Do_you_consume_sugary_snacks = input ("1) No/ 2) Yes ")
    if Do_you_consume_sugary_snacks == "1": 
        break
    if Do_you_consume_sugary_snacks == "2":
        print ("How often do you consume them?")
        How_often_do_you_consume_them = input ("1) Less then a once a week/ 2)/ More than once a week 3)/ Daily ") 
        break
        break  
        


    
        
     
         
        




