# Loops
#### 1. Loops
###### - loops are a way to do something over and over again.
#### 2. While Loops
###### - The `while` loop is nearly universal throughout all coding languages.
###### - Such a loop will repeat a block of code over and over again.
```
i = 2
while i != 0:
    print("meow")
```
###### - Even though this code will execute `print("meow")` multiple times, it will never stop! It will loop forever.
###### - `while` loops work by repeatedly asking if the condition of the loop has been fulfilled. 
###### - When you get stuck in a loop that executes forever, you can press control-c on your keyboard to break out of the loop.
###### - To fix this loop that lasts forever:
```
i = 2
while i != 0:
  print("meow")
  i = i - 1
```
###### - Notice that now our code executes properly, reducing `i` by `1` for each “iteration” through the loop.
###### - We can further improve our code as follows:
```
  i = 1
  while i <= 2:
      print("meow")
      i = i + 1
```
###### - Notice that when we code `i = i + 1` we assign the value of `i` from the right to the left.
###### - We can improve our code, to start counting with zero:
```
i = 0
while i < 2:
    print("meow")
    i += 1
```
#### 2. For Loops