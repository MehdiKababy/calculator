def calculate():
    while True:
        input_calculate = input(
            "Enter mathematical calculations (To Exit, Type Exit) : "
        )
        if input_calculate.title() in ("Exit", "Leave"):
            break
        check_items = []
        for i in input_calculate:
            if i.isnumeric() or i in (" ", "+", "-", "*", "/", "//", "%", "**"):
                check_items.append(True)
            else:
                check_items.append(False)
        if all(check_items):
            print(eval(input_calculate))
        else:
            print("The math operation is wrong")


if __name__ == "__main__":
    print("Welcome to Calculator")
    calculate()
