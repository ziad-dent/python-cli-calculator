def add (x, y):
    return x + y
def subtract(x, y):
    return x - y
def mutiply(x, y):
    return x * y
def power(x, y):
    return x ** y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return x / y
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("invalid input. please enter a number")
def calc():
    operation = {'+': add, '-': subtract, '*': mutiply, '/': divide, '**': power}
    history = []
    print("=== Simple CLI Calculator ===")
    print("Available operations: +, -, *, /, **")
    while True:
        num1 = get_number("enter first number: ")
        op = input("enter operator (+, -, *, /, **), history or 'quit' to exit: ")
        if op.lower() == 'quit':
            print("calculator exited")
            break
        if op.lower() == 'history':
            if not history:
                print("no calculations yet")
            else:
                print("calculation history:")
                for entry in history:
                    print(entry)
            continue
        if op in operation:
            num2 = get_number("enter second number: ")
            try:
                result = operation[op](num1, num2)
                print(f"{num1} {op} {num2} = {result}")
                history.append(f"{num1} {op} {num2} = {result}")
            except ZeroDivisionError as e:
                print(f"error: {e}")
        else:
            print("invalid operator. please use +, -, *, /, or **")


calc()