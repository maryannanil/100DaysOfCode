#write code to swap two numbers#write code to swap two numbers

# Example: swapping values of a and b
a = 5
b = 10

# Swap using a temporary variable
temp = a
a = b
b = temp

print("After swapping (using temp): a =", a, ", b =", b)

# Swap using Python's tuple unpacking
a, b = b, a

print("After swapping (using tuple unpacking): a =", a, ", b =", b)