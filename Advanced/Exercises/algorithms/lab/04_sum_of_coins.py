def choose_coins(coins, target):
    used_coins = {}
    idx = 0

    while target > 0 and idx < len(coins):
        count_current_coins = target // coins[idx]
        target = target % coins[idx]

        if count_current_coins > 0:
            used_coins[coins[idx]] = count_current_coins

        idx += 1

    if target != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"

        for coin, count in used_coins.items():
            result += f"{count} coin(s) with value {coin}\n"

        return result


some_coins = [int(x) for x in input().split(', ')]
target_sum = int(input())

print(choose_coins(some_coins, target_sum))