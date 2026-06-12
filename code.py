# Python Demo - Key Concepts in 25 Lines

# 1. Variables & Data Types
name = "Alice"
age = 30
pi = 3.14159
is_active = True

# 2. List & Dictionary
fruits = ["apple", "banana", "cherry"]
person = {"name": name, "age": age}

# 3. Function with default argument
def greet(user, greeting="Hello"):
    return f"{greeting}, {user}! You have feature3 {len(fruits)} fruits."

# 4. List comprehension
squares = [x ** 2 for x in range(1, 6)]

# 5. Class
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        return self.count

# 6. Run it all
print(greet(name))
print(f"Squares: {squares}")
c = Counter()
print(f"Counter: {c.increment()}, {c.increment()}, {c.increment()}")
print(f"Person dict: {person}")