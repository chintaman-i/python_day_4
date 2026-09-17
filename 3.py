def add(a, b):
    print("sum is:", a + b)

def subtract(a, b):
    print("difference is:", a - b)

def multiply(a, b):
    print("product is:", a * b)

def divide(a, b):
    print("quotient", a / b)

while True:
    k = input("Enter the operation (+, -, *, /) or 'exit' to quit: \n")
    
    if k == "exit":
        print("Exiting the calculator.")
        break
        
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    match k:
        case "+":
            add(a, b)
        case "-":
            subtract(a, b)
        case "*":
            multiply(a, b)
        case "/":
            divide(a, b)
        case _:
            print("Invalid operation. Please try again.")
