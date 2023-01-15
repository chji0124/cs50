texts = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]

for text in texts:
    if text in vowels:
        texts = texts.replace(text.lower(), "")
print("Output: " + texts)