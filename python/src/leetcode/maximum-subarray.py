# https://leetcode.com/problems/maximum-subarray/description/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left: int = 0
        right: int = 0

        max_sum: int = nums[left]
        current_sum: int = nums[left]
        while right < len(nums) - 1:
            right += 1

            if current_sum + nums[right] >= nums[right]:
                # the sum is increasing, so it is ok to add the next element
                current_sum += nums[right]
            else:
                # reset current_sum and start from the new element
                left = right
                current_sum = nums[left]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


if __name__ == "__main__":
    s = Solution()

    def test(nums: list[int], expected: int) -> None:
        print("===================================================")
        print(f"nums     = {nums}")
        print(f"expected = {expected}")

        result:int = s.maxSubArray(nums)

        print(f"result   = {result}")

        assert expected == result


    test([-2,1,-3,4,-1,2,1,-5,4], 6)
    test([-1,0,-2], 0)
    test([-2,1], 1)
    test([1], 1)
    test([5,4,-1,7,8], 23)
