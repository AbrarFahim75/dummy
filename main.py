print("Hello, world")

# Basic Operations and Concepts in Python

# 1. Variable Assignment
name = "Alice"  # String assignment
age = 30        # Integer assignment
height = 5.7     # Float assignment
is_student = True  # Boolean assignment

# 2. Printing to Console
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 3. Conditionals (If-Else Statements)
if age < 18:
    print(name + " is a minor.")
elif age >= 18 and age <= 60:
    print(name + " is an adult.")
else:
    print(name + " is a senior citizen.")

# 4. Basic Math Operations
sum_result = 10 + 5
diff_result = 10 - 5
prod_result = 10 * 5
quot_result = 10 / 5
mod_result = 10 % 3

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Quotient:", quot_result)
print("Remainder:", mod_result)

# 5. Loops: For Loop
print("\nFor Loop - Numbers from 1 to 5:")
for i in range(1, 6):  # range(1, 6) generates numbers from 1 to 5
    print(i)

# 6. Loops: While Loop
print("\nWhile Loop - Numbers from 1 to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment i

# 7. Functions
def greet(person_name):
    """Function that greets a person by name"""
    return f"Hello, {person_name}!"

greeting = greet(name)
print("\nGreeting:", greeting)

# 8. Lists (Mutable Sequence)
fruits = ["apple", "banana", "cherry"]
print("\nFruits List:", fruits)

# Add item to the list
fruits.append("orange")
print("After Adding Orange:", fruits)

# Remove item from the list
fruits.remove("banana")
print("After Removing Banana:", fruits)

# Access items in the list
print("First Fruit:", fruits[0])

# 9. Dictionaries (Key-Value Pairs)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print("\nPerson Dictionary:", person)

# Access dictionary values
print("Person's Name:", person["name"])
print("Person's Age:", person["age"])

# Add key-value pair
person["occupation"] = "Engineer"
print("After Adding Occupation:", person)

# 10. Exception Handling (Try-Except)
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("\nError: Cannot divide by zero!")
else:
    print("Division Successful")
finally:
    print("Execution complete.")

# 11. List Comprehensions
squares = [x ** 2 for x in range(1, 6)]
print("\nList of squares from 1 to 5:", squares)

# 12. String Manipulation
text = "  Python is awesome!  "
print("\nOriginal Text:", text)

# Remove leading/trailing spaces
trimmed_text = text.strip()
print("Trimmed Text:", trimmed_text)

# Convert to uppercase
uppercase_text = text.upper()
print("Uppercase Text:", uppercase_text)

# Replace a word in the string
replaced_text = text.replace("awesome", "fantastic")
print("Replaced Text:", replaced_text)

# 13. Lambda Function
# A short anonymous function that squares a number
square = lambda x: x ** 2
print("\nSquare of 5:", square(5))

# 14. Working with Sets
numbers_set = {1, 2, 3, 4, 5}
print("\nOriginal Set:", numbers_set)

# Adding an element to the set
numbers_set.add(6)
print("After Adding 6:", numbers_set)

# Removing an element from the set
numbers_set.remove(3)
print("After Removing 3:", numbers_set)

# 15. Working with Tuples (Immutable Sequence)
coordinates = (10, 20)
print("\nCoordinates Tuple:", coordinates)

# Accessing tuple elements
print("First Coordinate:", coordinates[0])

# 16. File Operations
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file!\n")
    file.write("Python is fun.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:\n", content)

