coke = 50
coins = [5, 10, 25]

while True:
    machine = int(input("Amount Due: "))
    coin = int(input("Insert Coin: "))
    for c in coins:
        if coin == coins:
            coke = coke - coin
            break
    if coke <= 0: 
        break