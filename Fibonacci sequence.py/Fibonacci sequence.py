##اسامة محمد صالح الهرش


def fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    
    if n <= 1:
        return sequence[:n + 1]  # Return the sequence up to the nth number
    
    while len(sequence) <= n:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number
        sequence.append(next_number)  # Add the next number to the sequence
    
    return sequence

# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(n)
print("Fibonacci sequence:", fib_sequence)