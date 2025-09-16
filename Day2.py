# # print(int("124"))

# # print(int("124")+int("567"))

# # print(int("No. of letters in your name is" + str (len(input("what us your name?")))))

# # name=input("what is your name?")
# # length=len(name)
# # # print("No. of letters in your name is " + str(length)pri
# # print(6 /3)
# # print("Welcome Maryann" + " " + str(777))

# print(3/3*3-3+3)

# print(round(84/2.65*2))

# print(round(84/2.632, 2))

# score=0
# #user scores a Point
# score+=1
# print(score)

# print("Your score is " + str(score))

# height=1.8
# isWinning=True  
# print (f" your score is {score}")

# Tip calculatoer

print("Welcome to the tip calculator")
bill=float(input("what is the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12 or 15? "))
people=int(input("How many people to split the bill? "))
tot_bill=round((bill + bill * tip / 100) / people,2)
print(tot_bill)