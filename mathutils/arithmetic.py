def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
print(add(2, 3))  
print(subtract(5, 3))
print(multiply(2, 3))
print(divide(6, 2))
