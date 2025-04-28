# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:

    def rotate_not_memory_optimized(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        This impl is not memory optimized, but it is faster.
        """
        l: int = len(nums)
        if k > l:
            k = k % l
        tmp = nums[l - k: l]
        for j in range(l - k - 1, -1, -1):
            nums[j + k] = nums[j]

        for i in range(len(tmp)):
            nums[i] = tmp[i]


    def swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def rotate_section(self, nums: List[int], start: int, end: int) -> None:
        while(start < end):
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        l: len = len(nums)
        if k > l:
            k = k % l

        self.rotate_section(nums, 0, l - k - 1)
        self.rotate_section(nums, l - k, l - 1)
        self.rotate_section(nums, 0, l - 1)

if __name__ == "__main__":
    sol = Solution()

    def test(nums: List[int], k: int, expected: List[int]):
        print("=======================================================================")
        print(f"Input:        {str(nums)} ; k={k}")

        sol.rotate(nums, k)
        print(f"Expected:     {str(expected)}")
        print("------------------------------------")
        print(f"Output:       {str(nums)}")
        print("------------------------------------")

        assert len(expected) == len(nums)

        for i in range(len(expected)):
            assert expected[i] == nums[i]



    test([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4])
    test([-1,-100,3,99], 2, [3,99,-1,-100])
    test([-1], 2, [-1])
    test([1,2], 3, [2,1])