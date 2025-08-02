from datetime import date, datetime

# DOB = "2000-01-01"  # Example date of birth
# DOB = datetime.strptime(DOB, "%Y-%m-%d").date()




# print("Current date:", current_date)
# print(age)

# d0 = date(DOB)
# d1 = date(2008, 9, 26)
# delta = d1 - d0
# print(delta.days)


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

age = calculate_age(DOB)
print("Age:", age)