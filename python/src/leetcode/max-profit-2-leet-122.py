# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    # The description for this one doesn't do a great job explaining the rules for buying and selling the stock. That's why
    # a lot of people have used dynamic optimisation with memoisation and other complicated solutions while in reality
    # the authors of the problem just want to sell whenever there's a chance for profit. There are different version of
    # this problem which may require using theses advanced techniques.
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                # sell
                max_profit += prices[i] - prices[i - 1]

        return max_profit

if __name__ == "__main__":
    sol = Solution()

    def test(prices: List[int], expected_max_profit: int):
        max_profit = sol.maxProfit(prices)

        print("================================================")
        print(f"Prices: {str(prices)}")
        print(f"Max profit          : {max_profit}")
        print(f"Expected max profit : {expected_max_profit}")

        assert max_profit == expected_max_profit

    test([7,1,5,3,6,4], 7)
    test([1,2,3,4,5], 4)
    test([7,6,4,3,1], 0)


