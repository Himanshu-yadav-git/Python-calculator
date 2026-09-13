# 🧮 Python Calculator

A simple **console-based calculator built with Python**.
This project is designed to practice Python fundamentals such as functions, loops, conditional statements, exception handling, lists, and formatted strings.

## ✨ Features

The calculator currently supports:

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* `%` Modulus
* 📊 Percentage calculation
* 🔢 Power calculation
* √ Square root
* 📜 Calculation history
* 🗑️ Clear calculation history
* ❌ Input validation and error handling
* 🔄 Continuous calculations until the user chooses to exit

## 📋 Menu

```text
====================================
        PYTHON CALCULATOR
====================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Percentage
7. Power
8. Square root
9. History
10. Clear history
11. Exit
====================================
```

## 🛠️ Technologies Used

* **Python 3**
* No external libraries are required.

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check by running:

```bash
python --version
```

### 2. Save the program

Save the Python code as:

```text
calculator.py
```

### 3. Run the program

Open your terminal in the project folder and run:

```bash
python calculator.py
```

## 📜 Calculation History

The calculator stores calculations in a Python list called `history`.

For example:

```text
5.0 + 10.0 = 15.0
20.0 × 3.0 = 60.0
√25.0 = 5.0
```

Choose:

```text
9. History
```

to display previous calculations.

Choose:

```text
10. Clear history
```

to remove all stored calculations.

> **Note:** The current version stores history only while the program is running. Closing the program will reset the history.

## 🛡️ Error Handling

The calculator uses `try` and `except` to handle invalid inputs.

For example:

```text
Enter your choice: abc
❌ Invalid choice
```

It also prevents division or modulus by zero:

```text
Enter your second number: 0
❌ Cannot divide by zero
```

The square root operation also checks for negative numbers:

```text
Enter your number: -25
❌ Cant find square root of negative numbers.
```

## 🧠 Python Concepts Practiced

This project helped me practice:

* Variables
* Functions
* `while` loops
* `if`, `elif`, and `else`
* Lists
* `try` and `except`
* `continue` and `break`
* User input with `input()`
* Type conversion using `int()` and `float()`
* Formatted strings using **f-strings**
* Basic mathematical operators
* List methods such as `.append()` and `.clear()`

## 📈 Project Improvements

The calculator started as a basic calculator and was gradually improved with:

1. Basic arithmetic operations
2. Error handling
3. Percentage calculation
4. Power calculation
5. Square root
6. Calculation history
7. Clear history
8. Better menu and user interface

## 🔮 Future Improvements

Some features I plan to add in the future:

* 💾 Save history to a `.txt` file
* 📂 Load previous history when the program starts
* 🔢 Factorial
* 🔄 Continue calculations using the previous result
* 🕒 Add date and time to calculation history
* 🧮 More advanced mathematical operations
* 🎨 Improve the console interface

## 👨‍💻 About the Project

This is a beginner-level Python project created to improve my programming skills and understand how different Python concepts work together in a practical application.

---

⭐ **More features will be added as I continue learning Python.**
