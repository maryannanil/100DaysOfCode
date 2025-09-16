#Randomisation
import random
import my_module

# random_integer=random.randint(1, 10) #random integer between 1 and 10
# print(random_integer)

# random_nuber_0_to_1 = random.random() * 10

# print(random_nuber_0_to_1)

# random_head_tails= random.randint(0,1)
# if random_head_tails == 1:
#     print("HEADS")
# else:
#     print("TAILS")

# states_of_india=["Maharashtra", "Gujrat", "Kerala"]
# cities=["Mumbai", "Pune", "Nagpur", "Ahmedabad", "Surat", "Kochi", "Trivandrum"]
# states=len(states_of_india)

# what=[states_of_india, cities] 
# print(what[0])
# print(what[1])
# print(what [0][1])

print("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scissors")
choose=int(input())
choice= ["Rock", "Paper", "Scissor"]

computer_choice=random.randint(0,2)
print("You chose: ", choice[choose])
print("Computer chose: ", choice[computer_choice])

if choose==0 and computer_choice==2:
    print("You win")
elif choose==2 and computer_choice==1:    
    print("You win")
elif choose==1 and computer_choice==0:
    print("You win")
elif choose==computer_choice:
    print("It's a draw")
else:
    print("You lose")



# friends=["Rahul", "Rohit", "Rajesh", "Ramesh", "Raj"]
# print(random.choice(friends))

