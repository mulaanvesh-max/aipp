def get_positive_integer(prompt):
    """Prompt user for a positive integer and validate input, recording outcomes."""
    changes = []
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value > 0:
                changes.append(f"Accepted input: {value}")
                return value, changes
            else:
                changes.append(f"Rejected non-positive value: {value}")
                print("Please enter a positive integer.")
        except ValueError:
            changes.append(f"Rejected non-integer input: {user_input}")
            print("Invalid input. Please enter a positive integer.")

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Prompt user for sequence length
n, changes = get_positive_integer("Enter the number of Fibonacci terms (positive integer): ")

# Generate sequence
fib_seq = fibonacci_sequence(n)
changes.append(f"Generated sequence: {fib_seq}")

# Display results and recorded changes
print("Fibonacci sequence:", fib_seq)
print("Records of prompt handling and results:")
for change in changes:
    print("-", change)
