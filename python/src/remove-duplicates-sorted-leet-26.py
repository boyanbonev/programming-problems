# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i: int = 0
        while i < len(nums) - 1:
            el = nums[i]
            i += 1
            while i < len(nums) and el == nums[i]:
                del nums[i]

        return len(nums)

if __name__ == "__main__":
    sol: Solution = Solution()

    def test(nums: List[int], expected_nums: List[int]):
        print("-------------------------------------")
        print("Input      : " + str(nums))

        res = sol.removeDuplicates(nums)

        print("Expected   : " + str(expected_nums))
        print("Result     : " + str(nums))

        assert res == len(expected_nums)

        for i in range(len(nums)):
            assert nums[i] == expected_nums[i]


    test([1,1,2], [1,2])
    test([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4])

