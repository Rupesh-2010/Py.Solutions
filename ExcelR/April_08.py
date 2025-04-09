#Premitive and Non-P data types
'''
1. Premitive data type--> return the value.
    i. none Value
    ii. number
        1.int
        2. float
        3. Complex 
        4. boolean

2. Non-Prem DT--> Return the Addres.
    1. List
    2. tuple
    3. String
    4. Set
       i. Frozen Set
    5. Dict
    6. range
    
'''

#List []
""" List is the container that store all types of elements, i.g.. str, int, bool,float.(it is the hetrogeneous data type.)
a list is a Flexibale, muteable it means it can be changebele and accept the duplicate values.
you can modify the list, by append(), remove(), and sort() or pop()
duplicates are not allowed. 
- Mutable
- it is a ordered collection o data
- Non-Premitative (refrence by addres. (index))

"""

# L = [1,2,3,"Rupesh", 4, "VDX"]
# print(L[3])
# print(L[-2])


#Nested List.
L = [1,2,3,"Rupesh", 4, "VDX",[100,200,300],[1000,2000,3000]]
# print(L[1]) # Output: 2
# print(L[6][0])  # Output: 100
# print(L[7][2])  # Output: 3000

#Slicing
# L1 = [10,20,30,40,50,60,70]

# print(L1[0:5])
# print(L1[ :2])


#Methods.

L2 =[1,2,3,4,1,1]
L3 = [10,20,30,40]
# A= L2.append("Rup")  #add to the end of the list
# B = L2.extend(L3) 
# L2.insert(0,11111) #first is Index number and secod is th New element that iwant to change at the index num 1
# C= L2.remove(1) #You Hve to enter the specicfic "Num",Not a Index Value.
# D = L2.clear() #remove the all elemtns form the list
# E = L2.count(1) #counts the how many times, the 1 is appper, but print the E to knows the count of 1

print(L2)

