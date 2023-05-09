#!/usr/bin/env python3

from multiprocessing import current_process
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import os
import csv


# Class defining Ervin to be called later
class Ervin:
    def __init__( self ):
        # Set attributes upon initialization 
        self.mood = 50
        self.name = "Ervin"
        self.curr_state = 3
        self.curr_state_response = "base"
        
        self.greet = "null"
        self.end = "bye goodbye"
        
        # Opinion based attributes
        self.favorite_color = "null";
        
        # Current user info
        self.user_name = "null"
        self.user_age = -1
        self.user_dob = "null"
        self.user_fav_color = "null"
        self.user_hometown = "null"
        self.user_hobbies = "null"
        self.user_occupation = "null"
        self.user_init_mood = -1
        self.user_eoc_mood = -1

        return


    # Sets the state based on values from 0 - 100
    def state( self ):     
        if self.mood <= 20:
            self.curr_state = 1
        elif self.mood > 20 and self.mood < 40:  
            self.curr_state = 2 
        elif self.mood >= 40 and self.mood <= 60:
            self.curr_state = 3  
        elif self.mood > 60 and self.mood <= 80:
            self.curr_state = 4  
        elif self.mood > 80 and self.mood <= 100:
            self.curr_state = 5  
            
        return
    
    
    # writes to the user_state csv of unlabled data
    def unlabled_user_state( self , userin):
        cwd = os.getcwd()
        unlabled_user_state_filepath = cwd +  "/unlabled_data/unlabled_user_state.csv"
        
        # Open the file in append mode
        with open(unlabled_user_state_filepath, 'a', newline='') as user_state_file:
            fieldnames = ["Descriptor","Scale"]
            writer = csv.DictWriter(user_state_file, fieldnames=fieldnames)

            # Write the headers if the file is empty
            if user_state_file.tell() == 0:
                writer.writeheader()

            # Write a row to the file
            writer.writerow({"Descriptor": userin})
        
        return 
    
    
    # Checks if the current user has used the chat bot before
    def check_user( self , userin):
        cwd = os.getcwd()
        report_filepath = cwd +  "/data/report.csv"
        
        with open(report_filepath, 'r', newline='') as report_file:
            # fieldnames = ["name","age","dob","favorite color","Hometown","Hobbies","Occupation","Initial Mood","Mood at EOC"]
            reader = csv.reader(report_file)
  
            next(reader)
            new = 1
            
            for row in reader:
                name = row[0]
                
                if(name.lower().find(userin) != -1):
                    new = 0
                    break
        
        if(new == 0):
            self.speak("Nice to talk to you again!")
        elif (new == 1):
            self.speak("Nice to meet you!")
        
        return 
    
    
    # Function to determine favorite color using the csv data file
    def favorite_color_choice ( self ):
        cwd = os.getcwd()
        color_filepath = cwd + "/data/favorite_colors.csv"
        color_data = open(color_filepath, "r")      
          
        num_blue = 0
        num_yellow = 0
        num_red = 0
        
        for x in color_data:
            if "b" in x:
                num_blue += 1
            elif "r" in x:
                num_red += 1
            elif "y" in x:
                num_yellow += 1    
                
        choice = np.random.randint(2500)
        
        # print(num_blue)
        # print(num_yellow)
        # print(num_red)
        
        if(choice >= 0) and (choice <= (num_blue)):
            self.favorite_color = "blue"
        elif(choice > (num_blue) and (choice <= (num_blue) + (num_red))):
            self.favorite_color = "red"
        elif(choice > (num_blue) + (num_red)) and (choice <= 2500):
            self.favorite_color = "yellow"
            
        color_data.close()
        
        return
    
    
    # Recognizes whether the user is stating how they are feeling
    def user_init_state( self , userin):
        cwd = os.getcwd()
        mood_filepath = cwd +  "/data/possible_mood_states.csv"
        
        with open(mood_filepath, 'r') as mood:
            # fieldnames = ["Descripter", "Scale"]
            reader = csv.reader(mood)
  
            next(reader)
            
            for row in reader:
                # Get the value in the second column (index 1)
                descripter = row[0]
                mood = row[1]
                
                if((descripter.lower() in userin)):
                    self.user_init_mood = int(mood)
                    break
                
        if(self.user_init_mood == -1):
            self.speak("Error: Unable to recognize descriptor")
            self.unlabled_user_state(userin)
            return
        
        if int(mood) <= 20:
            self.speak("I am really sorry to hear that.")
        elif int(mood) > 20 and int(mood) < 40:  
            self.speak("I am sorry to hear that")
        elif int(mood) and int(mood) <= 60:
            self.speak("It is what it is.")
        elif int(mood) > 60 and int(mood) <= 80:
            self.speak("Good to hear")
        elif int(mood) > 80 and int(mood) <= 100:
            self.speak("That is really good to hear!")
        
        return
    
    
    # Greatens mood
    def positive_update ( self ):
        self.mood += 1
        
        return
    
    
    # Worsens mood
    def negative_update ( self ):
        self.mood -= 1
        
        return 
    
    
    # Referencing the insult csv data file, this determines whether the userin is offensive excluding racial slurs
    def is_insult( self , userin):
        cwd = os.getcwd()
        insult_filepath = cwd +  "/data/insults.csv"
        
        with open(insult_filepath, 'r') as insult:
            contents = insult.read()
    
            # Split the string into a list of words
            words = contents.split()
            
            # Iterate over the list of words
            for word in words:
                if (word.lower().find(userin) != -1) :
                    self.mood -= 30
                    self.speak("There is no need for that kind of language")
                    break
        return 
    
    
    # Determines a current state response to how are you?
    def state_response_bank ( self ):
        one_ops = ["horrible", "terrible", "very bad", "miserable"]
        two_ops = ["not great", "bad" ]
        three_ops = ["alright", "fine", "chill"]
        four_ops =  ["good", "nice", "satisfied"]
        five_ops = ["great", "amazing", "fantastic", "terrific"]
        
        if(self.curr_state == 1):
            self.curr_state_response = one_ops[(np.random.randint((len(one_ops)-1)))]
        elif(self.curr_state == 2):
            self.curr_state_response = two_ops[(np.random.randint((len(two_ops)-1)))]
        elif(self.curr_state == 3):
            self.curr_state_response = three_ops[(np.random.randint((len(three_ops)-1)))]
        elif(self.curr_state == 4):
            self.curr_state_response = four_ops[(np.random.randint((len(four_ops)-1)))]
        elif(self.curr_state == 5):
            self.curr_state_response = five_ops[(np.random.randint((len(five_ops)-1)))]
        
        return
    
    
    # Randomizes which greeting to respond with
    def greeting( self ):
        greetings = ["Hello friend", "Hi", "Howdy", "Wassup", "Hey", "Good day"]
        
        greeting_choice = np.random.randint((len(greetings) - 1))
        
        self.greet = greetings[greeting_choice]
        
        return
    
    
    # Final report of the conversation
    def generate_report ( self ):
        cwd = os.getcwd()
        report_filepath = cwd +  "/data/report.csv"
        
        # Open the file in append mode
        with open(report_filepath, 'a', newline='') as report_file:
            fieldnames = ["name","age","dob","favorite color","Hometown","Hobbies","Occupation","Initial Mood","Mood at EOC"]
            writer = csv.DictWriter(report_file, fieldnames=fieldnames)

            # Write the headers if the file is empty
            if report_file.tell() == 0:
                writer.writeheader()

            # Write a row to the file
            writer.writerow({"name": self.user_name, "age": self.user_age, "dob": self.user_dob, "favorite color": self.user_fav_color, "Hometown": self.user_hometown, "Hobbies": self.user_hobbies, "Occupation": self.user_occupation, "Initial Mood": self.user_init_mood, "Mood at EOC": self.user_eoc_mood})
        
        return 
    
    
    # The prints function for all possible outputs
    def speak ( self , sentence):
        print(sentence)
        
        return 
