# https://leetcode.com/problems/integer-to-roman/
# medium difficulty - # 12

class Solution:

    def intToRoman(self, num: int) -> str:
        mapping = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        result = ""
        while(num > 0):
            for j in range(len(mapping)):
                max_value = mapping[j][0]
                if num >= max_value:
                    result += mapping[j][1]
                    num = num - max_value
                    break

        return result


if __name__ == "__main__":
    s: Solution = Solution()

    def test(num: int, expected: str):
        result: str = s.intToRoman(num)
        print(f"Result: {result}, expected: {expected}")

        assert result == expected


    test(3749, "MMMDCCXLIX")
    test(58, "LVIII")
    test(1994, "MCMXCIV")
    test(400, "CD")