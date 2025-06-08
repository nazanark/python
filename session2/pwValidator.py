# Task 3: Password Validator
# Description:
#  Ask the user to input a password.
#  Check if it meets all of the following conditions:
# At least 8 characters long
# Contains the letter “@”
# Does not contain any spaces
# Print:
# "Strong password" if all conditions are met
# Otherwise, print "Weak password"
# Example:
# Input: hello@123  
# Output: Strong password

userPW = input("Enter your password: ")


if len(userPW)>=8 and userPW.find("@") !=-1 and userPW.find("") !=-1:
    print("Strong password")
elif userPW.find(" ") != -1:
    print("No spaces are allowed. Try again!")
else:
    print("Weak password")