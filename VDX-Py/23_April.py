# L1 = [2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, L1))
# print(squared)
# L1 = (2, 3, 4, 5)
# squared = tuple(map(lambda x: x ** 2, L1))

# print(squared)


#######################

# def test():
#     print("hi, eating.")
#     def eating():
#         print("hi, i am eating")
#     eating()
# test()

################

def addition(a,b):
    return a+b
def subtract(a,b):
    return a+b

def add(a):
    return(a*a)

def test(func1, func2,a,b):
    if a>0 and b>0:
        print("positive")
        c = func1(a,b)
        print("result",c)
    else:
        c = func2(a,b)
        print("result",c)
test(addition,subtract, -12, -54)
l1=[4,5]
c= list(map(add,l1))
print("result pf map",c)








