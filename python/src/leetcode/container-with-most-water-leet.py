# https://leetcode.com/problems/container-with-most-water/
from typing import List

class Solution:

    # solution with O(n) compute complexity
    # we start at both ends (because this is the biggest width) and work our way to the center. If
    # there's a current hight bigger than the rest, we keep it as a possible index (either left ot right)
    # and move the other index towards the center. The algorithm is finished when the 2 indexes meet
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            if height[i] > height[j]:
                j -= 1
            else:
                i +=1

        return max_area

if __name__ == "__main__":
    s = Solution()

    def test(height: List[int], expected: int):
        actual:int = s.maxArea(height)
        print(f'Input: {str(height)}, expected: {expected}, actual: {actual}')

        assert expected == actual

    test([1,8,6,2,5,4,8,3,7], 49)
    test([1,1], 1)
