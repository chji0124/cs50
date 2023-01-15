def main():
    text = input("CamelCase: ")
    print("SnakeCase: " + camel2snake(text))

def camel2snake(text):
    for c in text:
        if c.isupper(): 
            text = text.replace(c, "_" + c.lower())
    return text

main()
    