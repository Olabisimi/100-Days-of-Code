import art

def add(n1, n2):
    return n1 + n2\

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    print(art.logo)
    accumulation = True
    input1 = float(input("What is your first number?"))
    while accumulation:
        for symbol in operators:
            print(symbol)
        operation = input("Pick an operator")
        input2 = float(input("what is your second number?"))
        result = operators[operation](input1, input2)
        print(f"{input1} {operation} {input2} = {result}")
        choice = input(f"Type 'y' to continue with {result}, or type 'n' to start over")
        if choice == "y":
            input1 = result
        else:
            accumulation = False
            print("\n" * 20)
            calculation()
calculation()
