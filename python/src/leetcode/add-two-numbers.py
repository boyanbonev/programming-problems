# https://leetcode.com/problems/add-two-numbers/
from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, value) -> ListNode:
        current = self
        while current.next != None:
            current = current.next

        current.next = ListNode(val = value)

        return self


    def __str__(self):
        res: str = "["
        head = self
        while head != None:
            res += str(head.val) + ("," if head.next else "")
            head = head.next

        return res + "]"


class Solution:

    def add(self, head: Optional[ListNode], value) -> Optional[ListNode]:
        # empty list
        if not head:
            return ListNode(val = value)

        current = head
        while current.next != None:
            current = current.next

        current.next = ListNode(val = value)

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        l2_head = l2

        result: ListNode | None = None

        should_run: bool = True
        remainder: int = 0
        sum: int = 0
        while should_run:
            sum = remainder
            should_run = False
            if l1_head:
                should_run = True
                sum += l1_head.val
                l1_head = l1_head.next

            if l2_head:
                should_run = True
                sum += l2_head.val
                l2_head = l2_head.next

            if should_run:
                result = self.add(result, sum % 10)
                remainder = sum // 10

        if remainder > 0:
            result = self.add(result, remainder)

        return result if result else ListNode(0)


if __name__ == "__main__":
    s = Solution()

    def test(l1: Optional[ListNode], l2: Optional[ListNode], expected_result: str):
        print(f"l1 = {l1}, l2 = {l2}")
        result: Optional[ListNode] = s.addTwoNumbers(l1, l2)
        print(f"expected_result = {str(expected_result)}")
        result_str = str(result)
        print(f"result = {result_str}")

        assert result_str == expected_result
        print("========================================================")


    #### TEST 1 ####
    l1: ListNode  = ListNode(2).add(4).add(3)
    l2: ListNode = ListNode(5).add(6).add(4)
    test(l1, l2, "[7,0,8]")

    #### TEST 2 ####
    l1 = ListNode(0)
    l2 = ListNode(0)
    test(l1, l2, "[0]")

    #### TEST 3 ####
    l1  = ListNode(9).add(9).add(9).add(9).add(9).add(9).add(9)
    l2 = ListNode(9).add(9).add(9).add(9)
    test(l1, l2, "[8,9,9,9,0,0,0,1]")

    #### TEST 4 ####
    # [1,6,0,3,3,6,7,2,0,1]
    l1  = ListNode(1).add(6).add(0).add(3).add(3).add(6).add(7).add(2).add(0).add(1)
    # [6,3,0,8,9,6,6,9,6,1]
    l2 = ListNode(6).add(3).add(0).add(8).add(9).add(6).add(6).add(9).add(6).add(1)
    test(l1, l2, "[7,9,0,1,3,3,4,2,7,2]")