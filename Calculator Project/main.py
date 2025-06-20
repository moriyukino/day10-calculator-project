import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return  n1 / n2

operation = {
    "+": add,
    "-":subtract,
    "*": multiply,
    "/": divide
}

# print(operation["*"](4,8))
def calculation():
    print(art.logo)
    n1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:

        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        answer = operation[operation_symbol](n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")

        if continue_calc == "y":
            n1 = answer
        else :
            should_continue = False
            print("\n" * 20)
            calculation()
while True:
        calculation()

