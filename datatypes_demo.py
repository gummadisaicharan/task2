# ---------------------------------------------
# Task 2: Variables, Data Types & Type Conversion
# Python Developer Internship
# ---------------------------------------------

# 1. Declaring variables of different data types
integer_var = 10              # int
float_var = 25.5              # float
string_var = "Python"         # string
boolean_var = True            # boolean

# 2. Printing values and their data types
print("Integer Value:", integer_var, "| Type:", type(integer_var))
print("Float Value:", float_var, "| Type:", type(float_var))
print("String Value:", string_var, "| Type:", type(string_var))
print("Boolean Value:", boolean_var, "| Type:", type(boolean_var))

print("\n-------------------------------\n")

# 3. Arithmetic operations using numeric variables
addition = integer_var + float_var
subtraction = float_var - integer_var
multiplication = integer_var * 2
division = float_var / integer_var

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

print("\n-------------------------------\n")

# 4. Type Conversion (Type Casting)
user_input = input("Enter a number: ")

try:
    int_value = int(user_input)      # Convert string to integer
    float_value = float(user_input)  # Convert string to float

    print("Integer Conversion:", int_value)
    print("Float Conversion:", float_value)

except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("\n-------------------------------\n")

# 5. String and Number Concatenation
age = 21

# Correct way using str() conversion
print("My age is " + str(age))

# Correct way using f-string
print(f"My age is {age}")

print("\n-------------------------------\n")

# 6. Demonstrating Dynamic Typing
dynamic_var = 100
print("Value:", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = "Now I am a string"
print("Value:", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = 45.75
print("Value:", dynamic_var, "| Type:", type(dynamic_var))
