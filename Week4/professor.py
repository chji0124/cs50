import random
# answer of the problem
# how many times user has tried
# how many times user answered correctly so that they can get a score
# use for loops 
def main():
    score = 0
    level = get_level()
    for i in range(10):
        x, y = generate_integer(level), generate_integer(level)
        answer = x + y

        for chance in range(3):
            print(f"{x}+{y} = ", end="")
            equation = int(input())
            if equation == answer:
                score = score + 1
                break
            elif equation != answer and chance == 2:
                print(f"{x}+{y} =",answer)
                break
            else:
                print("EEE")
    print(f"Score: {score}")
           
                
               

# prompt the user for a level and returns 1, 2, or 3
# use while true loop to catch ValueError 
# need return value
def get_level():
    while True:
        try:
            lev = int(input("Level 1, 2, 3: "))
            if 1 <= lev <= 3:
                return lev
        except ValueError:
            pass

# randomly generated non-negative integer with level digits or 
# raises a ValueError if level is not 1, 2, or 3:
def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    elif level == 2:
        return random.randint(10, 100)
    elif level == 3:
        return random.randint(100, 1000)
    else:
        raise ValueError

if __name__ == "__main__":
    main() 