"""
Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
"""

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")
