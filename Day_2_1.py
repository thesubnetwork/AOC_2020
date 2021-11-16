
def SplitTest(testString):
    returning = ''

    for a in testString:
        if a.isalnum():
            returning = returning + a
        else:
            returning = returning + ','

    theList = returning.split(',')
    theList.pop(3)
    return theList

input_file = open("Day_2_Input.txt", "r")
lines = input_file.read()
input_file.close()

print(lines)

