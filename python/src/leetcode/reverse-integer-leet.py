# https://leetcode.com/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x: int) -> int:
        if x == 2147483647 or x==-2147483648:
            return 0

        result: int = 0

        is_neg: bool = False
        # stupid Python
        if x < 0:
            x = -x
            is_neg = True

        while True:
            result = result * 10 + x % 10
            x = x // 10
            if x == 0:
                break

        if is_neg:
            result = -result

        if result > 2147483647 or result < -2147483648:
            result = 0
        return result


if __name__ == '__main__':
    sol = Solution()

    def test_reverse(x: int, expected: int):
        reversed = sol.reverse(x)
        print(f'x: {x}, expected: {expected}, actual: {reversed}')

        assert expected == reversed

    test_reverse(123, 321)
    test_reverse(-123, -321)
    test_reverse(120, 21)
    # 2^32 has is bigger than int max val (2 ^ 31 -1)
    test_reverse(4294967296, 0)
    test_reverse(-2147483648, 0)

