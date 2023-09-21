import control
import os
os.system('cls')
user = control.control()
def StartMenu():
    print("Welcome To The Quiz!")
    print("\n")
    print("1 - Start Quiz")
    print("2 - Exit")
    n = input("Enter your choice: ")
    if n == "1":
        os.system('cls')
        user.display_ques()
        os.system('cls')
        print("Your Answer was Recorded!")
        NextMenu()

    elif n == "2":
        user.exit()
    else:
        os.system('cls')
        print("Invalid Input!")
        StartMenu()
def NextMenu(): 
    if(user.ques==control.noq):
        print("Do you want to re-attempt any of your skipped questions? ")
        print("1 - Yes")
        print("2 - No")
        n = input("Enter your choice: ")
        if n=="1":
            os.system('cls')
            SkippedMenu()
        elif n=="2":
            user.exit()
        else:
            os.system('cls')
            print("Invalid Input!")
            NextMenu()
    else:    
        print("\n")
        print("1 - Next Question")
        print("2 - Exit")
        n = input("Enter your choice: ")
        if n == "1":
            os.system('cls')
            user.display_ques()
            os.system('cls')
            print("Your Answer was Recorded!")
            NextMenu()

        elif n == "2":
            user.exit()
        else:
            os.system('cls')
            print("Invalid Output!")
            NextMenu()
def SkippedMenu():
    print("Here is a list of remaining skipped questions: ")
    for i in range(len(user.skipped)):
        print("Question "+str(user.skipped[i]+1))
    print("\nEnter the question number which you'd like to re-attempt. Enter 0 to exit")
    n = input()
    skstr = [str(i+1)for i in user.skipped]
    if n == "0":
        user.exit()
    elif n not in skstr:
        os.system('cls')
        print("Invalid Input!")
        SkippedMenu()
    else:
        os.system('cls')        
        user.skippedq(n)
        if len(user.skipped)!=0 :
            os.system('cls')
            SkippedMenu()
        else:
            user.exit()
StartMenu()