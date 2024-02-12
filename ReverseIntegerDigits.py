# write a program that takes in an integer as input and returns an integer with reversed digit ordering

def Reverse_number(value):
    # check whether the value < 0
    if value < 0:
        # the my_list stores numbers before reversal
        my_list = []
        # the reversed list stores numbers after reversal
        reversed_list = []
        x = str(value)
        for i in x:
            my_list.append(i)
        while my_list:
            res = my_list.pop()
            reversed_list.append(res)
        # the while loop continuously checks whether the first element of the reversed list is 0
        # if yes it removes the 0
        while reversed_list[0] == '0':
            reversed_list.remove('0')
        # the for loop here checks whether there is "-" in the reversed list
        # the "-" is always at the end of the reversed list
        # it's popped out, stored in variable k and added to the string version of reversed list
        for y in reversed_list:
            if y == "-":
                k = reversed_list.pop()
                reversed_num = k + "".join(reversed_list)
                return reversed_num
    # if value > 0 we reverse the number
    else:
        reversed_num = int(str(value)[::-1])
        return reversed_num


number = int(input("Enter a number: "))
print(Reverse_number(number))
