def calculater(n1, n2):
    print("Enter first number: ")
    n1 = float(input())
    print("Enter second number: ")
    n2 = float(input())
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice (1/2/3/4): "))
    if choice == 1:
        result = n1 + n2
        print("Result:", result)
    elif choice == 2:
        result = n1 - n2
        print("Result:", result)
    elif choice == 3:
        result = n1 * n2
        print("Result:", result)
    elif choice == 4:
        result = n1 / n2
        print("Result:", result)
    else:
        print("Invalid choice")
    again = input("Perform another calculation? (y/n): ")
    if again == 'y':
        calculater(n1, n2)
    else:
        exit()
calculater(0, 0)
