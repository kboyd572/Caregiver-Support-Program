# Caregiver App Support
# Program implementations
    # Location
    # Ask about their well-being
    # Where to find support
    # How to cope (hobbies, habits, forums)
    # Community (local groups)
    # Daily quote
    # Caregiver quiz

import random  #selecting a random daily quote

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

# inspirational quotes to show user each session
quotes = [
    '“It is so important, as a caregiver, not to become so enmeshed in your role that you lose yourself.” - Dana Reeve'
    '“It is not how much you do, but how much love you put into the doing.” - Mother Teresa'
    '“Never believe that a few caring people can’t change the world. For, indeed, that`s all who ever have.” - Margaret Mead'
    # '“Caregiving often calls us to lean into love we didn’t know was possible.” - Tia Walker'
    # '“If you have the courage to begin, you have the courage to succeed.” - David Viscott'
    # '“Rest and self-care are so important. When you take time to replenish your spirit, it allows you to serve others from the overflow.” - Eleanor Brown'
]


#Ask for user name, so user can be address and program is more personalable
name = input ("Hello, what is your name?")
print ("Hello, " + name)

#Caregiver Explaination
print ("Who is a Caregiver?")
print ("A caregiver is a person who provides physical or psychological care to someone else.")
print ("Caregivers help others who aren’t able to help themselves fully on their own due to " \
"\n declining health, an illness, injury or an underlying medical condition like: " \
"\n Alzheimer’s disease or dementia." \
"\n Cancer. \n Chronic illness." \
"\n Mental health conditions." \
" \n Multiple sclerosis." \
"\n Parkinson’s disease.\n Stroke." \
"\n Traumatic brain injuries.")

def location ():
    #get user location - ATL is only open location
    loc = input ("Are you located in Atlanta (metro Atlanta is acceptable)? (Y/N)")
if loc.startswith == 'y':
    print ("Great! We have recoures available for you.")
else:
    print ("")


#ask user how they are feeling, because this is something every caregiver should acknowlege
def well_being():
    mood = input ("First, we want to ask - How are you feeling?\n" \
    "Enter G for 'Good', B for 'Bad', or Ok for 'Okay'")
    if mood.isupper() == "G":
        print ("That is great! We are happy you are feeling good." \
        "\n Please refer to our Main Menu.")
        #return menu()

#menu options 
    # Where to find support
    # How to cope (hobbies, habits, forums)
    # Community (local groups)
    # Daily quote
    # Caregiver quiz
def menu ():
    options_menu = "Menu"
    print ("Please see our options below: ")
print ("") 
         


def support():
    print ("Here are a list of websites to find local support groups")
    print ("Resources for Caregivers - https://empowerline.org/resource/resources-for-caregivers/")
    print ("Peer Support Groups - http://shepherd.org/admissions/patient-experience/peer-support/groups/")
   

def cope ():
    print ("How to cope: ")
    print ("Caring for yourself while caring for others - https://magazine.medlineplus.gov/article/caring-for-yourself-while-caring-for-others")
    print ("Healthy Ways to Overcome Caregiver Burnout - https://www.brainandlife.org/articles/healthy-ways-overcome-caregiver-burnout")
    # link for caregiver tips - https://www.mayoclinic.org/healthy-lifestyle/stress-management/in-depth/caregiver-stress/art-20044784
    # link - https://www.caregiver.org/resource/emotional-side-caregiving/
    # link - https://my.clevelandclinic.org/health/diseases/9225-caregiver-burnout
    # link - https://www.nia.nih.gov/health/caregiving/taking-care-yourself-tips-caregivers

def community ():
    print ("Reddit pages dedicated to caregivers")
    print ("")
    print ("")
    print ("")
    print ("")

def daily_quote():
    print ("")
    print ("")

def caregiver_quiz():
#quiz for user to test their knowledge on caregivers
    print("CAREGIVER KNOWLEDGE QUIZ")
print("____________________________________  ")
print("What do know about caregivers? Answer these questions.")
print("Input the letter of the answer of your choice: (A, B, C, or D).")
print("")

#set the score variable to 0, so it can be calculated as quiz is completed
score = 0

# question 1
print("Question 1: What is caregiver burnout?")
print("A) Feeling bored with caregiving")
print("B) A state of physical, emotional, and mental exhaustion from caregiving")
print("C) Taking too many breaks")
print("D) Being paid too little for caregiving")

ques1_answer = input("Your answer: ")

#if statement - to determince correctness of answers prints to show user their answer is correct.
if ques1_answer == "B" or ques1_answer == "b":
   # prints to show user their answer is correct.
    print("Correct!")
    
    #if the user chooses the correct answer, then score will add increment of 1 
    score = score + 1
else:
    #if incorrect, then score will not increase
    print("Incorrect. The correct answer was B.")
print("")

# question 2
print("Question 2: Which of the following is a healthy coping strategy for caregivers?")
print("A) Ignoring your own needs completely")
print("B) Isolating yourself from friends and family")
print("C) Joining a caregiver support group")
print("D) Working longer hours without breaks")

ques2_answer = input("Your answer: ")
if ques2_answer == "C" or ques2_answer == "c":
    print("Correct!")
    
    #if the user chooses the correct answer, then score will add increment of 1 
    score = score + 1
else:
    #if incorrect, then score will not increase
    print("Incorrect. The correct answer was C.")
print("")

# question 3
print("Question 3: Which condition is commonly associated with needing a caregiver?")
print("A) Alzheimer's disease")
print("B) Common cold")
print("C) Seasonal allergies")
print("D) Minor sprain")

ques3_answer = input("Your answer: ")
if ques3_answer == "A" or ques3_answer == "a":
    print("Correct!")
    
    #if the user chooses the correct answer, then score will add increment of 1 
    score = score + 1

else:
    #if incorrect, then score will not increase
    print("Incorrect. The correct answer was A.")
print("")

# question 4
print("Question 4: What is an early warning sign of caregiver stress?")
print("A) Feeling energized every day")
print("B) Losing interest in activities you once enjoyed")
print("C) Sleeping too well")
print("D) Having too much free time")

ques4_answer = input("Your answer: ")
if ques4_answer == "B" or ques4_answer == "b":
    print("Correct!")
    
    #if the user chooses the correct answer, then score will add increment of 1 
    score = score + 1

else:
    #if incorrect, then score will not increase
    print("Incorrect. The correct answer was B.")
print("")

# question 5
print("Question 5: Which resource provides FREE help connecting caregivers in Atlanta?")
print("A) Doordash")
#resource for caregivers in the atlanta area 
print("B) EmpowerLine (empowerline.org)")
print("C) Search engines")
print("D) Github")

ques5_answer = input("Your answer: ")
if ques5_answer == "B" or ques5_answer == "b":
    print("Correct!")
    
    #if the user chooses the correct answer, then score will add increment of 1 
    score = score + 1
    
else:
    #if incorrect, then score will not increase
    print("Incorrect. The correct answer was B.")
print("")

# final score calculation
print("Calculating final score.")

#calculates score out of 5, using the score variable declared above
print("You got " + str(score) + " out of 5.")

# if statements print depenting on score variable
if score == 5:
    #if 5, then user is an expert 
    print("5/5 - You are an expert on caregiving!")

if score == 4:
    #if 4, then user is an semi-expert
    print("4/5 - You are a semi-caregiver expert! Just one shy!")
    
    #if 3, then user is knowledgable
if score == 3:
    print("3/5 - You're so close, and knowledgeable about caregiving!")

#if score is < 3, then user will not see total out of 5
if score < 3:
    print("You are learning, and that's what caregiving is all about :) ")
print("")