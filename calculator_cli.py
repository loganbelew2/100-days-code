
#Arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
def calculator():
    keep_going = True
    num1 = int(input("what is the first number?: \n"))
   
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    for op in operations:
            print(op)
    operation = input("pick a operation\n")

    while keep_going == True:
        num2 = int(input("what is the next number?: \n"))
        function_to_perform = operations[operation]
        answer = function_to_perform(num1, num2)
        print(f'{num1} {operation} {num2} = {answer}')
        num1 = answer
        new_op = input("type x to reset otherwise choose another operation to perform.\n") 
        if new_op is not "x":
            num1 = answer
            operation = new_op
        else:
            keep_going = False
            calculator()
calculator()