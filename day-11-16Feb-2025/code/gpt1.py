import random

def roll_dice():
    dice_faces = [
        "+-------+\n|       |\n|   *   |\n|       |\n+-------+",  # 1
        "+-------+\n| *     |\n|       |\n|     * |\n+-------+",  # 2
        "+-------+\n| *     |\n|   *   |\n|     * |\n+-------+",  # 3
        "+-------+\n| *   * |\n|       |\n| *   * |\n+-------+",  # 4
        "+-------+\n| *   * |\n|   *   |\n| *   * |\n+-------+",  # 5
        "+-------+\n| *   * |\n| *   * |\n| *   * |\n+-------+"   # 6
    ]
    roll = random.randint(0, 5)
    print(dice_faces[roll])

def pick_payer(friends):
    print("\nShaking the basket... 🎲")
    roll_dice()
    chosen_one = random.choice(friends)
    return chosen_one

def main():
    print("Welcome to the Dinner Bill Game! 🍽️")
    friends = []

    print("\nEnter the names of five friends:")
    i = 1
    while len(friends) < 5:
        name = input(f"Enter name {i}: ").strip()
        if name == "":
            print("Name cannot be empty. Try again.")
        elif name in friends:
            print("This name is already added. Try a different name.")
        else:
            friends.append(name)
            i += 1

    print("\nAll names are in the basket:")
    for friend in friends:
        print(f"- {friend}")

    input("\nPress Enter to draw a name from the basket...")
    payer = pick_payer(friends)

    print(f"\n🎉 The unlucky friend who will pay the bill is: {payer}! 💸")

if __name__ == "__main__":
    main()
