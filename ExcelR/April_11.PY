"""________________________________Tuple___________________________________"""

#()

"""Tuple is the immutable (No modification) data type in the python.
you can not change, update or modify the values in the typle.
it is the ordered data type. 
Tuple is the container that store all types of elements
i.g.. str, int, bool,float.(it is the hetrogeneous data type.)
it is allowed Duplicates.
"""

T1= (1,2,3,4)
# print(type(T1))
# T2 =(1)  #this is int
# T2 =(1,)  #, इज  complsory, when you want to represent the tuple'
# print(type(T2))

T3 = (1,2,3,4,5,5,5,5,5)
# T = T1.count(5)
# L1= list(T1) #convert the tuple into list

A = T3.index(2) #find the index value of the perticular element.(2)
# print(A)

T4 = ("Rupesh", 'Shub', 1,2,3,4)
# T4[0]= 'SS' #give Error, coz tuple immutable.
# print(T4[0: 2]) #Slicing
# print(T4)


"""___________Metods__________________________"""
T5 = ("R", "U", "P","S", 1,2,3)
# print(T5.count(1)) #REturn how many times, the 1 is appers in tuple.
# T6 = list(T5) #converting tuple to list
# print(type(T6))



"""________________________________Dictionary___________________________________"""

#Dict
"""Dict Identify by {}

    Dict is a set of KeyL Value pair.
    is is Unorded, (B.coz of No index value asosciated with it.)
    Key is Unique and Value Can be repeated. 
    it is Mutable."""

D1 ={
    #"Key" : "Value",
    "Name" : "Rupesh",
    "Age" : 25,
    "Gender" : "Male",
    "Age" : 25 #Key is Unique, Value can be repeated.
}
# print(type(D1))
# print(D1)

D2 = {} #empty Dict

# print(type(D2))

# print(D1.keys())  #Give the key only.

# print(D1.values()) #Give the value only.

Az = D2.update({"Marks": 33})
# print(D2)


D3 = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3
}

i = D3.popitem()  #
# print(i)
# print(D3)


