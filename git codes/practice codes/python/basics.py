name = "Paarth"
age = 18
height = 183
is_student = True

# print statements
print("hello, my name is {name}, i am {age} years old and {height} centimetres tall")

# taking input 
user_input = input("enter something")
print("the thing you input is stored in 'user_input' and gets printed as:", user_input)

# conditional statements 
if age >= 18 and not is_student:
    print("I am an adult worker.")
elif age >= 18 and is_student:
    print("I am an adult student.")
else:
    print("I am a minor.")

# lists and loops
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: I like {fruit}s.")


# functions
def greet(person_name, greeting="Namaste"):
    """Yeh function kisi ko namaste kehne ke liye hai."""
    return f"{greeting}, {person_name}!"

print(greet("Moksh"))
print(greet("Paarth", greeting="Hello"))

# dictionaties

person = {"name": "Moksh", "age": 25, "is_student": False}
print(f"{person['name']} {person['age']} saal ka hai.")

# sets
unique_numbers = {1, 2, 3, 4, 5, 1, 2}
print("Unique numbers:", unique_numbers)

# tuples
coordinates = (3, 4)
print("Coordinates:", coordinates)

# file handling
with open("example.txt", "w") as file:
    file.write("Yeh ek udaharan hai.\nDusra line.\n")

with open("example.txt", "r") as file:
    file_content = file.read()
    print("File Content:")
    print(file_content)

# error/exception handleing
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Error: Zero se divide karne mein dikkat aayi"
finally:
    print(f"Result: {result}")

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Namaste, main {self.name} hoon aur main {self.age} saal ka hoon."

person_instance = Person("Mopa", 32)
print(person_instance.introduce())

