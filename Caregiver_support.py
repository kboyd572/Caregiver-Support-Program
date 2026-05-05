# Caregiver App Support
# Program implementations
    # Location
    # Ask about their well-being
    # Where to find support
    # Community support
    # How to cope (hobbies, habits, forums)
    # Daily quote
    # Caregiver quiz

# ***** RUBRIC GUIDELINES:  ********
# ______________________________________________
# Code Functionality:
# Code functions and meets all assignment criteria. No detectable logic errors.

# In Code Comments:
# Comments are complete and well thought out. They can be used to fully follow the logic used in the programs

# Code Design:
# Code design is efficient and well thought out. Student makes good use of functions, decisions, and loops for reusable code bits

# User Experience:
# User Experience is easy and self-evident. UI is well designed and appealing. Software use is intuitive.

# Error Handling:
# Program handles all foreseeable errors. Errors are dealt with in a way that allows the program to continue to run and allows the user to correct the issue.

# CMS (GitHub) Use: 
# Changes are committed regularly and well commented. Readme file is thorough. (Verified through activity log)
# _______________________________________________________________________________________________________________________

#creating UI for program - import tinker Python's GUI 
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import webbrowser



#**************** START ***********************
# def user_start():
# #Ask for user name, so user can be address and program is more personalable
#     name = input ("Hello, what is your name? ")
#     print ("Hello, " + name)

#testing ui greeting 
def user_start():
    name = simpledialog.askstring("Test", "Is the name popup working?")
    if name:
        messagebox.showinfo("Test", f"Hello, {name}! This part works.")

#testing ui closing/exit 
def exit_program(root_window):
    messagebox.showinfo("Goodbye", "Thank you! Goodbye ♥︎")
    root_window.destroy()

# ui foundation 
root = tk.Tk()
root.title("Testing UI ")
root.geometry("300x200")

# testing UI buttings
tk.Button(root, text="Greetings test", command=user_start).pack(pady=10)
tk.Button(root, text=" Exit test", command=lambda: exit_program(root)).pack(pady=10)

user_start()

root.mainloop()

# ************* Caregiver explanation **************
#Caregiver Explaination
def care_explained():
    print ("")
    print ("First let's review what a caregiver is (◍•ᴗ•◍)")
    print ("-------------------------------------------------")
    print("Who is a Caregiver?")
    print("A caregiver is a person who provides physical or psychological care to someone else.")
    print("Caregivers help others who aren’t able to help themselves fully on their own due to")
    print("declining health, an illness, injury or an underlying medical condition like:")
    print("- Alzheimer’s disease or dementia, Parkinson's, MS, Chronic illnesses, etc.")
    print("")


# **************** Location ***********************************
def location ():
    #get user location - ATL is only open location
    loc = input ("Are you located in Atlanta (metro Atlanta is acceptable)? (Y/N)")
    if loc.lower().startswith('y'):
        print ("Great! We have recoures available for you.")
    else:
        print ("")

# **************** Well being ***********************************

#ask user how they are feeling, because this is something every caregiver should acknowlege
def well_being():
    # ask user how they are feeling
    mood = input("First, we want to ask - How are you feeling?\nEnter G for 'Good', B for 'Bad', or OK for 'Okay': ")
    if mood.lower() == "g":
        print("That is great! We are happy you are feeling good.")
    elif mood.lower() == "b":
        print("Sorry to hear that, and it's okay to have bad days. ʕ￫ᴥ￩　ʔ \n We will find you resources to help! ʕ　·ᴥ·ʔ ")
    else:
        print("Incorrect selection, but thank you for sharing.")
    print("")


# **************** Support ***********************************
def support():
    print ("Here are a list of websites to find local support groups")
    print ("Resources for Caregivers - https://empowerline.org/resource/resources-for-caregivers/")
    print ("Peer Support Groups - http://shepherd.org/admissions/patient-experience/peer-support/groups/")
   
# ********** coping *****************
def cope():
    print("How to cope: ")
    print("Caring for yourself: https://magazine.medlineplus.gov/article/caring-for-yourself-while-caring-for-others")
    print("Healthy Ways to Overcome Burnout: https://www.brainandlife.org/articles/healthy-ways-overcome-caregiver-burnout")


# **************** quotes ***********************************
# inspirational quotes to show user each session
def daily_quote():
    print(".𖥔 ݁ ˖𓂃.☘︎ ݁˖ Daily Quote .𖥔 ݁ ˖𓂃.☘︎ ݁˖ ")

    #user will pick a number in order to pick an inspirational quote
    print("Pick a number between 1 and 6 to see your inspirational quote:")
    quote_choice = input("Enter number: ")


    #user chooses a number and the follow quotes will appear by number
    if quote_choice == "1":
        print("“It is so important, as a caregiver, not to become so enmeshed in your role that you lose yourself.” - Dana Reeve")

    elif quote_choice == "2":
        print("“It is not how much you do, but how much love you put into the doing.” - Mother Teresa")

    elif quote_choice == "3":
        print("“Never believe that a few caring people can't change the world. For, indeed, that's all who ever have.” - Margaret Mead")

    elif quote_choice == "4":
        print("“Caregiving often calls us to lean into love we didn't know was possible.” - Tia Walker")

    elif quote_choice == "5":
        print("“If you have the courage to begin, you have the courage to succeed.” - David Viscott")

    elif quote_choice == "6":
        print("“Rest and self-care are so important. When you take time to replenish your spirit, it allows you to serve others from the overflow.” - Eleanor Brown")

    else:
        # if user does not enter a number between 1-6
        print("That was not a number between 1 and 6, please try again!")
        print("                      ฅ^•ﻌ•^ฅ                           ")
    print("")



# **************** QUIZ ***********************************
def caregiver_quiz():
    # quiz for user to test their knowledge on caregivers
    print("CAREGIVER KNOWLEDGE QUIZ")
    print("____________________________________  ")
    print("What do know about caregivers? Answer these questions.")
    print("Input the letter of the answer of your choice: (A, B, C, or D).")
    print("")

    # set the score variable to 0, so it can be calculated as quiz is completed
    score = 0

    # question 1
    while True:
        print("Question 1: What is caregiver burnout?")
        print("A) Feeling bored with caregiving")
        print("B) A state of physical, emotional, and mental exhaustion from caregiving")
        print("C) Taking too many breaks")
        print("D) Being paid too little for caregiving")

        #will print the answer the user has chosen 
        ques1_answer = input("Your answer: ")
        print("You chose: " + ques1_answer)

        #valiates user input within the constraints of the list created (a-d)
        if ques1_answer.lower() in ["a", "b", "c", "d"]:
            if ques1_answer == "B" or ques1_answer == "b":
                 #if correct user will be informed
                print("Correct!")
                score = score + 1
            #if incorrect user will be informed           
            else:
                print("Incorrect. The correct answer was B.")
            break 
        #if input is invalid, loop will make user retry
        else:
            print("Input invalid! Enter A, B, C, or D")
            print("")

    # question 2
    while True:
        print("Question 2: Which of the following is a healthy coping strategy for caregivers?")
        print("A) Ignoring your own needs completely")
        print("B) Isolating yourself from friends and family")
        print("C) Joining a caregiver support group")
        print("D) Working longer hours without breaks")

        ques2_answer = input("Your answer: ")
        print("You chose: " + ques2_answer)

        # validate answer
        if ques2_answer.lower() in ["a", "b", "c", "d"]:
            if ques2_answer == "C" or ques2_answer == "c":
                #if correct user will be informed
                print("Correct!")
                score = score + 1
            #if incorrect user will be informed
            else:
                print("Incorrect. The correct answer was C.")
            break
        #if input is invalid, loop will make user retry
        else:
            print("Input invalid! Enter A, B, C, or D")
            print("")

    # question 3
    while True:
        print("Question 3: Which condition is commonly associated with needing a caregiver?")
        print("A) Alzheimer's disease")
        print("B) Common cold")
        print("C) Seasonal allergies")
        print("D) Minor sprain")

        ques3_answer = input("Your answer: ")
        print("You chose: " + ques3_answer)

        # validate answer
        if ques3_answer.lower() in ["a", "b", "c", "d"]:
            if ques3_answer == "A" or ques3_answer == "a":
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect. The correct answer was A.")
            break
        else:
            print("Input invalid! Enter A, B, C, or D")
            print("")

    # question 4
    while True:
        print("Question 4: What is an early warning sign of caregiver stress?")
        print("A) Feeling energized every day")
        print("B) Losing interest in activities you once enjoyed")
        print("C) Sleeping too well")
        print("D) Having too much free time")

        ques4_answer = input("Your answer: ")
        print("You chose: " + ques4_answer)

        # validate answer
        if ques4_answer.lower() in ["a", "b", "c", "d"]:
            if ques4_answer == "B" or ques4_answer == "b":
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect. The correct answer was B.")
            break
        else:
            print("Input invalid! Enter A, B, C, or D")
            print("")

    # question 5
    while True:
        print("Question 5: Which resource provides FREE help connecting caregivers in Atlanta?")
        print("A) Doordash")
        print("B) EmpowerLine (empowerline.org)")
        print("C) Search engines")
        print("D) Github")

        ques5_answer = input("Your answer: ")
        print("You chose: " + ques5_answer)

        # validate answer
        if ques5_answer.lower() in ["a", "b", "c", "d"]:
            if ques5_answer == "B" or ques5_answer == "b":
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect. The correct answer was B.")
            break
        
        else:
            print("Input invalid! Enter A, B, C, or D")
            print("")

    # final score calculation
    print("Calculating final score.")
    print("You got " + str(score) + " out of 5.")

    # if statements print depending on score variable
    if score == 5:
        print("5/5 - You are an expert on caregiving!")
        print("                     ฅ₍^•⩊ •マⳊ                               ")

    if score == 4:
        print("4/5 - You are a semi-caregiver expert! Just one shy!")
        
    if score == 3:
        print("3/5 - You're so close, and knowledgeable about caregiving!")

    if score < 3:
        print("You are learning, and that's what caregiving is all about :) ")
        print ("                          ദ്ദി◝ ⩊ ◜)                           ")
    print(" ")



# ******** MAIN with UI added ***********
def main ():

    user_start()
root.mainloop()
    # user_start()
    # care_explained()
    # location()
    # well_being()

    
    
# Main menu and view for user
    start_menu = True
    #loop created so user can continously make choices until wanting to exit
    while start_menu == True:
        print("♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎ ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎") 
        print("Please see our options below: ")
        print("1. Where to find support")
        print("2. How to cope")
        print("3. Daily quote")
        print("4. Caregiver quiz")
        print("5. Exit Program")
        print("♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎  ♥︎ ♥︎  ♥︎  ♥︎  ♥︎  ♥︎ ♥︎")

        menu_choice = input("Enter a number to select an option: ")

        if menu_choice == "1":
            support()
        elif menu_choice == "2":
            cope()
        elif menu_choice == "3":
            daily_quote()
        elif menu_choice == "4":
            caregiver_quiz()
        elif menu_choice == "5":
            print("Thank you for being a caregiver or wantining to understand one! ♥︎")
            print("♥︎\(◡̈ )/♥︎ Goodbye ♥︎  \( ◡̈)/♥︎")
            start_menu = False # This breaks the loop and ends the program
        else:
            print("Invalid choice, please select 1-5.")

# start of caregiver app

main()

