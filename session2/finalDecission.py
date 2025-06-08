# Task 2: Final Decision
# Description:
#  Take two boolean inputs from the user (True or False) and show the result of and, or, and not operations.
# Example:
# Input:
# First Boolean: True  
# Second Boolean: False  
# Output:
# True and False = False  
# True or False = True  
# not True = False

firstReply = input ("First Boolean: ") == "true"
secondReply = input ("Second Boolean: ")  == "true"

if firstReply and secondReply:
    print("True and True =  True")
elif firstReply and not secondReply:
    print("True and False = False")
elif not firstReply and secondReply:
    print("False and True = False")
else:
    print("False and False = False")



