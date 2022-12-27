# Functions,Variables
#### 1. Creating Code with Python
###### - VS Code is a special type of text editor that is called a compiler. At the top, you’ll notice a text editor and, at the bottom you will see a terminal where you can execute commands.

###### - In the terminal, you can execute `code hello.py` to start coding.

###### - In the terminal window, you can execute commands. 

###### - Recall, computers really only understand zeros and ones. Therefore, when you run `python hello.py`, python will interpret the text that you created in `hello.py` and translate it into the zeros and ones that the computer can understand.

#### 2. Functions
###### - Functions are verbs or actions that the computer or computer language will already know how to perform.

#### 3. Variables
###### - A variable is just a container for a value within own program.
###### - In your program, you can introduce your own variable in your program by editing it to read
###### 
```
name = input("What's your name? ")
print("hello, world")
```
###### - Notice that this equal `=` sign in the middle of `name = input("What's your name? ")` has a special role in programming. This equal sign literally assigns what is on the right to what is on the left. Therefore, the value returned by `input("What's your name? ")` is assigned to `name`.
#### 4. Comments
###### - Comments are a way for programmers to track what they are doing in their programs and even inform others about their intentions for a block of code.
#### 5. Strings and Paremeters
###### - A string, known as a `str` in Python, is a sequence of text.
###### - Functions take arguments that influence their behavior. If we look at the documentation for `print` you’ll notice we can learn a lot about the arguments that the print function takes.
###### - Looking at this documentation, you’ll learn that the print function automatically include a piece of code `end='\n'. This \n indicates that the print function will automatically create a line break when run. The print function takes an argument called end` and the default is to create a new line.
###### - modifying codes
```
# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")`
print(name)
```

###### - Parameters, therefore, are arguments that can be taken by a function.

#### 5. Formatting Strings
```
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
```
###### - This `f` is a special indicator to Python to treat this string a special way

#### 6. More on Strings
###### - Strings have the ability to remove whitespace from a string.
###### - By utilizing the method `strip` on `name` as `name = name.strip()`, it will strip all the whitespaces on the left and right of the users input.
###### - Using the `title` method, it would title case the user’s name:
```
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# Print the output
print(f"hello, {name}")
```
###### - Notice that you can modify your code to be more efficient:
```
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()

# Print the output
print(f"hello, {name}")
```
###### - We could even go further!
```
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")
```
#### 7. Integers or int
###### - In Python, an integer is referred to as an `int`.
###### - All numeric types (except complex) support the following operations 
```
x + y: sum of x and y
x - y: difference of x and y
x * y: product of x and y
x / y: quotient of x and y
x // y: floored quotient of x and y
x % y: remainder of x / y
```
#### 8. Float Basics
###### - A floating point value is a real number that has a decimal point in it, such as `0.52`.
###### - `round` to a digit to its nearest integer
```
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the result
print(z)
```
###### - `round` to nearest integer with comma
```
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the formatted result
print(f"{z:,}")
```

#### 9. More on Floats
###### - Round down
```
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result and round the result to the neartest two decimal points
z = round(x / y, 2)

# Print the result
print(z)
```
###### - Round down using `fstring` 
```
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")
```

