# import time
# currnt_date = time.time()
# print(f"current time: {time.ctime(currnt_date)}")
# exp = currnt_date+3600
# print(f"exp time: {time.ctime(exp)}")


# from datetime import datetime
# today = datetime.strftime(datetime.now(), format= '%Y-%M-%D')
# print("Today is ", today,type(today))


# #Q
import time
# # Hrs = float(input("Enter The Hrs you Reqired Parking: "))
# if Hrs <= 2:
#     charge = 3.50
# elif Hrs <= 4:
#     charge = 5.00
# elif Hrs <= 12:
#     charge = 10.00
# else:
#     print("Sorry, Max time is 12 Hrs.")
#     exit()
# tm= Hrs*3600

# currnt_date = time.time()

# print(f"Time now is : {time.ctime(currnt_date)}")
# exp = currnt_date+ tm
# print(f"exp  is: {time.ctime(exp)}")
# # charge = 
# print("\nCharge is {:.2f}".format(charge))

# import datetime
# Age = int(input("Enter your age: "))

# C = datetime.datetime.now()
# Now_Age = datetime.datetime(C.year)
# print(Now_Age)
# print("Age is: ", Now_Age - Age)



import random
Dice_1 = random.randint(1,6)
A = Dice_1
print("You rolled Dice 1 is", Dice_1)
Dice_2 = random.randint(1,6)
A = Dice_1
print("You rolled Dice 2 is", Dice_2)

if (Dice_1 != Dice_2):
    print(f"Your Score is {Dice_1+Dice_2} ")
else:
    print(f"You got a pair {Dice_1*Dice_1}")