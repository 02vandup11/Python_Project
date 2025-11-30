# ==========================
# Calculator Program (CLI)
# ==========================

# Define functions for each operation
def add(a, b):
    """Return sum of a and b"""
    return a + b

def subtract(a, b):
    """Return a minus b"""
    return a - b

def multiply(a, b):
    """Return a times b"""
    return a * b

def divide(a, b):
    """Return a divided by b, handle division by zero"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def calculator():
    """Main calculator loop"""
    print("========== Simple Calculator ==========")
    print("You can perform: +  -  *  /")
    print("Type 'q' at any time to quit.\n")

    while True:
        # Take first input
        num1_input = input("Enter first number (or 'q' to quit): ")
        if num1_input.lower() == "q":
            print("Exiting calculator. Goodbye!")
            break  # exit loop

        # Validate and convert first number
        try:
            num1 = float(num1_input)
        except ValueError:
            print(" Invalid input. Please enter a valid number.\n")
            continue  # restart loop

        # Take operator
        op = input("Enter operator (+, -, *, /): ")
        if op not in ["+", "-", "*", "/"]:
            print(" Invalid operator. Please enter one of +, -, *, /.\n")
            continue

        # Take second input
        num2_input = input("Enter second number: ")
        try:
            num2 = float(num2_input)
        except ValueError:
            print(" Invalid input. Please enter a valid number.\n")
            continue

        # Perform operation based on operator
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)

        # Print result
        print(f" Result: {num1} {op} {num2} = {result}\n")


# Run calculator only if this file is executed directly
if __name__ == "__main__":
    calculator()
