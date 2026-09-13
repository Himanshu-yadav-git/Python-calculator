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

        choice = float(input("Enter your choice :"))
        if (choice == 6):
            print("Thanks for using our calculator.")
            break
        if choice not in [1,2,3,4,5]:
            print("❌Invalid choice")
            continue

        #input numbers

        try:
            num1 = float(input("Enter your first number :"))
            num2 = float(input("Enter your second number :"))
        except ValueError:
            print("❌ Invalid form")
            continue

        #addition

        if (choice == 1):
            sum = num1 + num2
            print("The addition is :",sum)

            #subtraction

        elif (choice == 2):
            diff = num1 - num2
            print("The difference is :",diff)

            #multiplication

        elif (choice == 3):
            multi = num1 * num2
            print("The multiplication is :",multi)

            #division

        elif (choice == 4):
            if (num2 == 0):
                print("❌ Cannot divide by zero")
                continue
            else:
                div = num1 / num2 
                print("The division is :",div)

            #Modulus

        elif (choice == 5):
            if (num2 == 0):
                print("❌ Cannot Divide by zero")
            else:
                mod = num1 % num2
                print("The modulus is :",mod)

#ready to use

calculator()