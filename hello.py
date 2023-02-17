playing = True

while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input("Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n")

    if operation == "exit":
        playing = False
    elif operation == "+":
        print("Result:", a + b)
    elif operation == "-":
        print("Result:", a - b)
    elif operation == "*":
        print("Result:", a * b)
    elif operation == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("cannot divide by zero.")