
def main():
    gauge = fuel_tank()
    if gauge <= 1:
        print("E")
    elif gauge >= 99:
        print("F")
    else:
        print(gauge,"%")

def fuel_tank():
    while True:
        fuel = input("Fraction: ")
        try:
            numerator, denominator = fuel.split("/")
            f = int(numerator) / int(denominator)
            if numerator <= denominator and denominator != 0:
                return int(f * 100)
        except (ValueError, ZeroDivisionError):
            pass

main()