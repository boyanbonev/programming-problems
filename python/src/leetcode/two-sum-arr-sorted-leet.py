from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            num = nums[i]
            remainder = target - num
            reminder_index = self.find_reminder_index_binary_search(nums, 0, len(nums), remainder, i)
            if reminder_index > 0 and reminder_index != i:
                return [i + 1, reminder_index + 1]

        # no result
        return[-1, -1]

    def find_reminder_index_binary_search(self, arr, start, end, reminder, current_idx):
        if start >= end:
            return -1

        mid_idx = (start + end) // 2
        mid_elem = arr[mid_idx]
        if mid_elem == reminder and mid_idx != current_idx:
            return mid_idx

        if mid_elem <= reminder:
            # search to the right
            return self.find_reminder_index_binary_search(arr, mid_idx + 1, end, reminder, current_idx)
        else:
            # search to the left
            return self.find_reminder_index_binary_search(arr, start, mid_idx, reminder, current_idx)


s = Solution()
arr = [0,0,1,3]
arr = s.twoSum(arr, 0)
print(f'Result {arr}')