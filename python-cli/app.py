#Import Modules
import random

#Functions
def CheckMath(userAnswer):
    if userAnswer != 'stop':
        userAnswer = int(userAnswer)
        global usercorrect, MorD, Num1, Num2, userwrong, questions

        if MorD == "m":
            if userAnswer == (int(Num1 * Num2)):
                questions += 1
                usercorrect += 1
                return("Yes that's correct!")
            else:
                questions += 1
                userwrong += 1
                return("Wrong, but good try!")
        if MorD == "d": 
            if userAnswer == (Num2):
                questions += 1
                usercorrect += 1
                return("Yes, thats correct!")                
            else:
                questions += 1
                userwrong += 1           
                return("Wrong, but good try!")


# def CheckMupliyMath(userAnswer):
   # if userAnswer != "stop":
    #    userAnswer = int(userAnswer)
    #    global usercorrect
    #    global userwrong
     #   global questions
     #   if userAnswer == (int(Num1 * Num2)):
     #       questions += 1
     #       usercorrect += 1
     #       return("Yes that's correct!")
     #   else:
      #      questions += 1
      #      userwrong += 1
       #     return("Wrong, but good try!")
        

#def CheckDivideMath(userAnswer):
   # if userAnswer != "stop":
    #    userAnswer = (int(userAnswer))
   #     global usercorrect
    #    global userwrong
    #    global questions
    #    if userAnswer == (Num2):
     #       questions += 1
     #       usercorrect += 1
  #          return("Yes, thats correct!")
  #      else:
  #          questions += 1
   #         userwrong += 1           
   #         return("Wrong, but good try!")
        
    
def grade(usercorrect, userwrong, questions, testGrade):
    if questions == 0:
        return "You haven't answered any questions yet!"
    testGrade = ((usercorrect / questions) * 100)
    return("You got " + str(usercorrect) + " out of " + str(questions) + " correct. So you got " + str(userwrong) + " wrong, or " + str(testGrade) + "%." )

#Main part of progarm
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Num1 = random.choice(num1)
Num2 = random.choice(num2)
usercorrect = 0
userwrong = 0
questions = 0
testGrade = 0
userAnswer = ""
MorD = input("Welcome to the math test! Answer the math questions and when you want your grade, press 'stop'. Do you want to do Multiplication (m) or Division (d): ")

#Mulipication
if MorD == "m":
    while not userAnswer == "stop":
        Num1 = random.choice(num1)
        Num2 = random.choice(num2)
        print(str(Num1) + " * " + str(Num2))
        userAnswer = input("Answer: ")
        print(CheckMath(userAnswer))
        if userAnswer == "stop":
            print(grade(usercorrect, userwrong, questions, testGrade))

        
#Divison
if MorD == "d":
    while not userAnswer == "stop":
        Num1 = random.choice(num1)
        Num2 = random.choice(num2)
        Num3 = Num1 * Num2
        print(str(Num3) + " / " + str(Num1))
        userAnswer = input("Answer: ")
        print(CheckMath(userAnswer))
        if userAnswer == "stop":
            print(grade(usercorrect, userwrong, questions, testGrade))