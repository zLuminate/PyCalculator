def operate(num1, num2, op):
    if op == "^":
        return num1 ** num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2

def theSmallerOf(a, b):
    if a < b:
        return a
    else:
        return b

def calculate(expression:str):
    if " " in expression: expression = expression.replace(" ", "")
    tokens = []

    i = 0
    for count, char in enumerate(expression):
        if char in "^*/+-":
            tokens.append(expression[i:count])
            tokens.append(char)
            i = count + 1
        elif count == len(expression) - 1:
            tokens.append(expression[i:count + 1])
    
    for op in [("^"), ("*", "/"), ("+", "-")]:
        while any(x in tokens for x in op):
            if len(op) != 1:
                try:
                    index = theSmallerOf(tokens.index(op[0]), tokens.index(op[1]))
                except ValueError:
                    if op[0] in tokens:
                        index = tokens.index(op[0])
                    else:
                        index = tokens.index(op[1])
            else: index = tokens.index(op[0])
            tokens[index - 1] = operate(float(tokens[index - 1]), float(tokens[index + 1]), tokens[index])
            del tokens[index:index + 2]

    return tokens[0]

import random
import time
import threading

trueCount = 0
start = time.time()

def constant_calculate():
    global trueCount, start

    while trueCount < 10**9:
        arr=[]
        for i in range(5):
            arr.append(str(random.randint(1, 100)))
            arr.append(random.choice(["*", "/", "+", "-"]))
        arr.append(str(random.randint(1,100)))

        expression = "".join(arr)
        if calculate(expression) == eval(expression):
            trueCount += 1
        else:
            "CODE FAILED"

def print_rate():
    global trueCount, start, yourmom

    while True:
        print(trueCount / (time.time() - start), yourmom)
        time.sleep(0.25)

yourmom = 0

if __name__ == "__main__":
    threading.Thread(target=print_rate).start()
    for i in range(41):
        yourmom += 1
        threading.Thread(target=constant_calculate).start()