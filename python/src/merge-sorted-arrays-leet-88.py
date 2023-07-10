# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i: int = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)


if __name__ == "__main__":
    sol: Solution = Solution()

    def test(nums, val, expected_nums, expected_num_diff_el):
        print("-------------------------------------")
        print("Input   : " + str(nums) + " val=" + str(val))

        diff_el = sol.removeElement(nums, val)

        print("Output  : " + str(nums))
        print("Expected: " + str(expected_nums))

        assert len(nums) == len(expected_nums)

        print(f"Num diff elements = {diff_el}, expected = {expected_num_diff_el}")
        assert diff_el == expected_num_diff_el

        nums = sorted(nums)
        expected_nums = sorted(expected_nums)

        for i in range(len(nums) - 1):
            assert nums[i] == expected_nums[i]


test([3,2,2,3], 3, [2,2], 2)
test([0,1,2,2,3,0,4,2], 2, [0,1,4,0,3], 5)