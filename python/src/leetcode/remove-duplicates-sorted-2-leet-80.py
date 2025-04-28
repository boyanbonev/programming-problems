# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i: int = 0
        total_deletion_cnt: int = 0
        while i < len(nums) - 1:
            current_num: int = nums[i]
            i += 1
            duplication_cnt: int = 0
            while i < len(nums) and current_num == nums[i]:
                duplication_cnt += 1
                if duplication_cnt > 1:
                    del nums[i]
                    total_deletion_cnt += 1
                else:
                    i += 1

        res = len(nums)
        for i in range(total_deletion_cnt):
            nums.append("_")

        return res

if __name__ == "__main__":
    sol: Solution = Solution()

    def test(nums: List[int], expected_nums: List[int], expected_res: int):
        print("-------------------------------------")
        print("Input      : " + str(nums))

        res = sol.removeDuplicates(nums)

        print("Expected   : " + str(expected_nums))
        print("Result     : " + str(nums))

        assert res == expected_res

        for i in range(expected_res):
            assert nums[i] == expected_nums[i]


    test([1,1,1,2,2,3], [1,1,2,2,3,"_"], 5)
    test([0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3,"_","_"], 7)