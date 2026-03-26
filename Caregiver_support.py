# Caregiver App Support
# Program implementations
    # Location
    # Ask about their well-being
    # Where to find support
    # How to cope (hobbies, habits, forums)
    # Community (local groups)
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
    print()
    print ("")
    print ("")
    print ("")
    print ("")