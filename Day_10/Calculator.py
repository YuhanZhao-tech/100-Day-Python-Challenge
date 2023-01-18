# Calculator

operation_list = ['+', '-', '*', '/']
def calculate(first_num, second_num, operation):
    """Take the first and second number and do the operation specified"""
    
    if not (first_num.isnumeric() and second_num.isnumeric() and operation in operation_list):
        raise TypeError("The operation cannot be completed.")
    return eval(f"{first_num} {operation} {second_num}")

    

