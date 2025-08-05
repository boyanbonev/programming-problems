# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def gen_nth_parenthesis(self, l_cnt: int, r_cnt:int, n: int, current_comb: str, result: list[str]) -> list[str]:
        if l_cnt > n or r_cnt > n:
            return result
        elif l_cnt == n and r_cnt == n:
            result.append(current_comb)
            return result
        if l_cnt < n:
            self.gen_nth_parenthesis(l_cnt + 1, r_cnt, n, current_comb + "(", result)
        if r_cnt < n and l_cnt > r_cnt:
            self.gen_nth_parenthesis(l_cnt, r_cnt + 1, n, current_comb + ")", result)

        return result

    def generateParenthesis(self, n: int) -> List[str]:
        return self.gen_nth_parenthesis(0, 0, n, "", list())


if __name__ == "__main__":
    s: Solution = Solution()

    def test(n: int, expected: list[str]):
        expected = sorted(expected)
        print("================================================")
        print(f"n={n}, expected = {expected}")
        result: list[str] = s.generateParenthesis(n)
        result = sorted(result)
        print(f"n={n}, result   = {result}")

        assert result == expected


    test(1, ["()"])
    test(2, ["(())", "()()"])
    test(3, ["((()))","(()())","(())()","()(())","()()()"])
    test(4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])