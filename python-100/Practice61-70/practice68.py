animals = {
    "개": "dog",
    "고양이": "cat",
    "소": "cow",
    "양": "sheep"
}

keys = ""
for key in animals.keys():
    keys += f'{key} '

print(keys)