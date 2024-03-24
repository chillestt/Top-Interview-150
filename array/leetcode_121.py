def maxProfit(self, prices) -> int:
    # if not prices:
    #     return 0

    # min_price = prices[0]
    # max_profit = 0

    # for price in prices:
    #     min_price = min(min_price, price)
    #     max_profit = max(max_profit, price - min_price)

    # return max_profit

    buy = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy

    return profit