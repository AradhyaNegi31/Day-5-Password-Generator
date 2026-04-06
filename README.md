# Password Generator

This is a simple Python program that generates a **random secure password** based on user preferences. You can specify how many alphabets, numbers, and special characters you want in your password, and the program will create a randomized password for you.

---

## Features

- User-defined number of **alphabets** (both lowercase and uppercase).  
- User-defined number of **numbers**.  
- User-defined number of **special characters** (like `!`, `@`, `#`, etc.).  
- Randomized order of characters to make the password more secure.  
- Easy to use and modify.

---

## How to Use

1. Make sure you have Python installed on your computer.  
2. Copy the code into a Python file, e.g., `PW_GENERATOR(Begineer_05).py`.  
3. Run the program:

```bash
python PW_GENERATOR(Begineer_05).py
Enter the number of alphabets, numbers, and special characters you want when prompted.

The program will print your generated password.

Example

Copy code
How many alphabets would you like in your password? 5
How many numbers would you like in your password? 3
How many special characters would you like in your password? 2
Your password is: aB3$dE7@f1


How It Works
The program stores alphabets, numbers, and special characters in separate lists.

It takes user input for how many of each character type to include.

It randomly selects characters from each list based on the user input.

All selected characters are combined into a list and shuffled for randomness.

The final password is formed by joining all characters into a string and displayed to the user.

Dependencies
 Python 3.x

 random module (built-in Python library)

Author - Aradhya Negi