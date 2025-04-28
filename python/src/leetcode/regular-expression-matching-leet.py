class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        elif p=="":
            return False
        else:
            print(f"s={s}, p={p}")

        s_index: int = 0
        p_index: int = 0

        while(s_index < len(s) and p_index < len(p)):
            s_ch: str = s[s_index]
            p_ch: str = p[p_index]
            if s_ch != p_ch:
                # check if  the next char is * - not
                if p_index < len(p) - 1 and p[p_index + 1] != "*":
                    # skip the any symbol
                    return p_ch == "."
                # if the different char is not a . and there's isn't a star after it - Fail
                elif p_ch == ".":
                    s_index += 1
                    p_index += 1
                elif p_ch == "*":
                    aaaa
                else:
                    # we have char followed by a start
                    new_p = remove_sequence(p, p_index, 1)
                    return self.isMatch(s, new_p)

            s_index += 1
            p_index += 1

        return True


def remove_sequence(string: str, index: int, length: int) -> str:
    return string[0 : index : ] + string[index + length : :]


if __name__ == "__main__":
    sol: Solution = Solution()
    assert sol.isMatch("aa", "a") == False
    assert sol.isMatch("aa", "a.") == True
    assert sol.isMatch("aa", "a*") == True
    # assert sol.isMatch("ab", ".*") == True
    # assert sol.isMatch("abab", ".*") == True
    # assert sol.isMatch("ab", "*") == False

    # assert sol.isMatch("aab", "c*a*b") == True
    # assert sol.isMatch( "aaa", "ab*ac*a") == True

    # assert sol.isMatch("ab", "b*") == False
    # assert sol.isMatch("ab", "x*") == False