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

L2 = []

while True:
    Name = input("Enter Name: ")
    if Name == "":
        break
    L2.append(Name)
print(f"The List is {L2} ")


UL =[]
for i in L2:
    if i not in UL:
        UL.append(i)
    print(f"Unique List is {UL} ")

