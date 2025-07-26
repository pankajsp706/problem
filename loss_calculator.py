def minimize_loss(prices):
    n = len(prices)
    min_loss = float('inf')
    buy_year = sell_year = -1

    for i in range(n):
        for j in range(i+1, n):
            if prices[i] > prices[j]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year, sell_year = i + 1, j + 1
    return buy_year, sell_year, min_loss

# Example usage
if __name__ == "__main__":
    prices = [20, 15, 7, 2, 13]
    buy, sell, loss = minimize_loss(prices)
    print(f"Buy in year {buy}, sell in year {sell}, loss = {loss}")
