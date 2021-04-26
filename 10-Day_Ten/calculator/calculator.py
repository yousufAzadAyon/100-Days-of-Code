from art import calculator_art

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2


operation = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : division
}

def calculator():
    should_continue = True
    print(calculator_art)
    num1 = float(input('enter first number: '))
    for symbol in operation:
        print(symbol)
    while should_continue:
        operation_symbol = input('enter what operation you want to perform: ')
        num2 = float(input('enter another number: '))

        operation_function = operation[operation_symbol]
        answer = round(operation_function(num1, num2),2)
        print(f'{num1} { operation_symbol} {num2} = {answer}')

        if input(f'type "yes" to continue with {answer} or type "no" to start over\n:') == "yes":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()