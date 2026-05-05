# Caregiver App Support - Coping with Care 

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
from tkinter import simpledialog # creates UI popup for user input
from tkinter import messagebox # creates UI for information and ques
import webbrowser

#function that open URLs in the browser
def open_url(url):
    webbrowser.open_new(url)

#**************** START ***********************

# **** Pre-UI Start
# def user_start():
# #Ask for user name, so user can be address and program is more personalable
#     name = input ("Hello, what is your name? ")
#     print ("Hello, " + name)

def user_start():
    name = simpledialog.askstring("Welcome", "Hello, what is your name?")
    if name:
        messagebox.showinfo("Hello, " + name)

# ************* Caregiver explanation **************

def care_explained():
    explanation_text = (
        "First let's review what a caregiver is (◍•ᴗ•◍)\n"
        "-------------------------------------------------\n"
        #Caregiver Explaination
        "Who is a Caregiver?\n"
        "A caregiver is a person who provides physical or psychological care to someone else.\n"
        "Caregivers help others who aren’t able to help themselves fully on their own due to\n"
        "declining health, an illness, injury or an underlying medical condition like:\n"
        "- Alzheimer’s disease or dementia, Parkinson's, MS, Chronic illnesses, etc."
    )
    # popup box that will explain caregiver
    messagebox.showinfo("Who is a Caregiver?", explanation_text)


# **************** Location ***********************************
#asks for user loccation
def location():
    #atlanta is only available city, but will validate answer
    loc = simpledialog.askstring("Location", "Are you located in Atlanta? (Y/N)")
    if loc and loc.lower().startswith('y'):
        messagebox.showinfo("Great! We have resources available for you.")

# **************** Well being ***********************************

#ask user how they are feeling, because this is something every caregiver should acknowlege

        def well_being():
    # Ask user how they are feeling using a dialog box
            mood = simpledialog.askstring("First, we want to ask - How are you feeling?\nEnter G for 'Good', B for 'Bad', or OK for 'Okay':")
    
        # checks if user is okay and if the user inputs incorrectt info
        if mood:
            if mood.lower() == "g":
                messagebox.showinfo("That's great! We are happy you are feeling good.")
            elif mood.lower() == "b":
                messagebox.showinfo("Sorry to hear that, and it's okay to have bad days. ʕ￫ᴥ￩　ʔ \n We will find you resources to help! ʕ　·ᴥ·ʔ ")
            else:
                # safe guard - if uses enter the wrong input 
                messagebox.showinfo("Incorrect input, but thank you for sharing  \( ◡̈)/♥︎ ")

# **************** Support ***********************************
def support():
#     print ("Here are a list of websites to find local support groups")
#     print ("Resources for Caregivers - https://empowerline.org/resource/resources-for-caregivers/")
#     print ("Peer Support Groups - http://shepherd.org/admissions/patient-experience/peer-support/groups/")
   

    #make an additional window on top of my main window
    sw = tk.Toplevel()

    #title of support window
    sw.title("Support")

    #size of the window
    sw.geometry("300x400")

    #adds the text inside of the window; words inside of ""
    tk.Label(sw, text = "Click a link to find support:", font = ("Arial", 10, "bold")).pack(pady = 10)
    
    #creates the hyperlink - makes the text line purple and changes mouse to pointer, so hyperlink is easer to access
    l1 = tk.Label(sw, text = "EmpowerLine Resources", fg = "purple", cursor = "hand2")
    l1.pack(pady = 5)
    
    #makes the link clickable and will open link
    l1.bind("<Button-1>", lambda e: open_url("https://empowerline.org/resource/resources-for-caregivers/"))



# ********** coping *****************
def cope():
    # print("How to cope: ")
    # print("Caring for yourself: https://magazine.medlineplus.gov/article/caring-for-yourself-while-caring-for-others")
    # print("Healthy Ways to Overcome Burnout: https://www.brainandlife.org/articles/healthy-ways-overcome-caregiver-burnout")

    cw = tk.Toplevel()
    cw.title("Coping")
    cw.geometry("300x400")

    


# **************** quotes ***********************************
# inspirational quotes to show user each session

def daily_quote():
    #user chooses a number and the follow quotes will appear by number
    quote_choice = simpledialog.askstring(".𖥔 ݁ ˖𓂃.☘︎ ݁˖ Daily Quote .𖥔 ݁ ˖𓂃.☘︎ ݁","\n Pick a number between 1 and 6 to see your inspirational quote:")

    
    # if statements to go through quotes by choice
    if quote_choice == "1":
        messagebox.showinfo("“It is so important, as a caregiver, not to become so enmeshed in your role that you lose yourself.” - Dana Reeve")

    elif quote_choice == "2":
        messagebox.showinfo("“It is not how much you do, but how much love you put into the doing.” - Mother Teresa")

    elif quote_choice == "3":
        messagebox.showinfo("“Never believe that a few caring people can't change the world. For, indeed, that's all who ever have.” - Margaret Mead")

    elif quote_choice == "4":
        messagebox.showinfo("“Caregiving often calls us to lean into love we didn't know was possible.” - Tia Walker")

    elif quote_choice == "5":
        messagebox.showinfo("“If you have the courage to begin, you have the courage to succeed.” - David Viscott")

    elif quote_choice == "6":
        messagebox.showinfo("“Rest and self-care are so important. When you take time to replenish your spirit, it allows you to serve others from the overflow.” - Eleanor Brown")
    else:
        # safe guard for errors 
        messagebox.showwarning("That was not a number between 1 and 6, please try again!  ฅ^•ﻌ•^ฅ  ")

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

# **** EXIT  ******
#
def exit_program(root_window):
    # message when user exits program
    exit_msg = (
        "Thank you for being a caregiver or wanting to understand one! ♥︎\n\n"
        "♥︎\(◡̈ )/♥︎ Goodbye ♥︎  \( ◡̈)/♥︎"
    )
    messagebox.showinfo("Goodbye", exit_msg)
    root_window.destroy()


# ******** MAIN with UI added ***********
def main():
    root = tk.Tk()
    root.title("Caregiver App Support")
    root.geometry("300x500")

    tk.Label(root, text = "Main Menu", font = ("Arial", 12, "bold")).pack(pady = 10)
    
    # main menu buttons 
    tk.Button(root, text = "Caregiver Explanation", command = care_explained, width = 20).pack(pady = 5)
    tk.Button(root, text = "Location Check", command = location, width = 20).pack(pady = 5)
    tk.Button(root, text = "Well-being Check", command = well_being, width = 20).pack(pady = 5)
    tk.Button(root, text = "Find Support", command = support, width = 20).pack(pady = 5)
    tk.Button(root, text = "How to Cope", command = cope, width = 20).pack(pady = 5)
    tk.Button(root, text = "Daily Quote", command = daily_quote, width = 20).pack(pady = 5)
    tk.Button(root, text = "Caregiver Quiz", command = caregiver_quiz, width = 20).pack(pady = 5)
    
    # Exit Button with your original message
    tk.Button(root, text = "Exit", command = lambda: exit_program(root), bg = "#ddc0ea").pack(pady = 20)

    user_start()
    root.mainloop()

if __name__ == "__main__":
    main()