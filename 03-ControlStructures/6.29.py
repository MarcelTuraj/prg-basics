def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def displayer(N):
    """Find and return the first N leading prime numbers as a string."""
    sequence = ""
    count = 0
    x = 2  # Start checking for primes from 2
    
    while count < N:
        if is_prime(x):
            sequence += str(x) + ", "  # Add the prime number to the sequence
            count += 1
        x += 1  # Move to the next candidate number
    
    # Remove the last comma and space if sequence is not empty
    if sequence:
        sequence = sequence[:-2]
        
    return sequence

# Input and output
N = int(input("N: "))
print(displayer(N))