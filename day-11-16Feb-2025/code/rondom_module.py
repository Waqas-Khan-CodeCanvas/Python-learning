import random
# random.random()	Random float in [0.0, 1.0]
# random.randint(a, b)	Random integer between a and b
# random.choice(seq)	Selects a random element from seq
# random.shuffle(seq)	Shuffles seq in-place
# random.sample(seq, k)	Selects k unique elements


# print(random.randint(1, 10))
# print(random.choice(['apple', 'banana', 'cherry']))
# sequence = [1, 2, 3, 4, 5]
# random.shuffle(sequence)
# print(sequence)
# print(random.sample(sequence, 3))
names=[1,2,3,4,5,6,7]
print(random.random())
print(random.choice(names))
print(random.randint(1,3))
print(random.randrange(1,3))
print(random.uniform(1,2))
print(random.sample(names,3))



# print(random.randint(1, 100))

# The error occurs because the file is named `random.py`, which shadows the built-in `random` module.
# Rename the file to something else, for example, `random_example.py`, and then run the code again.
