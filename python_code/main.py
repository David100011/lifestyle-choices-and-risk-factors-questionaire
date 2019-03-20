# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:44:10 2019

@author: David Normoyle
"""
while True :
    LogIn_SignUp = input("1)SignUp 2)Login ")
#store username and login details for first signup. store to database
    if LogIn_SignUp == "1":
        print ("SignUp")
        print ("You accept the terms and conditions")
        Enter_Username = input ("Full Name ")
        Enter_DOB = input ("Enter Date of Birth ")
        Enter_Sex = input ("Male/Female ")
        Enter_Living_Location= input ("1) Rural/ 2)Town/ 3)City ")
#score 0, 1 ,2 based on answer
            
            
#verify login/password
        Enter_Password = input ("Please choose a password ")
        break
    if LogIn_SignUp == "2":
        print ("LogIn")
        print ("You accept the terms and conditions")
        while True :
            Username = input ("Username ")
            break
        while True :
            password = input ("Password ")
            break
        break
#This first section will deal with lungs and questions relating to a persons lungs health/condition
while True :
    
    print ("Do you have Asthma?")
    Do_you_have_Asthma = input (" 1) No / 2) Yes ")
    if Do_you_have_Asthma == "1" :
        break
#score 0 and move onto next question
    if Do_you_have_Asthma == "2" :
        break
#score 1 and move on 
    
    print ("Do you suffer from chest infections? ")
    Do_you_suffer_from_chest_infections = input (" 1) No / 2 )Yes ")
    if Do_you_suffer_from_chest_infections == "1" :
        break
#score 0 and onto next question
    if Do_you_suffer_from_chest_infections == "2" :
        break
#score 1 and move to next question
     
    print ("Do you smoke? ")
    Do_you_smoke = input (" 1) No / 2) Yes ")
    if Do_you_smoke == "1":
        break
#score 0 and move onto next question
    if Do_you_smoke =="2" :
    #add score of 1
        print ("How many per day")
        Ciggerettes_Per_Day = input (" 1)0 / 2)1-10 / 3) 10+")
#score 0, 1, 2 based on answer
        
    print ("Do you suffer from a smokers cough?")
    Do_you_suffer_from_a_smokers_cough = input (" 1) No / 2) Yes ")
    if Do_you_suffer_from_a_smokers_cough == "1":
        break
#socre 0 and move o
    if Do_you_suffer_from_a_smokers_cough == "2":
        break
#score 1 and move on
    
    print ("Do you cough up phlegm?")
    Do_You_cough_up_Phlegm = input ("1) No / 2) Yes ")
    if Do_You_cough_up_Phlegm == "1" :
        break
#score 0 and move on
    if Do_You_cough_up_Phlegm == "2" :
        break
#score 1 and move on
    
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
    
    print ("Do you consume sugery drinks?")
    Do_you_consume_sugary_drinks = ("1) No / 2) Yes ")
    if Do_you_consume_sugary_drinks == "1" :
        break
#move onto next question
    if Do_you_consume_sugary_drinks == "2" :
        print ("How often do you consume them?")
        How_often_do_you_consume_them = ("1 Less thena once a week/ 2/ More than once a week 3/ Daily")
#score 0, 1, 2
        break
    
    print ("Do you consume sugary snacks?")
    Do_you_consume_sugary_snacks = input ("1) No/ 2) Yes")
    if Do_you_consume_sugary_snacks == "1": 
        break
#add score of 0
    if Do_you_consume_sugary_snacks == "2":
     print ("How often do you consume them?")
     How_often_do_you_consume_them = ("1 Less then a once a week/ 2/ More than once a week 3/ Daily")
#score 0, 1, 2  
    
        
        


    
        
     
         
        




