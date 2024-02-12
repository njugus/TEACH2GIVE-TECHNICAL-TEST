# write a program that accepts a string as input capitalizes the first letter of each word in the string and then
# returns the result string.

def Capilize_String(x):
    myList = []
    # using the split and join () to split and join a string
    txt = x.split()
    for i in txt:
        y = i.capitalize()
        myList.append(y)

    newString = " ".join(myList)
    return newString


myString = str(input("Enter a string: "))
print(Capilize_String(myString))
