# ---- GLOBAL VARIABLES ----
# These variables are available everywhere
default_number = 10

def add_numbers(x, y):
    """
    Function to add two numbers.
    x and y are LOCAL variables inside this function.
    """
    result = x + y  # Local variable
    return result

def multiply_with_default(x):
    """
    Function to multiply a number with a global variable.
    """
    # Access global variable default_number
    result = x * default_number
    return result

def change_default_number(new_value):
    """
    Function to change the global variable.
    We must use 'global' keyword if modifying it.
    """
    global default_number
    default_number = new_value

def main():
    """
    Main function to control the flow.
    """
    num1 = 5  # Local variable
    num2 = 3  # Local variable
    
    # Calling add_numbers function
    sum_result = add_numbers(num1, num2)
    print(f"Sum of {num1} and {num2} is {sum_result}")

    # Calling multiply_with_default function
    multiply_result = multiply_with_default(num1)
    print(f"{num1} multiplied with default_number ({default_number}) is {multiply_result}")

    # Changing the global default_number
    change_default_number(20)

    # Calling again after changing default_number
    multiply_result = multiply_with_default(num1)
    print(f"After changing, {num1} multiplied with new default_number ({default_number}) is {multiply_result}")

# Program entry point
if __name__ == "__main__":
    main()
