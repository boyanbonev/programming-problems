# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.

from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        arr_len = len(height)
        if arr_len < 3:
            return 0

        left_maxes: list[int] = []
        right_maxes: list[int] = [0] * arr_len
        current_left_max:int = 0
        current_right_max: int = 0
        for i in range(0, arr_len):
            current_left_max = max(current_left_max, height[i])
            left_maxes.append(current_left_max)

            current_right_max = max(current_right_max, height[arr_len - i - 1])
            right_maxes[arr_len - i - 1] = current_right_max

        sum: int = 0
        for i in range(0, arr_len - 1):
            sum+=  min(left_maxes[i], right_maxes[i]) - height[i]

        return sum



if __name__ == "__main__":
    s = Solution()

    def test(height: list[int], expected: int):
        print("============================================================")
        print(f"Input: {height}, expected={expected}")

        result: int = s.trap(height)

        print(f"result={result}")
        assert expected == result


    test([0,1,0,2,1,0,1,3,2,1,2,1], 6)
    test([4,2,0,3,2,5], 9)
    test([0,3, 1, 0, 1, 0, 1, 0, 2, 0], 9)

    # test([1, 5, 2, 3, 4], 0)
