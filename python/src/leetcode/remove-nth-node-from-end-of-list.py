# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first: ListNode | None = head
        cnt: int = 0
        # we want to stop before the needed element so that we can skip it. There for we must do up to n - 1 steps: n - 1 > 0
        while first != None and cnt < n:
            first = first.next
            cnt += 1

        # we have reached the end of the list -> remove the first element of the list
        if not first:
            if cnt > 1:
                return head.next
            else:
                return None

        second: ListNode = head
        while first.next != None:
            first = first.next
            second = second.next

        # skip the N-th to the last element
        second.next = second.next.next

        return head


    def add(self, head: Optional[ListNode], value) -> Optional[ListNode]:
        # empty list
        if not head:
            return ListNode(val = value)

        current = head
        while current.next != None:
            current = current.next

        current.next = ListNode(val = value)

        return head


    def to_str(self, head: Optional[ListNode]):
        res: str = "["
        while head != None:
            res += str(head.val) + ", "
            head = head.next

        return res + "]"

if __name__ == "__main__":
    s = Solution()

    def test(head: Optional[ListNode], n, expected_result: str):
        print(f"head = {s.to_str(head)}, n = {n}")
        result: Optional[ListNode] = s.removeNthFromEnd(head, n)
        print(f"expected_result = {str(expected_result)}")
        result_str = s.to_str(result)
        print(f"result = {result_str}")

        assert result_str == expected_result
        print("========================================================")


    #### TEST 1 ####
    head: ListNode| None = s.add(None, 1)
    test(head, 1, "[]")

    # #### TEST 2 ####
    head = s.add(None, 1)
    for i in range(2, 6):
        s.add(head, i)
    test(head, 2, "[1, 2, 3, 5, ]")

    #### TEST 3 ####
    head: ListNode = s.add(None, 1)
    s.add(head, 2)
    test(head, 2, "[2, ]")