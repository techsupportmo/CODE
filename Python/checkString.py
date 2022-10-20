# This program checks whether a string has at least one letter and one number

def checkString(str):

    # Set flag to check letter
    letterFlag = False

    # Set flag to check number
    numFlag = False

    for i in str:

        if (i.isalpha()):
            letterFlag = True

        if(i.isdigit()):
            numFlag = True
    
    return numFlag and letterFlag



print(checkString("kjkjkjkjlkjljklkjl"))
print(checkString("142324324234234234"))
print(checkString("bruh123"))