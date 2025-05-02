def logicaland(a, b):
    # Logical AND: Both must be True
    if a and b:
        return True
    else:
        return False

def logicalor(a, b):
    # Logical OR: At least one must be True
    if a or b:
        return True
    else:
        return False

def logicalnot(a):
    # Logical NOT: Reverses the boolean value
    if not a:
        return True
    else:
        return False

# Testing the functions
logicaland_result = logicaland(True, False)
logicalor_result = logicalor(True, False)
logicalnot_result = logicalnot(True)

print("Logical AND result:", logicaland_result)
print("Logical OR result:", logicalor_result)
print("Logical NOT result:", logicalnot_result)
