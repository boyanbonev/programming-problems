from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sorted_nums = sorted(nums)
        for i in range(0, len(nums)):
            num = nums[i]
            remainder = target - num
            reminder_index = self.find_reminder_index_linear(nums, remainder, i)
            if reminder_index > 0 and reminder_index != i:
                return [i, reminder_index]

        # no result
        return[-1, -1]

    def find_reminder_index_linear(self, arr, reminder, current_pos):
        for i in range(0, len(arr)):
            if arr[i] == reminder and i != current_pos:
                return i
        return -1

    # def find_reminder_index(self, arr, start, end, reminder):
    #     if start > end:
    #         return -1

    #     mid_idx = (start + end) // 2
    #     mid_elem = arr[mid_idx]
    #     if mid_elem == reminder:
    #         return mid_idx

    #     if mid_elem < reminder:
    #         # search to the right
    #         return self.find_reminder_index(arr, mid_idx + 1, end, reminder)
    #     else:
    #         # search to the left
    #         return self.find_reminder_index(arr, start, mid_idx - 1, reminder)


s = Solution()
arr = [3,3]
arr = s.twoSum(arr, 6)
print(f'Result {arr}')