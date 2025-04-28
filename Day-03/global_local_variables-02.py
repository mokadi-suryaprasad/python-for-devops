# ---- GLOBAL VARIABLES ----
# These variables are available everywhere
default_number = 10

# Local variables
num1 = 5
num2 = 3

# Adding two numbers
sum_result = num1 + num2
print(f"Sum of {num1} and {num2} is {sum_result}")

# Multiplying with default_number
multiply_result = num1 * default_number
print(f"{num1} multiplied with default_number ({default_number}) is {multiply_result}")

# Changing the global default_number manually
default_number = 20

# Multiplying again with updated default_number
multiply_result = num1 * default_number
print(f"After changing, {num1} multiplied with new default_number ({default_number}) is {multiply_result}")
