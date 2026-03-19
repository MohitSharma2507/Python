import os

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    return a / b

operations_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": divide,
}

def calculator():
    number1 = int(input("Enter first number : "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
        op_symbol = input("Pick an operation : ")
        
        if op_symbol not in operations_dict:
            print("Invalid operation. Please try again.")
            continue
        
        number2 = int(input("Enter Second number : "))
        calc_num = operations_dict[op_symbol]
        output = calc_num(number1, number2)
        
        if output is None:
            continue
        
        print(f"{number1} {op_symbol} {number2} = {output}")

        user_input = input(f"Enter 'y' to continue calculations with {output} or 'n' to start new calculation and 'x' to exit : ").lower()
        if user_input == 'y':
            number1 = output
        elif user_input == 'n':
            continue_flag = False
            os.system('cls')
            calculator()      
        elif user_input == 'x':
            continue_flag = False

calculator()