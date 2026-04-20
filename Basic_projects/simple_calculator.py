# this is a simple calculator

def main():
    try:
        x = float(input("enter a number x ?: "))
        y = float(input("enter a number y ?: "))
    except ValueError:
        print("invalid number input.")
    
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }

    while True:
        func = input("Choose operation (+, -, *, /) or 'q' to quit: ").strip()
        
        if func == 'q':
            break
        
        if func in operations:
            result = operations[func](x, y)
            print(result)
            break
        else:
            print("Invalid operator. Try again.")


    
main()

