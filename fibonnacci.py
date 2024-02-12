# Write a program to generate fibonacci sequence up to 100

no_of_terms = 100
# initialize the first two terms of the sequence
x = 0
y = 1
counter = 0

# check if the number of terms entered is greater than 0
if no_of_terms <= 0:
    print("Enter a valid number of terms: ")

# if the input is 1 then return x
elif no_of_terms == 1:
    print("Fibonacci sequence upto: ", no_of_terms, ":")
    print(x)
# otherwise generate the fibonnacci sequence
else:
    print("Fibonacci sequence upto: ")
    while counter < no_of_terms:
        print(x)
        num = x + y
        x = y
        y = num
        counter += 
