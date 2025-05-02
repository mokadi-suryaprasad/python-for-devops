def sum(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def quotient(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 // num2  

sum_result = sum(10, 5)
difference_result = difference(10, 5)   
product_result = product(10, 5)
quotient_result = quotient(10, 5)
print("Sum:", sum_result)   
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
# Output: