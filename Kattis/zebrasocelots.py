num_animals = int(input())
animal_order = []
counter = 0
for i in range(num_animals):
    animal = input()
    animal_order.insert(0, animal)
for i in range(0, len(animal_order)):
    if animal_order[i] == "O":
        counter += 2 ** i
print(counter)
