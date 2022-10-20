def checkRightTriangle(a, b, c):

    # Formula for right triangle: a^2 + b^2 = c^2

    if ( (a*a + b*b == c*c) or  (a*a + c*c == b*b) or (b*b + c*c == a*a)):
        return True
    else:
        return False


print(checkRightTriangle(10,10,10))
print(checkRightTriangle(3,4,5))
