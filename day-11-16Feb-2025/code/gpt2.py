import random
import time

def display_dice(face):
    dice_faces = {
        1: """
         -------
        |       |
        |   *   |
        |       |
         -------
        """,
        2: """
         -------
        | *     |
        |       |
        |     * |
         -------
        """,
        3: """
         -------
        | *     |
        |   *   |
        |     * |
         -------
        """,
        4: """
         -------
        | *   * |
        |       |
        | *   * |
         -------
        """,
        5: """
         -------
        | *   * |
        |   *   |
        | *   * |
         -------
        """,
        6: """
         -------
        | * * * |
        |       |
        | * * * |
         -------
        """
    }
    print(dice_faces[face])

def get_friends():
    friends = []
    print("\nEnter the names of 5 friends going to dinner:")
    for i in range(5):
        name = input(f"Enter name {i + 1}: ").strip()
        friends.append(name)
    return friends

def roll_dice_animation():
    print("\nShaking the basket...")
    for _ in range(5):
        face = random.randint(1, 6)
        display_dice(face)
        time.sleep(0.5)

def pick_payer(friends):
    return random.choice(friends)

def play_game():
    print("Welcome to the 'Who Pays the Bill?' Game!\n")
    friends = get_friends()

    while True:
        roll_dice_animation()

        payer = pick_payer(friends)
        print(f"\n🎉 The lucky person who will pay the bill is: {payer} 🎉")

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nThanks for playing! Enjoy your dinner! 🍽️")
            break

play_game()
