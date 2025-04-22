"""__________________________________FUNCTION_____________________________________________"""

"""A function is a block of code that does a specific task.
You can reuse it anytime by calling its name.

To organize your code
To avoid repeating code
To make your code clean and easy to read"""

# def sum(A,B):
#     sum = A+B
#     print(sum)
#     return(sum)

# sum(10,20)
# sum(100,20)
# sum(1087,20)
# sum(10,7620)

####################

# def square(A):
#     square= A*A
#     print(square)

# square(4)

####################

# def is_even(num):
#     if num%2==0:
#         print(True)
#     else:
#         print(False)

# is_even(21)

##################

# def L1(LL):
#     Mx = max(LL)
#     print(Mx)
# L1(LL=[1,2,3,4,5])

##############//////////////////

# balance = 1000

# def deposit():
#     global balance
#     amount = int(input("Enter amount to deposit: "))
#     balance += amount
#     print("Amount deposited successfully.")
#     print("Current Balance:", balance)

# def withdraw():
#     global balance
#     amount = int(input("Enter amount to withdraw: "))
#     if amount <= balance:
#         balance -= amount
#         print("Amount withdrawn successfully.")
#     else:
#         print("Insufficient balance.")
#     print("Current Balance:", balance)

# def main():
#     print("1. Deposit")
#     print("2. Withdraw")
#     choice = input("Enter your choice (1 or 2): ")
    
#     if choice == '1':
#         deposit()
#     elif choice == '2':
#         withdraw()
#     else:
#         print("Invalid choice.")

# main()


##################################


# def result(*sub):
#     print("marks", sub)
#     ave = sum(sub)/len(sub)
#     print("result", ave)

# result(10,20)
# result(13,23,12,21,34)
# result(576,7,4343,2)


######################

# def getdata(**data):
#     print(data)


# getdata(id=101, salary = 000, location= "pune", name = "Rupesh")

######################

L1 = [3, 4, 7, 2, 4, 6, 8, 5, 9, 3]

index = 0
row = 1

for i in range(1, 5): 

    for j in range(i):
        print(L1[index], end=" ")
        index += 1
    print()

max = []
max.append(row)
print(max)





