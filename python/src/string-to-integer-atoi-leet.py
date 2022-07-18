# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        l = len(s)
        pos = 0

        while pos < l and s[pos] == ' ':
            pos += 1

        if pos == l:
            return 0

        sign = '+'
        if s[pos] in ['+', '-']:
            sign = s[pos]
            pos += 1

        result = ''
        while pos < l and s[pos].isdigit():
            result += s[pos]
            pos += 1

        if not result:
            return 0

        num: int = int(sign + result)
        if num < -2147483648:
            num = -2147483648
        elif num > 2147483647:
            num = 2147483647

        return num


if __name__ == '__main__':
    sol = Solution()

    def test_atoi(inp_str: str, expected: int):
        result: int = sol.myAtoi(inp_str)
        print(f'inp_str={inp_str}, parsed={result}, expected={expected}')
        assert expected == result

    test_atoi('1', 1)
    test_atoi('42', 42)
    test_atoi('   -42', -42)
    test_atoi('4193 with words', 4193)
    test_atoi('+1 ', 1)
    test_atoi('words and 987', 0)
    test_atoi('-91283472332', -2147483648)
    test_atoi('91283472332', 2147483647)
    test_atoi('+-12', 0)
    test_atoi('00000-42a1234', 0)
    test_atoi('   +0 123', 0)
    test_atoi('0  123', 0)
    test_atoi('    -88827   5655  U', -88827)



