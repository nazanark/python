# Task 5: Triangle Type Checker
# Description:
#  Ask the user for 3 side lengths and determine what type of triangle they form:
# Equilateral: all sides equal
# Isosceles: two sides equal
# Scalene: all sides different
# Not a triangle: if the sum of any two sides is not greater than the third
# Example:
# Input: 5, 5, 5  
# Output: Equilateral triangle

firstLen=float(input("Enter 1st side length: "))
secondLen=float(input("Enter 2nd side length: "))
thirdLen=float(input("Enter 3rd side length: "))

if firstLen == secondLen == thirdLen:
    print("Equilatetal")
elif firstLen == secondLen or firstLen == thirdLen or secondLen == thirdLen:
    print("Isosceles")
elif firstLen != secondLen != thirdLen:
    print("Scalene")
else:
    print("Wrong input. Try again!")