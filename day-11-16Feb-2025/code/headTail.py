import random

def flip_coin():
    return random.choice(["Head", "Tail"])

def get_coin_face(result):
    coin_faces = {
        "Head": """
        ***********
        *         *
        *  HEAD   *
        *   O     *
        *         *
        ***********
        """,
        "Tail": """
        ***********
        *         *
        *  TAIL   *
        *   X     *
        *         *
        ***********
        """
    }
    return coin_faces[result]

def play_head_tail_game():
    while True:
        input("Press Enter to flip the coin... (or type 'exit' to quit)")
        result = flip_coin()
        print(get_coin_face(result))
        
        choice = input("Do you want to flip again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_head_tail_game()
