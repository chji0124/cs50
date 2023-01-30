import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break
text = p.join(names)
print("Adieu, adieu, to " + text )



