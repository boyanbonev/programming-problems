# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0
        num1_len = len(nums1)
        num2_len = len(nums2)
        r = max(num1_len, num2_len)

        left_el = 0
        right_el = 0

        while l < r:
            # take the bigger element for the left index and smaller - for the right
            if nums1[l] < nums2[l]:
                left_el = nums2[l]
            else:
                left_el = nums1[l]

            l += 1

            if l>=r:
                break

            if nums1[num1_len - r - 1] < nums2[num2_len - r - 1]:
                right_el = nums2[num2_len - r - 1]
            else:
                right_el = nums1[num1_len - r - 1]

            r -= 1

        print(f"left_el={left_el}, right_el={right_el}")
        return (left_el + right_el) / 2




if __name__ == "__main__":
    sol: Solution = Solution()

    def test(nums1: List[int], nums2: List[int], expected: float) -> None:
        print("-------------------------------------")
        print("Input   : " + str(nums1) + " val=" + str(nums2))

        result: float = sol.findMedianSortedArrays(nums1, nums2)

        print("result  : " + str(result))
        print("expected: " + str(expected))

        assert result == expected


    # test([1,3], [2], 2.0)
    # test([1,2], [3,4], 2.5)

    test([2,2,4,4], [2,2,2,4,4], 2)