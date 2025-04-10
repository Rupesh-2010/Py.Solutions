A = 10
A = 20 

# print(A)

print(help('keywords'))
#Shorthand OP


print(1/66)
"""Q--- In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or less
have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
Write a program that reads the number of containers of each size from the user. 
I Your program should continue by computing and displaying the refund that will be received
for returning those containers. Format the output so that it includes a dollar sign and always
displays exactly two decimal places."""

Small_B = int(input("Enter the Small Num of Bottels: "))
Large_B = int(input("Enter the Large Num of Bottels: "))

SB = 0.10
LB = 0.25

A = Small_B*SB
B = Large_B*SB
C= A+B

Convert = C*86.68
print(f"Your Total Refund in Dollar is: {A+B} and {Convert:.2f}₹ in Indian Rupees")

