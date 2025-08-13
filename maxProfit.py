#----- First solution to understand the problem
#---- with this solution we'll have a time limit exceeded because the complexity is O(n^2)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        while prices:  # tant que la liste n'est pas vide
            min_price = min(prices)  # plus petit prix
            pos = prices.index(min_price)  # position du min

            if pos == len(prices) - 1:  # si c'est le dernier élément, pas de max possible
                prices.remove(min_price)
                continue

            max_price = max(prices[pos+1:])  # max après le min trouvé

            if max_price - min_price > profit:
                profit = max_price - min_price

            # enlever le min pour chercher d'autres profits possibles
            prices.remove(min_price)

        return profit


# --------------------- updated solution 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # biggest number possible 
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)            # Update min price so far
            max_profit = max(max_profit, price - min_price)  # Update max profit so far
            
        return max_profit
