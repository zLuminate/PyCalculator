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
    if " " in expression: expression = expression.replace(" ", "")
    exp_ops, exp_nums = [], []
    
    i = 0
    ops = ["^", "*", "/", "+", "-"]
    for count, char in enumerate(expression):
        if char in ops:
            exp_ops.append(char)
            exp_nums.append(expression[i:count])
            i = count + 1
        elif count == len(expression) - 1:
            exp_nums.append(expression[i:count + 1])

    ops = ["^", "*/", "+-"]
    for op in ops:
        if op == "^":
            while "^" in exp_ops:
                index = exp_ops.index("^")
                exp_nums[index] = operate(int(exp_nums[index]), int(exp_nums[index + 1]), "^")
                exp_nums.pop(index + 1)
                exp_ops.pop(index)
        else:
            if (op[0] and op[1]) in exp_ops:
                if exp_ops.index(op[0]) < exp_ops.index(op[1]):
                    while op[0] in exp_ops:
                        index = exp_ops.index(op[0])
                        exp_nums[index] = operate(int(exp_nums[index]), int(exp_nums[index + 1]), op[0])
                        exp_nums.pop(index + 1)
                        exp_ops.pop(index)
                else:
                    while op[1] in exp_ops:
                        index = exp_ops.index(op[1])
                        exp_nums[index] = operate(int(exp_nums[index]), int(exp_nums[index + 1]), op[1])
                        exp_nums.pop(index + 1)
                        exp_ops.pop(index)
            elif op[0] in exp_ops:
                while op[0] in exp_ops:
                    index = exp_ops.index(op[0])
                    exp_nums[index] = operate(int(exp_nums[index]), int(exp_nums[index + 1]), op[0])
                    exp_nums.pop(index + 1)
                    exp_ops.pop(index)
            elif op[1] in exp_ops:
                while op[1] in exp_ops:
                    index = exp_ops.index(op[1])
                    exp_nums[index] = operate(int(exp_nums[index]), int(exp_nums[index + 1]), op[1])
                    exp_nums.pop(index + 1)
                    exp_ops.pop(index)

    return exp_nums[0]

if __name__ == "__main__":
    print(calculate("500*2-7^3-10+20"))