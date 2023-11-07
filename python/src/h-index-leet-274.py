# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:

    # see wikipedia definition of how to calc the h-index properly - https://en.wikipedia.org/wiki/H-index
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)

        for index, citation in enumerate(citations):
            if index >= citation:
                return index

        return len(citations)


if __name__ == "__main__":
    sol = Solution()

    def test(citations: List[int], exptected_h_index: int):
        print("=========================================================")
        print(f"Citations: {citations}")
        h_index = sol.hIndex(citations)

        print(f"Expected h_index={exptected_h_index}")
        print(f"h_index={h_index}")

        assert exptected_h_index == h_index



    test([3,0,6,1,5], 3)
    test([1,3,1], 1)
    test([9,7,6,2,1], 3)
    test([0], 0)
    test([1,1], 1)
