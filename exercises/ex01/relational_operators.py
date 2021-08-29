"""False and True questions"""

left: str = input("left-hand side: ")
right: str = input("right hand side: ")
left_01 = int(left)
right_01 = int(right)

function_01: str = str(left < right)
function_02: str = str(left == right)
function_03: str = str(left >= right)
function_04: str = str(left != right)

__author__ = "730449914"

print(left + " < " + right + " is " + function_01)
print(left + " == " + right + " is " + function_02)
print(left + " >= " + right + " is " + function_03)
print(left + " != " + right + " is " + function_04)