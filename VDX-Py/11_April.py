"""_____________________________Loop__________________________________"""

"""A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge.
Children between 3 and 12 years of age cost $14.00.
Seniors aged 65 years and over cost $18.00. Admission for all other guests is $23.00.

Create a program that begins by reading the ages of all of the guests in a group from
the user, with one age entered on each line. The user will enter a blank line to indicate
that there are no more guests in the group. Then your program should display the admission
cost for the group with an appropriate message. The cost should be displayed using two
decimal places."""

# total_cost = 0.0

# while True:
#     age_input = input("Enter Your Age: ")
#     if age_input == "":
#         break
#     age = int(age_input)
#     if age <= 2:
#         price = 0.00
#     elif 3 <= age <= 12:
#         price = 14.00
#     elif age >= 65:
#         price = 18.00
#     else:
#         price = 23.00

#     total_cost += price

# print(f"Total admission cost for the group: ${total_cost:.2f}")


"""Write a program to allow the user to enter a number of 5-character product codes,
beginning with the letters "AB" or "AS" followed by 3 numeric characters.
Count and print the total number of product codes starting with "AB" and
the total number of product codes ending in "00".
Test your program by entering product codes AS123, AS101, AB111, AB345, CD222, AB200."""

# AB_count = 00
# AC_count = 00

# while True:

#     Prod_Name = input("Enter Your Prod Name: ")
#     if Prod_Name == "":
#         break
#     if Prod_Name[0:2] == "AB" and len(Prod_Name) == 5 and Prod_Name[3:].isdigit():
#         AB_count += 1
#     elif Prod_Name[0:2] == "AS" and len(Prod_Name) == 5 and Prod_Name[3:].isdigit():
#             AC_count += 1
#     else:
#         print("Invalid Product Code")

# print(f"The Total Count of AB Prod is {AB_count}")
# print(f"The Total Count of AC Prod is {AC_count}")



"""One of the first known examples of encryption was used by Julius Caesar.
Caesar needed to provide written instructions to his generals,
but he didn't want his enemies
to learn his plans if the message slipped into their hands.
As result, he developed what later became known as the Caesar Cipher.
The idea behind this cipher is simple
(and as a result, it provides no protection against modern code breaking techniques).
Each letter in the original message is shifted by 3 places.
As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.
The last three letters in the alphabet are wrapped around to the beginning:
X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified
by the cipher.

Write a program that implements a Caesar cipher.
Allow the user to supply the message and the shift amount, and
then display the shifted message. Ensure that your program encodes both uppercase and lowercase
letters. Your program should also support negative shift values so that it can be used
both to encode messages and decode messages."""


# Msg = input("Enter Your Msg: ")
# Shift = int(input("Enter The Shifting Msg: "))
# New_Msg = ""
# for i in Msg:
#     print("Your msg is", Msg)
#     New_Msg = chr(ord(Msg) + Shift)
#     for i in Msg:
#         print(New_Msg)





