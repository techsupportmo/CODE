def checkRightTriangle(a, b, c):

    # Formula for right triangle: a^2 + b^2 = c^2

    if ( (a*a + b*b == c*c) or  (a*a + c*c == b*b) or (b*b + c*c == a*a)):
        return True
    else:
        return False

def anotherMethod(a, b, c):

    # First store values into an arrary
    sides = []
    sides.append(a)
    sides.append(b)
    sides.append(c)

    # Sort the array in ascending order
    sides.sort()

    # Check pythagorean theorem
    if (sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]):
        return True
    else:
        return False

print(checkRightTriangle(10,10,10))
print(checkRightTriangle(3,4,5))
print("")
print(anotherMethod(12,2,1))
print(anotherMethod(5,4,3))