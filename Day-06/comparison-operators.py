def greater_than(a, b):
    return a > b

def less_than(a, b):
    return a < b

def greater_than_or_equal(a, b):
    return a >= b

def less_than_or_equal(a, b):
    return a <= b

def equal(a, b):
    return a == b

def not_equal(a, b):
    return a != b


greater_than_result = greater_than(5, 3)
less_than_result = less_than(5, 3)  
greater_than_or_equal_result = greater_than_or_equal(5, 5)
less_than_or_equal_result = less_than_or_equal(5, 3)
equal_result = equal(5, 5)
not_equal_result = not_equal(5, 3)

# Print results
print("Greater than:", greater_than_result)  # True
print("Less than:", less_than_result)  # False
print("Greater than or equal:", greater_than_or_equal_result)  # True
print("Less than or equal:", less_than_or_equal_result)  # False
print("Equal:", equal_result)  # True
print("Not equal:", not_equal_result)  # True