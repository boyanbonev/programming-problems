from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def _add_to_list(self, list: ListNode, val) -> ListNode:
        if not list:
            return ListNode(val)
        current = list
        while current.next != None:
            current = current.next
        current.next = ListNode(val)

        return list


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2

        if not l2:
            return l1

        l1_current = l1
        l2_current = l2
        result = None
        residue = 0

        while l1_current != None or l2_current != None:
            l1_val = l1_current.val if l1_current else 0
            l2_val = l2_current.val if l2_current else 0

            sum = l1_val + l2_val + residue
            val = sum % 10
            residue = sum // 10

            result = self._add_to_list(result, val)

            l1_current = l1_current.next if l1_current else None
            l2_current = l2_current.next if l2_current else None

        if residue != 0:
            result = self._add_to_list(result, residue)

        return result

def print_list(l: ListNode):
    tmp = l
    str = ''
    while tmp != None:
        str += f'{tmp.val}, '
        tmp = tmp.next

    print(str)

if __name__ == '__main__':
    s = Solution()
    # l1 = s._add_to_list(None, 2)
    # s._add_to_list(l1, 4)
    # s._add_to_list(l1, 3)
    # s._add_to_list(l1, 1)

    # l2 = s._add_to_list(None, 5)
    # s._add_to_list(l2, 6)
    # s._add_to_list(l2, 4)

    l1 = s._add_to_list(None, 9)
    s._add_to_list(l1, 9)
    s._add_to_list(l1, 9)
    s._add_to_list(l1, 9)
    s._add_to_list(l1, 9)
    s._add_to_list(l1, 9)
    s._add_to_list(l1, 9)

    l2 = s._add_to_list(None, 9)
    s._add_to_list(l2, 9)
    s._add_to_list(l2, 9)
    s._add_to_list(l2, 9)

    print_list(l1)
    print('+')
    print_list(l2)

    result = s.addTwoNumbers(l1, l2)
    print_list(result)