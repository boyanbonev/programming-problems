# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
# Explanation of the solution - https://www.youtube.com/watch?v=dJ7sWiOoK7g

from typing import List

class Solution:

    def jump(self, nums: List[int]) -> int:
        left = right = 0
        hops = 0

        while right < len(nums) - 1:
            max_range = 0
            for i in range(left, right + 1):
                max_range = max(max_range, i + nums[i])

            left = right + 1
            right = max_range
            hops += 1

        return hops

if __name__ == "__main__":
    sol = Solution()

    def test(nums: List[int], expected_result: int):
        print("=====================================================")
        # print(str(nums))

        result:  int = sol.jump(nums)

        print(f"Result={result}; expected result = {expected_result}")

        assert result == expected_result

    test([2,0], 1)
    test([2,0,0], 1)
    test([2,3,1,1,4], 2)
    test([2,3,0,1,4], 2)
