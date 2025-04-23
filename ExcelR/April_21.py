# def msg():
#     print("Good Morning")

# msg()

######################

# a =lambda name:print("good Morning", name)
# a("Rupesh")

#############

# a = lambda x:print(x*x)
# a(5)

#############

# larger = lambda a,b : a if a>b else b
# print(larger(10,20))

#############

"""__________________________________MAP____________________________________"""

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)

"""
map hold the 2 things.  1. function 2. sqeuenece."""


"""__________________________________Filter____________________________________"""

# numbers = [1, 2, 3, 4, 5,111,23,12,2324,53,54,34,67,89]   
#even numbr
# l1 = list(filter(lambda x: (x%2==0),numbers))
# print(l1)


"""_________________________________Scope____________________________________

1. Local Scope ----> when the scope of the veriable is only inside the block

2. global scope ----> can be access inside and the outside of the function.

"""

#############Local scope

# def M1():
#     A = "HEllo"
#     print(A)
# M1()

# print(M1)

#################Glober Scope

# def M1():
#     A = "HEllo"
#     print(A)
#     print(A)
# M1()

# print(M1)

"""_________________________________recurtion____________________________________

it is a process of definding somting in terms of itself.

"""

def factorial(x):
    if x ==1:
        return 1
    else:
        return(x*factorial(x-1))
    
num = int(input("Enter Num: "))
print(f"The facorial of num is {num} is {factorial(num)}")




