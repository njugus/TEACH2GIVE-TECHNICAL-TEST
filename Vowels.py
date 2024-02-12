# write a program that counts the number of vowels in a sentence

def Count_Vowels(y):
    counter = []
    # store the vowels in a set
    vowels = {"a", "e", "i", "o", "u"}

    # check whether there are vowels in the string
    for x in y:
        for y in vowels:
            if x == y:
                counter.append(x)
    # convert the result to a set to eliminate duplicates
    result = set(counter)
    # return the length of the result
    return len(result)


myString = str(input("Enter a string: "))
print(Count_Vowels(myString))
