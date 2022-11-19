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

def calculate(expression:str):
    # "5^2 + 3.5*2"

    if " " in expression:
        expression = expression.replace(" ", "")
    
    # "5^2+3.5*2"
    
    exp_ops = []
    exp_nums = []

    i = 0
    ops = ["^", "*", "/", "+", "-"]

    for count, char in enumerate(expression):
        if char in ops:
            exp_ops.append(char)
            exp_nums.append(expression[i:count])
            i = count + 1
        elif count == len(expression) - 1:
            exp_nums.append(expression[i:count + 1])
    
    # exp_ops = "^", "*", "+"
    # exp_nums = "5", "2", "3.5", "2"

    for op in ops:
        while op in exp_ops:
            num1 = float(exp_nums[exp_ops.index(op)])
            num2 = float(exp_nums[exp_ops.index(op) + 1])
            exp_nums[exp_ops.index(op)] = operate(num1, num2, op)

            del exp_nums[exp_ops.index(op) + 1]
            del exp_ops[exp_ops.index(op)]

    return exp_nums[0]

if __name__ == "__main__":
    random_tests = [
        ("5^2 + 3.5*2", 32),
        ("5^2 + 3.5*2 + 2^3", 40),
        ("5+ 4*4^2", 69)
    ]

    for test in random_tests:
        print(calculate(test[0]) == test[1])