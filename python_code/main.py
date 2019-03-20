# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:53:23 2019

@author: User1
"""
#
#Fisrt you need to login and then use your credenditals to answer the questions
#

import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'medical_records_db'

p_name = ''
p_password = ''
p_sex = ''
p_dob = ''
p_living_location = ''
p_lung_score =  0
p_heart_score = 0
p_diabetes_score =0


#
#the mydb object is used for connecting to the database
#the user has made it to the end of the questionaire, this is where we enter the details into the database
#

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        database='medical_records_db'
    )

accepted_terms_and_conditions = False
#
#login or signup section
#

while True :
    print("Welcome to Medical questionaire")
    LogIn_SignUp = input("1) SignUp 2) Login ")
    if LogIn_SignUp == "2":
        print("Enter username and password to login")
        login_username = input("Username: ")
        login_password = input("Password: ")

        mycursor = mydb.cursor()

        sql = "SELECT * FROM patients WHERE name = %s AND password = %s"

        name_and_password = (login_username, login_password)
        mycursor.execute(sql, name_and_password)

        myresult = mycursor.fetchall()

        if len(myresult) > 0:
            print("login successful")
            for patient in myresult:
                lung_score = int(patient[6])
                heart_score = int(patient[7])
                diabetes_score = int(patient[8])
                print("*****your medical record details*****")
                print("Name: " + patient[1])
                print("Sex: " + patient[3])
                print("DOB: " + patient[4])
                print("Living Location: " + patient[5])
                print("Lung Score: ", lung_score )
                print("Heart Score: ", heart_score  )
                print("Diabetes Score: ", diabetes_score )
                print("************************************")
                
                if lung_score > 1:
                    print("you have very healthy lungs")
                elif lung_score > 0:
                    print("you have moderately healthy lungs")
                elif lung_score > -2:
                    print("your lungs health is poor, your risk of lung disease is mild")
                elif lung_score > -4:
                    print("your lungs health is very poor, your risk of lung disease is moderate")
                elif lung_score > -8:
                    print("your lungs health is extremely poor, your risk of lung disease is very high")

                if heart_score > 1:
                    print("you have a healthy heart")
                elif heart_score > 0:
                    print("you have a moderately healthy heart")
                elif heart_score > -2:
                    print("your heart health is poor, your risk of heart disease is mild")
                elif heart_score > -4:
                    print("your heart health is very poor, your risk of heart disease is moderate")
                elif heart_score > -8:
                    print("your heart health is extremely poor, your risk of heart disease is very high")

                if diabetes_score > 1:
                    print("you are not at risk of diabetes")
                elif diabetes_score > 0:
                    print("you have moderate risk of deveolping diabetes")
                elif diabetes_score > -2:
                    print("you have an increased risk for diabetes")
                elif diabetes_score > -4:
                    print("you may be pre diabtic")
                elif diabetes_score > -8:
                    print("your risk for undiagnosed diabetes is very high")
                break
                
                
        else:
            print("INCORECT PASSWORD: login unsuccessful")
    elif LogIn_SignUp == "1":
        while accepted_terms_and_conditions == False:
            print ("Do you accept the terms and conditions")
            You_accept_terms_and_conditions = input ("1) No 2) Yes ")
            if You_accept_terms_and_conditions == "2":
                accepted_terms_and_conditions = True
                break # break out of the while accepted_terms_and_conditions == False
            else:
#
# break out of the while accepted_terms_and_conditions == False
#
                print("to do this questionaire, you will have to accept the terms and conditions") # stay in while loop until user agrees end of while loop "accepted_terms_and_conditions == False"
#        
#within the "LogIn_SignUp == "1" if statement and the user has accepted the terms and conditions
#
        if accepted_terms_and_conditions == True :
            p_name = input ("Enter full name:")
            p_password = input ("Please choose a password:")
            p_dob = input ("Enter Date of Birth:")
            p_sex = input ("Enter sex: (M) for Male/ (F) for Female\n")
            p_living_location= input ("Enter living location: 1) Rural/ 2)Town/ 3)City: ")
            if p_living_location == "1":
                p_living_location = "Rural"
            elif p_living_location == "2":
                p_living_location = "Town"
            elif p_living_location == "3":
                p_living_location = "City"
        
#
#all questions are within the if statement "if LogIn_SignUp == signup"
#
                
#
#This first section will deal with lungs and questions relating to a persons lungs health/condition
#
                
        print ("\n*************************************\n")
        print ("SignUp was successsful")
        
        print ("\n*************************************\n")
        print ("\n*************************************\n")
        print ("\n*************************************\n")
        

        print ("\n*************************************\n")
        print("*****your medical record details*****")
      
        print("Name: " + p_name)
        print("Sex: " + p_password)
        print("DOB: " + p_dob)
        print("Living Location: " + p_sex)
        print("Lung Score: ", p_lung_score )
        print("Heart Score: ", p_heart_score  )
        print("Diabetes Score: ", p_diabetes_score )
        print("************************************")
        print ("Welcome to the medical health app. Please answer these questions truthfully.")
        print ("\n*************************************\n")
        print ("\n*************************************\n")
        print ("\n*************************************\n")
        
        

        print ("\n*************************************\n")
        print ("\n*************************************\n")
        print ("Do you have Asthma?")
        Do_you_have_Asthma = input (" 1) No / 2) Yes ")
        if Do_you_have_Asthma == "1" :
            p_lung_score = p_lung_score + 1        
        if Do_you_have_Asthma == "2" :
            p_lung_score = p_lung_score - 1 # decrement the lung score because the user has asthma 
    
        print ("Do you suffer from chest infections? ")
        Do_you_suffer_from_chest_infections = input (" 1) No / 2 )Yes ")
        if Do_you_suffer_from_chest_infections == "1" :
            p_lung_score = p_lung_score + 1
        if Do_you_suffer_from_chest_infections == "2" :
            p_lung_score = p_lung_score - 1
  
        print ("Do you smoke? ")
        Do_you_smoke = input (" 1) No / 2) Yes ")
        if Do_you_smoke == "1":
                p_lung_score = p_lung_score + 1
        elif Do_you_smoke == "2":
            print ("How many per day")
            Ciggerettes_Per_Day = input (" 1)1 / 2)2-10 / 3) 10+ ")
            if  Ciggerettes_Per_Day == "1":
                p_lung_score = p_lung_score - 1
            if  Ciggerettes_Per_Day == "2":
                p_lung_score = p_lung_score - 2
            if  Ciggerettes_Per_Day == "3": 
                p_lung_score = p_lung_score - 3   
            
            print ("Do you suffer from a smokers cough?")
            Do_you_suffer_from_a_smokers_cough = input (" 1) No / 2) Yes ")
            if Do_you_suffer_from_a_smokers_cough == "1":
                p_lung_score = p_lung_score + 1
            #
            #score the answer
            #
                if Do_you_suffer_from_a_smokers_cough == "2":
                    p_lung_score = p_lung_score -1
        #
        #score the answer
        #
                   
                print ("Do you cough up phlegm?")
                Do_You_cough_up_Phlegm = input ("1) No / 2) Yes ")
                if Do_You_cough_up_Phlegm == "1" :
                    p_lung_score = p_lung_score + 1
                
            #
            #score the answer
            #
                    
                if Do_You_cough_up_Phlegm == "2" :
                    p_lung_score = p_lung_score - 1
           
        print ("Is there a histroy of lung diease in your family ")
        History_of_Lung_Disease = input (" 1) No / 2) Yes ")
        if History_of_Lung_Disease == "1":
            p_lung_score = p_lung_score + 1
        if History_of_Lung_Disease == "2":
            p_lung_score = p_lung_score - 1
    #    
    # section 2 will deal with heart/diabetes
    #
        
        print ("")
        print ("")
        print ("")
        print ("This section will deal with Diabetes and Coronary Artery Disease")
    

        print (" Do you have Type 1 Diabetes?")
        Do_you_Have_Type1 = input ("1) No / 2 Yes")
        if Do_you_Have_Type1 == "2":
            p_diabetes_score = p_diabetes_score - 1
        print ("More information will be needed.")
        
        if Do_you_Have_Type1 == "1" :
            p_diabetes_score = p_diabetes_score + 1
            

            print ("Have you been ever been checked for type 2 diabetes?")
            Have_you_ever_been_checked_for_Type2 = input ("1 No / 2) Yes ")
            if Have_you_ever_been_checked_for_Type2 == "1" :
             print ("Recommended to get checked as a precaution. Continue to answer questions to see if you are an at risk candidate")
             p_diabetes_score = p_diabetes_score - 1
          
         
             if Have_you_ever_been_checked_for_Type2 == "2" :
              print ("Now answer these questions on your sugar consumtion")
              p_diabetes_score = p_diabetes_score + 1
              
             
                
        
            print ("Do you continue to use sugar?")
            Do_you_consume_sugar = input ("1) No / 2) Yes ")
            if Do_you_consume_sugar == "1" :
                  p_diabetes_score = p_diabetes_score + 1
            elif Do_you_consume_sugar == "2" :
                  p_diabetes_score = p_diabetes_score - 1
                  
              
            print ("Do you consume sugary drinks?")
            Do_you_consume_sugary_drinks = input ("1) No / 2) Yes ")
            if Do_you_consume_sugary_drinks == "1" :
                p_diabetes_score = p_diabetes_score + 1
            elif Do_you_consume_sugary_drinks == "2" :
                p_diabetes_score = p_diabetes_score - 1
                print ("How often do you consume them?")
                How_often_do_you_consume_them = input ("1) Less thena once a week / 2) More than once a week / 3) Daily ")
                if How_often_do_you_consume_them == "1":
                    p_diabetes_score = p_diabetes_score - 1
                elif How_often_do_you_consume_them == "2":
                    p_diabetes_score = p_diabetes_score - 2
                elif  How_often_do_you_consume_them == "3": 
                      p_diabetes_score = p_diabetes_score -3 
                
     
            print ("Do you consume sugary snacks?")
            Do_you_consume_sugary_snacks = input ("1) No/ 2) Yes ")
            if Do_you_consume_sugary_snacks == "1":
                p_diabetes_score = p_diabetes_score + 1 
            elif Do_you_consume_sugary_snacks == "2":
                p_diabetes_score = p_diabetes_score - 1
    
                print ("How often do you consume them?")
                How_often_do_you_consume_them = input ("1) Less then a once a week / 2) More than once a week / 3) Daily ")
                if How_often_do_you_consume_them == "1":
                    p_diabetes_score = p_diabetes_score - 1
                elif How_often_do_you_consume_them == "2":
                    p_diabetes_score = p_diabetes_score - 2
                elif How_often_do_you_consume_them == "3": 
                    p_diabetes_score = p_diabetes_score - 3
                    
               
                
                
             
        mycursor = mydb.cursor()
            
        sql = "INSERT INTO patients (name, password, sex, dob, address, lung_score,heart_score, diabetes_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        patient_details = (p_name, p_password, p_sex, p_dob, p_living_location, p_lung_score, p_heart_score, p_diabetes_score)
            
        mycursor.execute(sql, patient_details)
            
        mydb.commit()
            
        print(mycursor.rowcount, "Your details have successfully been saved in our medical records")
        print("Lung Score , ", p_lung_score)
        print("Heart Score , ", p_heart_score)
        print("Diabetes Score , ", p_diabetes_score)
        print("Please retain this information as it is important.")
        
            
            #
            #When the user gets to teh end their information will be saved and can be views uopon their next login. The results will read for example your lung health is poor or your lung health is good.
