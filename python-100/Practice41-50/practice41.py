animals = ["dog", "cat", "rabbit", "cow", "goat", "sheep", "mouse"]
new_animals = []

for animal in animals:
    if len(animal) == 3:
        new_animals.append(animal)

print(new_animals)