# Coin Change Problem using Greedy Algorithm

def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    if amount != 0:
        return "Change cannot be made with the given coins."
    return result

# Testing Coin Change Problem
coins = [1, 2, 5, 10]
amount = 27
print(f"Coins for {amount}: {coin_change(coins, amount)}")
