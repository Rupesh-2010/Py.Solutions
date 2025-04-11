"""-----------------------------------DateTime Module.------------------------------------------"""

# import datetime as dt

# Today_date = dt.date.today() #prints todays time
# print(Today_date)
# print(f"year: {Today_date.year}")  ##prnts todays Year only
# print(f"Month: {Today_date.month}")  ##prnts todays Month only
# print(f"day: {Today_date.day}")  # #prnts todays Day only
# Nw = dt.datetime.now()  #You get current date and time
# print(Nw)

"""-----------------------------------------------------------------------------"""

"""Q. Get today’s date using the datetime module. """

import datetime as dt
# Today = dt.date.today()
# print(Today)

"""Q. Print the current year, month, and day separately."""

# Today= dt.date.today()

# print(f"Current Year is: {Today.year}")
# print(f"Current Month is: {Today.month}")
# print(f"Current day is: {Today.day}")

"""Add 7 days to today's date and print the new date."""

# Today = dt.date.today()
# A = Today + dt.timedelta(days=7)
# print(A)

"""Subtract 3 days from today and print that date."""
# Today = dt.date.today()
# B = Today - dt.timedelta(days= -3)
# print(B)

# import time
# currnt_date = time.time()
# print(f"current time: {time.ctime(currnt_date)}")
# exp = currnt_date+3600
# print(f"exp time: {time.ctime(exp)}")


# from datetime import datetime
# today = datetime.strftime(datetime.now(), format= '%Y-%M-%D')
# print("Today is ", today,type(today))


"""Q.... Write a program to calculate car park charges.
# Up to 2 hours costs £3.50, up to 4 hours £5.00, up to 12 hours £10.00. 
# The driver enters the number of hours they require and the machine
# prints the current time, expiry time and charge. For example:"""
# Time now:
# Wed Mar 8 15:47:46 2017
# Expires:
# Thu Mar 9 03:47:46 2017
# Charge 10.00
# Tip: Use the Python library function time by writing import time at the top of the program. The time in seconds since January 1st 1970 is given by


import time
# # Hrs = float(input("Enter The Hrs you Reqired Parking: "))
# if Hrs <= 2:
#     charge = 3.50
# elif Hrs <= 4:
#     charge = 5.00
# elif Hrs <= 12:
#     charge = 10.00
# else:
#     print("Sorry, Max time is 12 Hrs.")
#     exit()
# tm= Hrs*3600

# currnt_date = time.time()

# print(f"Time now is : {time.ctime(currnt_date)}")
# exp = currnt_date+ tm
# print(f"exp  is: {time.ctime(exp)}")
# # charge = 
# print("\nCharge is {:.2f}".format(charge))


"""Q.. Age Ques"""

# import datetime
# Birth_Year = int(input("Enter Your Birth_Year: "))

# Currnt_Year = datetime.datetime.now().year
# Age = Currnt_Year-Birth_Year
# print(f"Your Current age is {Age}")


# _____________________________Random Module__________________________________

"""Q... Write a program to simulate the throw of two dice (each between 1 and 6).
Print the numbers representing the two throws.If the numbers on the two dice are not equal,
the player's score is the sum of the numbers thrown. Print the score.
If the numbers on the two dice are equal, the player scores twice the
sum of the number thrown. Print "You threw a double", and the score."""

# import random
# Dice_1 = random.randint(1,6)
# A = Dice_1
# print("You rolled Dice 1 is", Dice_1)
# Dice_2 = random.randint(1,6)
# A = Dice_1
# print("You rolled Dice 2 is", Dice_2)

# if (Dice_1 != Dice_2):
#     print(f"Your Score is {Dice_1+Dice_2} ")
# else:
#     print(f"You got a pair {Dice_1*Dice_1}")

"""_______________________________________________________________"""

"""Random Module example.. 
Random()
randint()
choice()
randrange() """

"""it used to print some random number in programm"""

import random as rd

# print(rd.random()) #Returns a random float between 0 and 1.

# print(rd.randint(1,12))  #Returns a random integer between a and b (inclusive).

L1= ["Rupesh", "R", "U", "P", "Desai", "D", "P"]
# print(L1)
# print(rd.choice(L1))  #Returns a random element from the non-empty sequence seq.

# print(rd.randrange(1,10, 5))

"""___________"""

# print(rd.randint(10, 20))

# A = rd.sample(["Rupesh", "R", "U", "P", "Desai", "D", "P"],2)
# print(A)

B = rd.choices(["Rupesh", "R", "U", "P", "Desai",],k=2)
# print(B)


# _____________________________ASCII Value__________________________________


# A =input("Enter Char: ")
# print(ord(A))

# AS = int(input("Enter: ")

# B =chr(AS)
# print(B)


