# In deep.py, 
# implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.


question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
def answers():
    if question == "42" or question == "Forty Two" or question == "forty-two":
        print("Yes")
    else:
        print("No")
answers()