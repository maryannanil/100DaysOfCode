print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
side=input("Enter the side left or right?")
if side == "left":
    print("You have reached the river: Swim or Wait")
    next=input("Enter Swim or Wait?")
    if next == "swim":
        print("You have reached the wall. Choose the door color: RED, BLUE, or YELLOW")
        color=input("Enter the color of the door?")
        if color == "red" or "Red":
            print("You have found the treasure. You Win!")  
        elif color == "blue" :
            print("You have been eaten by beasts. Game Over!")
        elif color == "yellow":
            print("You have been attacked!")
    else:
        print("You have been attacked by a ghost. Game Over!")
else:
    print("You have fallen into a hole. Game Over!")

