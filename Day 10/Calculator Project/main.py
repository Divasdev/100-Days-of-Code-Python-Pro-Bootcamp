# Simple calculator with memory loop

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero!"
    return n1 / n2

# Map operator symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))

    while True:
        for symbol in operations:
            print(symbol)
        op_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[op_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")

        cont = input(f"Type 'y' to continue working with {answer}, or 'n' to start a new calculation: ").lower()

        if cont == 'y':
            num1 = answer
        else:
            calculator()  # Restart fresh
            break

calculator()



