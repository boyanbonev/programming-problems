# Given on a Meta interview on 21.06.2024
# Find which building has ocean view (There's no other building higher than the current)
#
# //   ___
# // 4 |  |  ___         ___
# // 3 |  |  |  |  ___   |  |
# // 2 |  |  |  |  |  |  |  |  ___
# // 1 |  |  |  |  |  |  |  |  |  |
# //                               ~~~~~ Ocean
# //    b0,   b1,   b2,   b3,   b4
# // outcome --> [0, 3, 4]

def calculate_ocean_views(arr: list) -> list:
    max_high: int = 0
    ocean_views = []
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_high:
            ocean_views.append(i)
            max_high = arr[i]

    return ocean_views

def arrays_equal(l1: list, l2: list) -> bool:
    len1: int = len(l1)
    len2: int = len(l2)
    if len1 != len2:
        return False

    for i in range(len1):
        if l1[i] != l2[i]:
            return False

    return True

if __name__ == "__main__":
    arr = [4, 3, 2, 3, 1]
    expected = [4, 3, 0]
    result = calculate_ocean_views(arr)
    print(f"expected = {expected}")
    print(f"result   = {result}")

    assert arrays_equal(result, expected)
    print("The result is OK!")