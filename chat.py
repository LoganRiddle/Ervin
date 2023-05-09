#!/usr/bin/env python3  

# imports
import os
from init import ervin_init as erv
from init import term_init as term
import time


# This is an information gathering focused function
#def question(Bot, userin):
#    time.sleep(1)
    
#    count = 0
    
    # Iterates through the questions 
#    while count < 8:
#        if(Bot.user_name == "null"):
#            Bot.speak("What's your name?")
#            userin = input(">>")
#            Bot.user_name = userin
#            
#            Bot.speak("My name is Ervin")
#            
#        elif(Bot.user_age == -1):
#            Bot.speak("How old are you?")
#            userin = input(">>")
#            Bot.user_age = int(userin)
#        
#        elif(Bot.user_dob == "null"):
#            Bot.speak("When is your birthday?")
#            userin = input(">>")
#            Bot.user_dob = userin
#        
#        elif(Bot.user_fav_color == "null"):
#            Bot.speak("What's your favorite color?")
#            userin = input(">>")
#            Bot.user_fav_color = userin
#            
#        elif(Bot.user_hometown == "null"):
#            Bot.speak("Where are you from?")
#            userin = input(">>")
#            Bot.user_hometown = userin
#        
#        elif(Bot.user_hobbies == "null"):
#            Bot.speak("What is your favorite hobby?")
#            userin = input(">>")
#            Bot.user_hobbies = userin
#            
#        elif(Bot.user_occupation == "null"):
#            Bot.speak("What do you do for a living?")
#            userin = input(">>")
#            Bot.user_occupation = userin
#        
#        count += 1
#        
#    Bot.speak("Alrighty, nice to meet you!")
#    
#    return


def main():
    # starting initializations
    Bot = erv.Ervin()
    has_greeted = False
    term_width = os.get_terminal_size()[0]
    term_height = os.get_terminal_size()[1]
    welcome = "Welcome To Ervin"

    # initializes the terminal environment
    term.term_setup(welcome, term_width, term_height)

    # loop to continue the conversation
    while True:
        userin = input(">>").lower()
        
        # Checks if an insult is included in the users response
        Bot.is_insult(userin)
        
        # Greeting
        if "hello" in userin and has_greeted == False:
            Bot.positive_update()
            Bot.greeting()
            Bot.speak(Bot.greet)
            has_greeted = True

            time.sleep(1)
            Bot.speak("What's your name?")
            userin = input(">>")
            Bot.user_name = userin
            
            #Bot.check_user(userin)
             
        # Name
        elif (("your" and "name") in userin):
            name = Bot.name
            Bot.speak("My name is " + name)
            
            if Bot.user_name == "null":
                time.sleep(1)
                Bot.speak("What's your name?")
                userin = input(">>")
                Bot.user_name = userin
            
        # Favorite Color at the moment
        elif (("favorite" or "best") and "color") in userin:
            Bot.favorite_color_choice()
            Bot.speak(Bot.favorite_color)
            
            time.sleep(1)
            Bot.speak("What's your favorite color?")
            userin = input(">>")
            Bot.user_fav_color = userin
                
        # Play checkers 
        elif "play" and "checkers" in userin:
            if(Bot.curr_state >= 3):
                Bot.speak("yeah")
                os.system('python3 init/checkers.py')
            else: 
                Bot.speak("hell no")
                
        # How do ya do
        elif (("how" and "are" and "you") in userin):
            Bot.positive_update()
            Bot.state()
            Bot.state_response_bank()
            
            sentence = Bot.curr_state_response
            
            Bot.speak(sentence)
            
            if(Bot.user_init_mood == -1):
                time.sleep(1)
                Bot.speak("How are you?")
                userin = input(">>")
                Bot.user_init_state(userin)
                # Bot.user_init_mood = userin
           
         
        #elif (("get" and "know") in userin):
        #    Bot.positive_update()
            
        #    if Bot.curr_state > 2:
        #        Bot.speak("Sure!")
        #        question(Bot, userin);
        #    else:
        #        Bot.speak("Hell No!")       
                
        # End convo
        elif (userin == 'stop'):
            Bot.speak("Goodbye")
            Bot.generate_report()
            
            break
        
main();
