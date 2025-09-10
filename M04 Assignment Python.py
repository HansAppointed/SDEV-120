#This program asks the user for their name and grade
#and tells them if they passed the class

name = input("Please enter your name: ")
grade = int(input("Please enter your final grade: "))
PASSING_GRADE = 60

if grade >= PASSING_GRADE:
    print("Hello ",name + ", you passed this class!")

else:
    print("Hello ",name + ", you failed this class.")
