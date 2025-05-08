print("Welcome to Calculator")
while True:
    number_Operator = input("Enter mathematical calculations (To Exit, Write exit) : ")
    if number_Operator in ("exit", "exit()", "Exit", "Exit()"):
        print("Calculator Task Finished")
        break
    check_Numbers = number_Operator.split()
    after_Check = []
    for i in check_Numbers:
        if i.isnumeric() or i in ("+", "-", "*", "/", "//", "%", "**"):
            after_Check.append(i)
    if after_Check == check_Numbers and len(check_Numbers) >= 3:
        result = eval(number_Operator)
        print(result)
    else:
        print("Input must be a number and an operator")
        print("Try again")
