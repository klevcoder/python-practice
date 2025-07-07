# Define a function to perform addition
def add(x, y):
    return x + y

# Define a function to perform subtraction
def subtract(x, y):
    return x - y

# Define a function to perform multiplication
def multiply(x, y):
    return x * y

# Define a function to perform division
def divide(x, y):
    # Avoid dividing by zero
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

# Main function that controls the calculator
def main():
    print("Welcome to Python Calculator! 🧮")

    # Start an infinite loop for repeated calculations
    while True:
        # Show available operations to the user
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user choice
        choice = input("Enter choice (1-5): ")

        # Exit the loop if the user chooses 5
        if choice == '5':
            print("Exiting calculator. Goodbye! 👋")
            break

        # Validate that the choice is one of the expected options
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please choose a number between 1 and 5.")
            continue

        # Get user input for numbers and handle non-numeric input
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue

        # Perform the selected operation
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        # Display the result
        print(f"Result: {result}")

# Run the calculator by calling the main function
if __name__ == "__main__":
    main()
