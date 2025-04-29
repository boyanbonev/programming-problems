# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def __init__(self):
        self.digit2letter = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }

    def calculate_cartesian_product(self, list1: list[str], list2: list[str]) -> list[str]:
        result: list[str] = []
        for ch1 in list1:
            for ch2 in list2:
                result.append(ch1 + ch2)

        return result

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        inp_lists = []
        for digit in digits:
            inp_lists.append(self.digit2letter[digit])

        result: list[str] = inp_lists[0]
        for i in range(1, len(inp_lists)):
            result = self.calculate_cartesian_product(result, inp_lists[i])

        return result

    # uses itertools.product
    def letterCombinationsWithItertoolsProduct(self, digits: str) -> List[str]:
        if not digits:
            return []
        import itertools
        inp_lists = []
        for digit in digits:
            inp_lists.append(self.digit2letter[digit])

        return ["".join(prd_tuple) for prd_tuple in itertools.product(*inp_lists)]

if __name__ == "__main__":
    s = Solution()

    def test(digits: int, expected_result: int):
        print(f"digits = {str(digits)}\nexpected_result = {expected_result}")
        result = s.letterCombinations(digits)
        print(f"result          = {str(result)}")

        print("========================================================")
        assert result == expected_result
        print("Test - OK")

    test("", [])
    test("2", ["a", "b", "c"])
    test("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"])