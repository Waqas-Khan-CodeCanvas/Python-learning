import random

def roll_dice():
    return random.randint(1, 6)

def get_dice_face(number):
    dice_faces = {
        1: """
        -------
        |     |
        |  O  |
        |     |
        -------
        """,
        2: """
        -------
        | O   |
        |     |
        |   O |
        -------
        """,
        3: """
        -------
        | O   |
        |  O  |
        |   O |
        -------
        """,
        4: """
        -------
        | O O |
        |     |
        | O O |
        -------
        """,
        5: """
        -------
        | O O |
        |  O  |
        | O O |
        -------
        """,
        6: """
        -------
        | O O |
        | O O |
        | O O |
        -------
        """
    }
    return dice_faces[number]

def play_dice_game():
    while True:
        input("Press Enter to roll the dice... (or type 'exit' to quit)")
        dice_value = roll_dice()
        print(get_dice_face(dice_value))
        
        choice = input("Do you want to roll again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_dice_game()
