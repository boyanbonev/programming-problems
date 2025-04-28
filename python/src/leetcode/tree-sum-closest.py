# https://leetcode.com/problems/3sum-closest/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        num_len: int = len(nums)
        current_min: int = nums[0] + nums[1] + nums[2]
        for i in range(num_len - 1):
            start_index: int = i + 1
            end_index: int = num_len - 1
            while start_index < end_index:
                sum: int = nums[i] + nums[start_index] + nums[end_index]
                # keep only the min diff
                if abs(target - sum) <= abs(target - current_min):
                        current_min = sum

                if current_min == target:
                    return current_min

                if sum < target:
                    start_index += 1
                elif sum > target:
                    end_index -= 1
                else:
                    # skip the duplicates
                    while start_index < end_index and nums[start_index] == nums[start_index + 1]:
                        start_index += 1
                    while start_index < end_index and nums[end_index] == nums[end_index - 1]:
                        end_index -= 1

                    # update the indexes
                    start_index += 1
                    end_index -= 1

        return current_min

if __name__ == "__main__":
    s = Solution()

    def test(nums: List[int], target: int, expected_result: int):
        print(f"nums = {str(nums)}, target={target}")
        result: int = s.threeSumClosest(nums, target)
        print(f"expected_result = {str(expected_result)}")
        print(f"result = {str(result)}")

        print("========================================================")
        assert result == expected_result


    test([-1,2,1,-4], 1, 2)
    test([0,0,0], 1, 0)
    test([0,1,2], 3, 3)
    test([0,1,2], 0, 3)
    test([10,20,30,40,50,60,70,80,90], 1, 60)
    test([4,0,5,-5,3,3,0,-4,-5], -2, -2)