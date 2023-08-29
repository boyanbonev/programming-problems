# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

from typing import Dict, List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = -1
        current_min: int = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - current_min)
            current_min = min(prices[i], current_min)

        return max_profit if max_profit > -1 else 0


if __name__ == "__main__":
    sol = Solution()

    def test(prices: List[int], expected_max_profit: int):
        max_profit = sol.maxProfit(prices)

        print("================================================")
        print(f"Prices: {str(prices)}")
        print(f"Max profit          : {max_profit}")
        print(f"Expected max profit : {expected_max_profit}")

        assert max_profit == expected_max_profit

    test([7,1,5,3,6,4], 5)
    test([7,6,4,3,1], 0)
    test([7,8,6,4,3,1], 1)

