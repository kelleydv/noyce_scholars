"""
Functions 1

The function squareArea below finds the area of a square, given its side length.

1. Write a function that computes the area of a circle given the radius.
2. Wtite a function that computes the area of a circle given the diameter.
3. Write a function called `difference` that finds the area of a square minus
   an inscribed circle.  Use the other functions you have created instead of
   repeating yourself.

"""


def squareArea(s):
    A = s*s
    return A

def circleArea_radius(r):
    pi = 3.14159
    #insert code here
    return #your result

def circleArea_diameter(d):
    pi = 3.14159
    #insert code here
    return #your result



print('The area of a square of side-length 8 is', squareArea(8))
print('The area of a circle of radius 10 is', circleArea_radius(10))
print('The area of a circle of diameter 16 is', circleArea_diameter(16))
print('The area of a square of side-length 10, minus the area of an inscribed circle, is', diff(10))
