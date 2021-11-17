
def SplitTest(testString):
    returning = ''

    for a in testString:
        if a.isalnum():
            returning = returning + a
        else:
            returning = returning + ','

    theList = returning.split(',')
    theList.pop(3)

    passwoodCount = theList[3].count(theList[2])
    low = int(theList[0])
    high = int(theList[1])

    if passwoodCount < low:
        #print("Low-Pass %s letter %s low %s high %s" % (theList[3], theList[2], low, high))
        return False
    if passwoodCount > high:
        #print("High-Pass %s letter %s low %s high %s" % (theList[3], theList[2], low, high))
        return False

    return True


#########################3

input_file = open("Day_2_Input.txt", "r")

#lines = input_file.read()

BadListCount = 0

for i in input_file:
    
    TestString =  SplitTest(i)  

    if TestString:
        BadListCount = BadListCount + 1

input_file.close()

print(BadListCount)


