# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def add_el_to_list(self, list: Optional[ListNode], val) -> Optional[ListNode]:
        if not list:
            return ListNode(val)
        current = list
        while current.next != None:
            current = current.next
        current.next = ListNode(val)

        return list

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp_lists: list[Optional[ListNode]] = []
        for l in lists:
            tmp_lists.append(l)

        heap: list = []
        # process elements till there are elements left in the lists of lists
        result: Optional[ListNode] = None
        while True:
            should_break: bool = True
            for i in range(0, len(tmp_lists)):
                head: ListNode = tmp_lists[i]

                if head != None:
                    # the processing continues as till there is a with at least 1 element
                    should_break = False

                    # get the value and push it in the heap
                    heapq.heappush(heap, head.val)
                    # move the cursor to the next position of the current list
                    head = head.next
                    # update the list of lists with new list
                    tmp_lists[i] = head

            if should_break:
                break

        while (len(heap)>0):
            result = self.add_el_to_list(result, heapq.heappop(heap))

        return result


if __name__ == "__main__":
    s = Solution()

    def to_regular_list(l: ListNode) -> list:
        tmp = l
        res = []
        while tmp != None:
            res.append(tmp.val)
            tmp = tmp.next

        return res

    def test(input: list[list], expected: list):
        ll_input: list = []
        for l in input:
            ll: Optional[ListNode] = None
            for el in l:
                ll = s.add_el_to_list(ll, el)
            ll_input.append(ll)

        print(f"Input: {input}")

        result = s.mergeKLists(ll_input)

        res1 = to_regular_list(result)
        print(f"Expected: {expected}")
        print(f"Result: {res1}")

        assert res1 == expected


    test([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6])

    test([], [])