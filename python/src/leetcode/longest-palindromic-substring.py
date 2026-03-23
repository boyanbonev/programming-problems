#https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:

    # Runtime: 204ms , Beats 93.33%
    # Memory: 19.22MB, Beats 85.56%


    def longestPalindrome(self, s: str) -> str:
        ls: int = len(s)
        if ls == 1:
            return s

        current_max_len: int = 0
        current_max_pal: str = ""
        for i in range(ls - 1):
            if i == ls - 1:
                break

            start = end = i

            # try to find the mid-point of a palindrome and start validation from there
            while start <= end:
                if end + 1 < ls and s[i] == s[end + 1]:
                    end = end + 1
                else:
                    while start - 1 >= 0 and end + 1 < ls and s[start - 1] == s[end + 1]:
                        start -= 1
                        end += 1

                    # there's no more palindrome after the current start and end
                    s1: str = s[start: end + 1]
                    ls1: int = len(s1)
                    if ls1 > current_max_len:
                        current_max_len = ls1
                        current_max_pal = s1
                    break

        return current_max_pal


if __name__ == "__main__":
    sol = Solution()

    def test(s: str, expected_output: str):
        print(f"s = {s}")
        result: str = sol.longestPalindrome(s)
        print(f"expected_output = {expected_output}")
        print(f"result = {result}")

        assert result == expected_output
        print("========================================================")

    test("a", "a")
    test("bb", "bb")
    test("ccc", "ccc")
    test("babad", "bab")# possible answer is "aba"
    test("cbbd", "bb")
    test("cccbbd", "ccc")
    test("cccabba", "abba")