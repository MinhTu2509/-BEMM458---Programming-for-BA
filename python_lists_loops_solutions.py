# ======================================
# Python Solutions: Lists, Loops & Tuples
# ======================================
# Save this file as solutions2.py

# 1. Defining and Accessing Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])  # first
print(fruits[-1])  # last

# 2. Modifying Lists
fruits[0] = "mango"
fruits.append("orange")
fruits.insert(0, "kiwi")
del fruits[1]  # delete by index
popped_fruit = fruits.pop()  # removes last
fruits.remove("banana") if "banana" in fruits else None
print(fruits)

# 3. Organizing Lists
countries = ["Japan", "Canada", "Brazil"]
print(sorted(countries))  # temporary sort
print(countries)  # original list
countries.sort()  # permanent sort
print(countries)
countries.reverse()  # reverse order
print(countries)
print("Number of countries:", len(countries))

# 4. Avoiding Index Errors
try:
    print(countries[10])
except IndexError:
    print("That index doesn’t exist.")

# 5. Looping with for
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    print(animal)
print("Thanks for viewing the animal list!")

# 6. Numerical Lists
for num in range(1, 11):
    print(num)

even_numbers = list(range(2, 21, 2))
print(even_numbers)
print("Min:", min(even_numbers))
print("Max:", max(even_numbers))
print("Sum:", sum(even_numbers))

# 7. List Comprehensions
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# 8. Slicing Lists
foods = ["pizza", "burger", "pasta", "salad", "sushi", "taco", "steak"]
print("First three:", foods[:3])
print("Middle three:", foods[2:5])
print("Last three:", foods[-3:])

for food in foods[:3]:
    print("Slice item:", food)

copy_foods = foods[:]
copy_foods.append("ice cream")
print("Original:", foods)
print("Copy:", copy_foods)

# 9. Tuples
dimensions = (1920, 1080)
for value in dimensions:
    print(value)

# dimensions[0] = 1280  # would cause an error

# redefine the tuple
dimensions = (1280, 720)
print(dimensions)

# 10. Code Styling (PEP 8)
# Reviewed manually: indentation (4 spaces), line length < 79, blank lines.

# Final Challenge
movies = ["Inception", "Avatar", "Titanic", "Interstellar"]
print(sorted(movies))

for movie in movies:
    print(f"I really enjoyed watching {movie}!")

ratings = (5, 4, 5, 3)
avg_rating = sum(ratings) / len(ratings)
print(f"Average movie rating: {avg_rating}")
