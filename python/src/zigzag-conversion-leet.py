# https://leetcode.com/problems/zigzag-conversion/

class Solution:

    def convert(self, s: str, numRows: int) -> str:
        chars = list(s)
        l = len(s)
        s = None

        arr = []
        for _ in range(0, numRows):
            arr.append('')

        go_down: bool = True
        i: int = 0
        for pos in range(0, l):
            arr[i] += chars[pos]
            if i == numRows - 1:
                go_down = False
            if go_down:
                # last row follows
                if i >= numRows - 2:
                    go_down = False
                i += 1
            else:
                if i <= 1:
                    go_down = True
                i -= 1

        return self.get_result_string(arr, numRows)

    def get_result_string(self, arr, numRows: int) -> str:
        result: str = ''
        for i in range(0, numRows):
            if arr[i]:
                result += arr[i]
        return result

if __name__ == '__main__':
    sol = Solution()

    def test_sol(s, numRows, expected_output):
        res = sol.convert(s, numRows)
        print(f'Converted: {res}')
        assert res == expected_output

    test_sol('A', 2, 'A')
    test_sol('AB', 1, 'AB')
    test_sol('ABC', 3, 'ABC')
    test_sol('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')
    test_sol('PAYPALISHIRING', 4, 'PINALSIGYAHRPI')