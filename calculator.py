import os


def calculator():

    while True:

        # Title
        print("====================================")
        print("        PYTHON CALCULATOR")
        print("====================================")

        # Menu
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Percentage")
        print("7. Power")
        print("8. Square root")
        print("9. History")
        print("10. Clear history")
        print("11. Exit")
        print("====================================")

        # Choice input
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid choice")
            continue

        # Exit
        if choice == 11:
            print("Thanks for using our calculator.")
            break

        # History
        if choice == 9:
            print("\n========== CALCULATION HISTORY ==========")

            if os.path.exists("history.txt"):
                with open("history.txt", "r") as f:
                    history = f.read()

                if history:
                    print(history)
                else:
                    print("No calculations yet.")
            else:
                print("No calculations yet.")

            print("=========================================")
            continue

        # Clear History
        if choice == 10:
            if os.path.exists("history.txt"):
                os.remove("history.txt")
                print("✅ History has been cleared.")
            else:
                print("❌ No history found.")

            continue

        # Square Root
        if choice == 8:

            try:
                num = float(input("Enter your number: "))
            except ValueError:
                print("❌ Invalid number")
                continue

            if num < 0:
                print("❌ Can't find square root of a negative number.")
                continue

            result = num ** 0.5
            calculation = f"√{num} = {result}"

            print("The square root is:", result)

            # Save square root to history
            with open("history.txt", "a") as f:
                f.write(calculation + "\n")

            continue

        # Check valid choice
        if choice not in [1, 2, 3, 4, 5, 6, 7]:
            print("❌ Invalid choice")
            continue

        # Input numbers
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("❌ Invalid number")
            continue

        # Addition
        if choice == 1:
            result = num1 + num2
            calculation = f"{num1} + {num2} = {result}"
            print("The addition is:", result)

        # Subtraction
        elif choice == 2:
            result = num1 - num2
            calculation = f"{num1} - {num2} = {result}"
            print("The difference is:", result)

        # Multiplication
        elif choice == 3:
            result = num1 * num2
            calculation = f"{num1} × {num2} = {result}"
            print("The multiplication is:", result)

        # Division
        elif choice == 4:
            if num2 == 0:
                print("❌ Cannot divide by zero")
                continue

            result = num1 / num2
            calculation = f"{num1} ÷ {num2} = {result}"
            print("The division is:", result)

        # Modulus
        elif choice == 5:
            if num2 == 0:
                print("❌ Cannot divide by zero")
                continue

            result = num1 % num2
            calculation = f"{num1} % {num2} = {result}"
            print("The modulus is:", result)

        # Percentage
        elif choice == 6:
            if num2 == 0:
                print("❌ Cannot divide by zero")
                continue

            result = (num1 / num2) * 100
            calculation = f"{num1} is {result}% of {num2}"
            print("The percentage is:", result)

        # Power
        elif choice == 7:
            result = num1 ** num2
            calculation = f"{num1} ** {num2} = {result}"
            print("The power is:", result)

        # Save calculation to history
        with open("history.txt", "a") as f:
            f.write(calculation + "\n")


# Run calculator
calculator()