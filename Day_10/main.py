from Calculator import calculate
from ascii_art import logo

def calculator():
    print(logo)

    memory = 0
    start_over = True
    while True:

        if start_over:
            first_num = input("What's the first number?: ")
        else:
            first_num = str(memory)
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_num = input("What's the next number?: ")


        try:
            result = calculate(first_num, second_num, operation)
            memory = result
            print(f"{first_num} {operation} {second_num} = {result}")
            start_over = {'yes': False, 'no': True}[input(f"would you like to operate on top of {result}, or start over? 'yes' or 'no': ")]

            if start_over:
                memory = 0

        except (TypeError, ZeroDivisionError) as e:
            print(e)
            break



calculator()