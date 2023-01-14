# Conditionals
#### 1. Conditionals
###### - Conditionals allow programmers to make decisions
###### - Built within Python are a set of “operators” that can are used to ask mathematical questions.
###### - Conditional statements compare a left-hand term to a right-hand term.

#### 2. if Statements
```
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```
###### - The if statement compares x and y. If the condition of x < y is met, the print statement is executed.
###### - If statements use bool or boolean values (true or false) to decide whether or not to execute.

#### 3. Control Flow, elif, and else
```
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```
###### - First, the `if` statement is evaluated. If this statement is found to be true, all the `elif` statements not be run at all. 
###### - However, if the `if` statement is evaluated and found to be false, the first `elif` will be evaluated. If this is true, it will not run the final evaluation.
###### - We can create a “catch-all,” default outcome using an `else` statement.

#### 4. or
###### - `or` allows your program to decide between one or more alternatives. 
###### - it returns True if one of the statements is true.

#### 5. and
###### - Similar to `or`, `and` can be used within conditional statements.
###### - `and` returns True if both statements are true.

#### 6. Modulo
###### - The modulo `%` operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.
###### - For example, 4 % 2 would result in zero, because it evenly divides. However, 3 % 2 does not divide evenly and would result in a number other than zero!

#### 7. `match`
###### - `match` statements can be used to conditionally run code that matches certain values.
###### - A match statement compares the value following the `match` keyword with each of the values following the `case` keywords. In the event a match is found, the respective indented code section is executed and the program stops the matching.
```
  name = input("What's your name? ")

  match name: 
      case "Jamie":
          print("KR")
      case "Ronnie":
          print("KR")
      case _:
          print("Who?")
```
###### - It will print out`KR` if `Jamie` or `Ronnie` is inputted. If a random name other than `Jamie` or `Ronnie` is inputted, it will print `Who?`.
###### - The use of the single vertical bar `|` allows  to check for multiple values in the same case statement.
```
 name = input("What's your name? ")

  match name: 
      case "Jamie" | "Ronnie": 
          print("KR")
      case _:
          print("Who?")
```