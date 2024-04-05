def print_diamond(n):
    # Upper half of the diamond
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    
    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Example usage:
n = 4
print_diamond(n)