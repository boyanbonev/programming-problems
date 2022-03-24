from typing import List
import time

class Solution:

    def _calc_ones(self, num: int) -> int:
        bin_str = bin(num)
        cnt = 0
        for ch in bin_str:
            if ch == '1':
                cnt += 1

        return cnt

    def countBits(self, n: int) -> List[int]:
        result = list()
        for i in range(n + 1):
            result.append(self._calc_ones(i))

        return result


if __name__ == '__main__':
    s = Solution()
    num = 1000000
    start_time = time.time()
    result = s.countBits(num)
    end_time = time.time()
    # print(f'{num}: {result}')
    print(f'Calculating result for {num} took {end_time - start_time} seconds')