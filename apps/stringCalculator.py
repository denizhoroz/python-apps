# data
symbols = ["+", "-", "*", "/"]


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def solve_equation(string):
    operationlist = string.split(" ")
    for i in operationlist:
        if i not in symbols:
            operationlist[operationlist.index(i)] = int(i)

    solved = False
    while not solved:
        for symbol in operationlist:
            if symbol == "*":
                i = operationlist.index(symbol)
                new_number = multiply((operationlist[i - 1]), (operationlist[i + 1]))
                operationlist[i] = new_number
                del operationlist[i + 1]
                del operationlist[i - 1]
                if len(operationlist) == 1:
                    solved = True
            elif symbol == "/":
                i = operationlist.index(symbol)
                new_number = divide((operationlist[i - 1]), (operationlist[i + 1]))
                operationlist[i] = new_number
                del operationlist[i + 1]
                del operationlist[i - 1]
                if len(operationlist) == 1:
                    solved = True
        for symbol in operationlist:
            if symbol == "-":
                i = operationlist.index(symbol)
                new_number = subtract((operationlist[i - 1]), (operationlist[i + 1]))
                operationlist[i] = new_number
                del operationlist[i + 1]
                del operationlist[i - 1]
                if len(operationlist) == 1:
                    solved = True
            elif symbol == "+":
                i = operationlist.index(symbol)
                new_number = add((operationlist[i - 1]), (operationlist[i + 1]))
                operationlist[i] = new_number
                del operationlist[i + 1]
                del operationlist[i - 1]
                if len(operationlist) == 1:
                    solved = True

    return operationlist


print("Calculator 1.0v (not accurate for long operations yet)")
print("(Please leave blanks between operations)")
userString = input()
result = solve_equation(userString)[0]
print(f"= {result}")
