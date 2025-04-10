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
# print(L2)


#.Q.........

# 1. Find the sum of all elements in a list

L4 = [1,2,3,4,5]
# print(sum(L4))

# 2. find the maximum and minimum elements in a list

L5 = [1,2,3,4,5,10]
# print(f"The maxi num of the List is {max(L5)}")
# print(f"The Mini num of the List is {min(L5)}")

# 3. count how many times a specific element appear in a list
L6 = [1,2,3,4,5,10,1,2,3,1,1,1,1]
# print(L6.count(1))

# 4. print all the even in the list

L7= [1,2,3,4,5,10,12,14,18,200]
# print([i for i in L7 if i%2==0])

# 5. sort a list in ascending and decsing order without using a sort()

L8= [10000,2000,2,3,4,5,10,12,14,18,200]
for i in L8:
    print(i)
print(L8)





# 6. remove all duplicates from a list


# 7. reverse a list without using reverse() ?
# 8. Find the second largest number in a list?
# 9. split a list into two halves ?
# 10. Find all paris in a list that sum to a give number
