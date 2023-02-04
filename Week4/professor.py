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
            equation = get_answer()
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

def get_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            return -100


# randomly generated non-negative integer with level digits or 
# raises a ValueError if level is not 1, 2, or 3:
def generate_integer(level):
    upperBound = 10 ** level
    lowerBound = int(upperBound / 10)
    return random.randint(lowerBound, upperBound)

if __name__ == "__main__":
    main() 