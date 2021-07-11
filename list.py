number_list = [1, 3, 5, 7]
animal_list = ['dog', 'cat', 'horse']

# Print all elements
print(number_list)
print(animal_list)

# Print specific element
print(animal_list[2])

# Iterate items
for animal in animal_list:
    print(animal)

# Sum items
print(sum(number_list))

# Min and Max values
print(min(number_list))
print(max(number_list))

# In list
animal = input('Enter an animal: ')
if animal in animal_list:
    print('{} is already on the list'.format(animal))
else:
    print('Adding {} to the list'.format(animal))
    animal_list.append(animal)

print(animal_list)

# Removing from list
# Remove last
animal_list.pop()
# Remove a specific item from the list
animal_list.remove('dog')
# List the remaining animals on the list
print(animal_list)
