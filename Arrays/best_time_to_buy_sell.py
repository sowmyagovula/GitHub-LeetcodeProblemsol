"""
def BuynSellStock(prices):
    min = prices[0]
    max = 0
    min_index = 0

    if len(prices) < 2:
        return 0
    
    for i in range(1, len(prices)):
        print(i)
        if prices[i] < min:
            min = prices[i]
            min_index = i
        i += 1
        print(min, min_index)

    for j in range(min_index, len(prices)):
        if prices[j] > max:
            max = prices[j]
    return max - min

"""

def BuynSellStock(prices):
    profit = prices[0]
    max_profit = 0
    
    for i in range(0, len(prices)):
        if prices[i] < profit:
            profit = prices[i]
        elif prices[i] - profit > max_profit:
            max_profit = prices[i] - profit
    return max_profit


# Big-O-Notation O(n) time complexity, O(1) space complexity
# ✅ Runtime 34ms Beats 85.45% Analyze Complexity Memory 27.06MB Beats 9.04%
 

prices = [1, 2]
Output = 1
print(BuynSellStock(prices))
print(BuynSellStock(prices)==Output)
