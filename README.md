# 🧮 Python Calculator

A simple **command-line calculator built using Python**.
This project allows users to perform basic mathematical operations such as addition, subtraction, multiplication, division, and modulus.

## 📌 Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* `%` Modulus
* 🚫 Prevents division by zero
* ❌ Handles invalid number inputs
* 🔄 Runs continuously until the user chooses Exit
* 📋 Simple and easy-to-use menu

## 🛠️ Technologies Used

* **Python 3**
* Built-in Python functions and operators
* No external libraries required

## 📂 Project Structure

```text
Python-Calculator/
│
├── calculator.py
└── README.md
```

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python version using:

```bash
python --version
```

### 2. Clone or Download the Project

Download the project to your computer or clone your repository.

```bash
git clone <your-repository-link>
```

### 3. Open the Project Folder

```bash
cd Python-Calculator
```

### 4. Run the Calculator

```bash
python calculator.py
```

## 💻 How to Use

When you run the program, you will see a menu:

```text
====================================
        PYTHON CALCULATOR
====================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exit
====================================
```

Enter the number corresponding to the operation you want to perform.

For example:

```text
Enter your choice : 1
Enter your first number : 10
Enter your second number : 5
The addition is : 15.0
```

## ➕ Available Operations

| Choice | Operation      | Example               |
| -----: | -------------- | --------------------- |
|      1 | Addition       | `10 + 5 = 15`         |
|      2 | Subtraction    | `10 - 5 = 5`          |
|      3 | Multiplication | `10 × 5 = 50`         |
|      4 | Division       | `10 ÷ 5 = 2`          |
|      5 | Modulus        | `10 % 3 = 1`          |
|      6 | Exit           | Closes the calculator |

## ⚠️ Error Handling

The program handles some common errors.

### Invalid Choice

If the user enters an option other than 1–6:

```text
❌Invalid choice
```

### Invalid Number

If the user enters text instead of a number:

```text
❌ Invalid form
```

### Division by Zero

The calculator prevents division by zero:

```text
❌ Cannot divide by zero
```

The same protection is included for the modulus operation.

## 🎯 Learning Objectives

This project was created to practice fundamental Python concepts such as:

* Functions
* `while` loops
* `if`, `elif`, and `else`
* User input
* Type conversion using `float()`
* `try-except` error handling
* Arithmetic operators
* `break` and `continue`
* Basic program structure

## 🔮 Future Improvements

Some features that could be added in future versions:

* 🧮 Exponentiation
* √ Square root
* 📊 Calculation history
* 🔢 Support for more mathematical operations
* 🎨 Improved terminal interface
* 🧹 Better input validation
* 📝 Save calculation history to a file

## 👨‍💻 Author

**Himanshu**

This project was created as a beginner-friendly Python project to practice programming fundamentals.

## 📄 License

This project is free to use for learning and educational purposes.
