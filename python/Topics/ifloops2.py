# A simple if else program with or as it's condition

# A simple input data type checker

# A variable for the input data type
inp1 = input("Enter the datatype here: [int/float/str] ")
if inp1 == 'int':
    print("A number entered here will be checked for even or odd (int).")
    # A variable to ask for your number
    num1 = int(input("Enter your number here: "))
    if (num1 % 2) == 0:
        print("Yep the number is even because %d is divisible by 2 with it's quotient being " + str(num1/2) %num1)
    # Else if the number is odd
    else:
        print("The number %d is odd." %num1)


# Now for the same variable but in float condition
elif inp1 == 'float':
    print("Your data type is float and idk what to do tbh.\n end of thinking capacity")
    print("Jk... I will think of something else.. I think...")
    num2 = float(input("Enter a float number here: "))
    print("Your int to float conversion results in " + str(int(num2)))


#else if the input is string 
elif inp1 == 'str':
    str1 = str(input("enter the string here or something idk..: "))
    print("Will convert everything to upper case now\n")
    print(str1.upper())


# Else if nothing matches just end the code and tsay input not found
else:
    print("Please enter a valid input")



# Now to think of something to put in this or condition

# just what can be in or. It needs to satisfy either of the one conditions
# why can't I think lmao

# Since I am unable to think I will do something half assed i think

y = input("Do you like onee sans? ") # ah yes the can't think of something option

# Let's satisfy two responses in one using or
if y == 'y' or y == 'Y' or y == 'yes' or y == 'Yes':
    inp2 = input("Ara~ Do you want to be with one? ")
    if y == 'y' or y == 'Y' or y == 'yes' or y == 'Yes':
        on = input("Can you name one Onee san? ")
        print("Aahh %s is a good choice UwU" %on)

else:
    print("Okay program exiting right now")