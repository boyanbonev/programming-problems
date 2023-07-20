# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from typing import Dict, List


class Solution:

    # O(n)- speed, O(n) - memory
    def majorityElement(self, nums: List[int]) -> int:
        elems: Dict = {}
        n = len(nums)

        for element in nums:
            if element in elems:
                elems[element] += 1
                cur_count = elems[element]
                if cur_count > n/2:
                    return element
            else:
                elems[element] = 1

        max_count = 0
        max_elem = nums[0]
        for cur_elem, cur_count in elems.items():
            if cur_count > max_count:
                max_count = cur_count
                max_elem = cur_elem

        return max_elem

if __name__ == "__main__":

    sol: Solution = Solution()

    def test(nums: List[int], expected_max_majority_element: int):
        result = sol.majorityElement(nums)
        print("----------------------------------------------------")
        print("Result           : " + str(result))
        print("Expected result  : " + str(expected_max_majority_element))

        assert result == expected_max_majority_element

    test([6,5,5], 5)
    test([3,2,3], 3)
    test([2,2,1,1,1,2,2], 2)