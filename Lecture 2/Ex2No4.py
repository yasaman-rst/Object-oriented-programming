def factorials(n: int):
    # Fractionals
    factorial_dict = {}
    
    # No from 1 to n
    for i in range(1, n + 1):
        # Calculating
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        
        # Store the factorial in the dictionary
        factorial_dict[i] = factorial
    
    return factorial_dict

# Example usage
k = factorials(5)
print(k[1])  # Output: 1
print(k[3])  # Output: 6
print(k[5])  # Output: 120