"""_____________________________Patterns__________________________________"""

# n = 1
# for i in range(1, 5):
#     for j in range(n + i - 1, n - 1, -1):
#         print(j, end=" ")
#     print()
#     n += i



"""_____________________________List__________________________________"""

# L1 = []

# while True:
#     Name = input("Enter Name: ")
#     if Name.lower() == "end":
#         break
#     L1.append(Name)
# print(f"The List is {L1} ")

# half = len(L1)//2
# print(f"half is {L1[ :half]}")



"""________________________________________-"""

# L2 = []
# while True:
#     Name = input("Enter Name: ")
#     if Name == "":
#         break
#     L2.append(Name)
# print(f"The List is {L2} ")

# UL =[]
# for i in L2:
#     if i not in UL:
#         UL.append(i)
#     print(f"Unique List is {UL} ")

"""________________________________________-------"""

"""Write a program that reads numbers from the user until a blank line is entered. 
Your program should display the average of all of the values entered by the user.
Then the program should display all of the below average values, followed by all of
the average values (if any), followed by all of the above average values.
An appropriate label should be displayed before each list of values."""


# L3 = []

# while True:
#     Num = input("Enter Num: ")
#     if Num == "":
#         break
#     L3.append(float(Num))

# print(f"The List is {L3}")


# avg = sum(L3) / len(L3)
# print(f"Average: {avg}")

# below_avg = []
# equal_avg = []
# above_avg = []

# for i in L3:
#     if i < avg:
#         below_avg.append(i)
#     elif i == avg:
#         equal_avg.append(i)
#     else:
#         above_avg.append(i)

# print("Below average values:", below_avg)
# print("Average values:", equal_avg)
# print("Above average values:", above_avg)


"""________________________________________-------"""


"""Create a program that reads integers from the user until a blank line is entered.
Once all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers.
Within each group the numbers should be displayed in the same order that they were entered.
by the user. For example, if the user enters the values 3, -4, 1, 0, 1, 0, and -2
then your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line."""


L4 = []

while True:
    Num = input("Enter Num: ")
    if Num == "":
        break
    Num = int(Num)
    L4.append(Num)
print(f"The List is {L4} ")

Negative_Num =[]
Zero_Num =[]
Positive_Num =[]

for i in L4:
    if (i<0):
        Negative_Num.append(i)
    elif (i==0):
        Zero_Num.append(i)
    else:
        Positive_Num.append(i)

print(f"The Negative Num List is: {Negative_Num}")
print(f"The Zero Num List is: {Zero_Num}")
print(f"The Positive Num List is: {Positive_Num}")

"""__________________________________________________"""
