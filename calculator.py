def calculator():
    while True:
        #Title
        print("====================================") 
        print("        PYTHON CALCULATOR")
        print("====================================")

        #Menu

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")
        print("====================================")

        #Choice input

        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("❌ Invalid choice")
            continue   
        if choice == 6:
            print("Thanks for using our calculator.")
            break
        if choice not in [1, 2, 3, 4, 5]:
            print("❌ Invalid choice")
            continue

        #input numbers

        try:
            num1 = float(input("Enter your first number:"))
            num2 = float(input("Enter your second number:"))
        except ValueError:
            print("❌ Invalid number")
            continue

        #addition

        if choice == 1:
            result = num1 + num2
            print("The addition is:", result)

            #subtraction

        elif choice == 2:
            result = num1 - num2
            print("The difference is:", result)

            #multiplication

        elif choice == 3:
            result = num1 * num2
            print("The multiplication is:", result)

            #division

        elif choice == 4:
            if num2 == 0:
                print("❌ Cannot divide by zero")
                continue

            result = num1 / num2 
            print("The division is:", result)

            #Modulus

        elif choice == 5:
            if num2 == 0:
                print("❌ Cannot Divide by zero")
                continue
            
            result = num1 % num2
            print("The modulus is:", result)

#ready to use

calculator()