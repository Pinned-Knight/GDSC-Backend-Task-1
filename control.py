import os
import blueprint

noq = len(blueprint.loq)
class control:

    def __init__(self):
        self.score = 0
        self.ques = 0
        self.skipped = []
 
    def display_ques(self):
        # os.system('cls')
        if self.ques != noq:
            print("Question number "+str((self.ques+1))+":\n")
            print(blueprint.loq[self.ques].text)
            self.takeAns()

    def takeAns(self):
        print("\nEnter your answer(true/false)")
        ans = input("Or Press 0 to Skip (you can attempt them later!):  ")
        ans = ans.lower()
        if ans != "true" and ans != "false" and ans !="0":
            os.system('cls')
            print("Invalid Answer. Try again")
            self.display_ques()
        elif ans == "0":
            self.skipped.append(self.ques)
            os.system('cls')
            print("Question Skipped!")
            self.ques+=1
            self.display_ques()
        else:
            self.checkAns(ans)
    
    def checkAns(self, ans):
        self.ques+=1
        if ans == blueprint.loq[self.ques-1].answer.lower():
            self.score +=2
        else:
            self.score -=1
        

    def exit(self):
        os.system('cls')
        print("Thank you for playing!")
        print("You attempted "+str(self.ques-len(self.skipped))+" questions")
        print("Your Score: "+str(self.score))
        input('Press ENTER to exit')
    
    def skippedq(self,n):
        n = int(n)-1

        print("Question number "+str((n+1))+":")
        print(blueprint.loq[n].text)
        print("\nEnter your answer(true/false): \n")
        ans = input("Or Press 0 to go back! ")
        if ans != "true" and ans != "false" and ans !="0":
            os.system('cls')
            print("Invalid Answer. Try again\n")
            self.skippedq(n+1)
        elif ans == "0":
            pass
        else:
            self.skipped.remove(n)
            if ans == blueprint.loq[n].answer.lower():
                self.score +=2
            else:
                self.score -=1
            