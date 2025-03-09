import random
shaps=[
     """
        ***********
        *         *
        *  HEAD   *
        *   O     *
        *         *
        ***********
        """,
        """
        ***********
        *         *
        *  TAIL   *
        *   X     *
        *         *
        ***********
        """
]


print("Welcome to Head Tail Game")
while True:
    get_face=random.randint(0,1)
    print(shaps[get_face])
    user_choice=input("Do you want to play again (y/n)")
    if user_choice.lower().strip()=="n":
        print("Thank you")
        exit()
        