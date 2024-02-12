# Write a program that takes an integer as input and returns true if the input is a power of two

def Power_Of_Two(x):
    y = x
    counter = 0
    # 1 is a power of 2
    if x == 1:
        return True

    # this statement eliminates negative numbers.Negative numbers cannot be considered powers of 2
    # it also eliminates a 0
    elif x <= 0:
        return False

    # now separate even numbers from odd numbers using modulus in an elif...else statement
    elif x % 2 == 0:
        counter += 1
        # store the result of dividing x by 2 in variable result
        res = x / 2
        while res > 0:
            if res == 1:
                return True

            elif res % 2 == 0:
                res /= 2
                counter += 1
                if 2 ** counter == y:
                    return True

            else:
                return False


    # this statement eliminates odd numbers starting from 2 going onwards
    else:
        return False


number = int(input("Enter a number: "))
is_power = Power_Of_Two(number)
print(is_power)
