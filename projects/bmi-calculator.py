height=float(input("Enter your height in meter : "))
weight=float(input("Enter your weight in kg : "))

bmi=round(weight/height**2)


if bmi <= 18:
    print(f"your bmi is {bmi} you are a under weight")
elif bmi <= 25:
    print(f"your bmi is {bmi} you are a normal weight")
elif bmi <= 30:
    print(f"your bmi is {bmi} you are a over weight")
elif bmi <= 35:
    print(f"your bmi is {bmi} you are a obese ")
else:
    print(f"your bmi is {bmi} you are a clinically obese ")
