"""________________________________Tuple___________________________________"""

#()

"""Tuple is the immutable (No modification) data type in the python.
you can not change, update or modify the values in the typle.
it is the ordered data type. 
Tuple is the container that store all types of elements
i.g.. str, int, bool,float.(it is the hetrogeneous data type.)
it is allowed Duplicates.
"""

# T1= (1,2,3,4)
# print(T1, type(T1))






"""_________________________________#Set {}_________________________________"""


"""the set is collection og Non-Repetitve elements.
it is identitfy by {}  
is store only the Unique value. and NO Duplicates is allowed.
Set is he unorded.it means we can NOT performs the idexing and slicing.
Set is the inmutable and mutebale also.
it is hetrogeneous Data types, (We can store multiple data type.) """

# print(f"this is set {S1}")
# print(type(S1))
S1 = {1,9, 2,3,4,5}
S2 = {5,6,7,1,8,9,10}

# print(S1.union(S2))
# print(S2.difference(S1))
# print(S1.intersection(S2))



"""On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it,
multiple key presses are needed for most letters. Pressing the number once generates
the first letter on the key. Pressing the number 2, 3, 4 or 5 times generates the second,
third, fourth or fifth character listed for that key.

Key		Symbols
1		.,?!:
2		ABC
3		DEF
4		GHI
5		JKL
6		MNO
7		PQRS
8		TUV
9		WXYZ
0		space

Write a program that displays the key presses that must be made to enter a text message
read from the user. Construct a dictionary that maps from each letter or symbol to the
key presses. Then use the dictionary to generate and display the presses for the user's message.
For example, if the user enters Hello, World! then your program should
output 4433555555666110966677755531111. Ensure that your program handles both
uppercase and lowercase letters. Ignore any characters that aren't listed in the
table above such as semicolons and brackets."""

K_Ph = {
    "1" : ".",
    "11" : ",",
    "111" : "?",
    "1111" : "!",
    "11111" : ":",
    "2" : "A",
    "22" : "B",
    "222" : "C",
    "3" :"D",
    "33" :"E",
    "333" :"F",
    "4" : "G",
    "44" : "H",
    "444" : "I",
    "5" : "J",
    "55" : "K",
    "555" : "L",
    "6" : "M",
    "66" : "N",
    "666" : "O",
    "7" : "P",
    "77" : "Q",
    "777" : "R",
    "7777" : "S",
    "8" : "T",
    "88" : "U",
    "888" : "V",
    "9" : "W",
    "99" : "X",
    "999" : "Y",
    "9999" : "Z",
    "0" : " "
}

msg = input("Enter Your msg: ").upper()
result = ""

for char in msg:
    found = False
    for key, value in K_Ph.items():
        if value == char:
            result += key
            found = True
            break
    if not found:
        pass
print("Key presses:", result)








