# 3. Exceptions
#### 1. Exceptions
###### - Exceptions are things that go wrong within our coding.
###### - syntax error 
```
print("hello, world)
```
###### - Double check if you typed the code correctly

#### 2. Runtime Exceptions
###### - Runtime errors refer to those created by unexpected behavior within your code. 
###### - For example, perhaps you intended for a user to input a number, but they input a character instead.
###### - An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.

#### 3. `try`
###### - In Python `try` and `except` are ways of testing out user input before something goes wrong.
```
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```
###### - Inputting `10` will be accepted. However, typing in `dog` will produce an error visible to the user, instructing them why their input was not accepted.
###### - This is still not the best way to implement this code.
###### - For best practice, we should only `try` the fewest lines of code possible that we are concerned could fail. Adjust your code as follows:
```
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
#### 3. `else`
###### - It turns out that there is another way to implement try that could catch errors of this nature.
```
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
###### - Notice that if no exception occurs, it will then run the block of code within `else`.
###### - Running the code and supplying `10`, you’ll notice that the result will be printed.
###### - Trying again, this time supplying `dog`, you’ll notice that the program now catches the error.
```
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```
###### - Notice that `while True` will loop forever.
###### - If the user succeeds in supplying the correct input, we can break from the loop and then print the output.

#### 4. `pass`
###### - We can make it such that our code does not warn our user, but simply re-asks them our prompting question by modifying our code as follows:
```
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass


main()
```
###### - Notice that our code will still function but will not repeatedly inform the user of their error.
###### - One final refinement that could improve the implementation of this `get_int` function.
###### - We probably want to pass in a prompt that the user sees when asked for input. Modify your code as follows.
```
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
```