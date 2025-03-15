import random

dice = [1, 2, 3, 4, 5, 6]

run = True
while run:
    user_input = input("Press 'enter' to Roll the Dice: ")
    dice_rolled = dice[random.randint(1,5)]
    
    if dice_rolled == 6:
        print("Congrats!! You got a 6")
    else:
        print(f"Oops, You got a {dice_rolled}")
    
    exit = input("Write 'esc' to terminate the program or Press 'enter' to continue: ")
    if exit.lower() == "esc":
        run = False

print("See you next time, Bye!!")
