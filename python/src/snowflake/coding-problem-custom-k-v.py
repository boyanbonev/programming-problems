# Design a key value store with the capability to store multiple timestamped versions per key
#  —   T=5 A=hello   ———  T=6 B=Snowflake ——    T=8 A=world  ->

from typing import Dict, Tuple

class CustomKeyValueMap():
    # key, (version, value)

    # get(key, version) -> value
    # get(key) -> value # the latest in the list
    # get_all(key) -> List[Tuple(version,value)

    # add(key, value, version):
    # add(key, value): # current ver + 1

    # delete(key, version) -> value
    # delete(key) -> List[Tuple(version, value)]

    _map: Dict[str, list[Tuple[int, str]]]

    def __init__(_self):
        _self._map = dict()

    # def _get_value_by_version_recursion(_self, versions: list[Tuple[int, str]], version: int, l: int, r: int) -> str:
    #     mid: int = (l + r) // 2
    #     mid_elem: Tuple[int, str] = versions[mid]

    #     if mid_elem[0] == version or l >= r:
    #         return mid_elem[1]
    #     elif mid_elem[0] > version:
    #         # left side of mid point
    #         return _self._get_value_by_version(versions, version, l=l, r=mid - 1)
    #     else:
    #         # right side of mid point
    #         return _self._get_value_by_version(versions, version, l=mid + 1, r=r)


    # iterative binary search. It is assumed that the versions are sorted
    def _get_value_by_version(_self, versions: list[Tuple[int, str]], version: int) -> str:
        l: int = 0
        r: int = len(versions)

        while l < r:
            mid: int = (l + r) // 2
            mid_element = versions[mid]
            if version == mid_element[0]:
                return mid_element[1]
            elif version < mid_element[0]:
                r = mid
            else:
                l = mid + 1

        # l==r==mid==len(versions) - 1
        # return the previous available version
        return versions[l - 1][1]


    # iterative binary search insert into ther right position. The versions should always be properly sorted
    def _insert_in_place(_self, versions: list[Tuple[int, str]], version: int, value: str):
        l: int = 0
        r: int = len(versions)

        while l < r:
            mid: int = (l + r) // 2
            mid_element = versions[mid]
            if version == mid_element[0]:
                # override it if there's already such an element
                versions[mid] = (version, value)
                return
            elif version < mid_element[0]:
                r = mid
            else:
                l = mid + 1

        versions.insert(l, (version, value))

    def __str__(_self) -> str:
        result: str = "CustomKeyValueMap:\n"
        for key, versions in _self._map.items():
            result += " " + key + ": ["
            for version_value in versions:
                result += str(version_value) + "; "
            result += "]\n"
        return result


    def get(_self, key: str, version: int) -> str:
        if not key:
            raise Exception(f"Wrong key={key}. The key should be neither null, nor empty string.")

        versions: list[Tuple[int, str]] = _self._map[key]
        return _self._get_value_by_version(versions, version)


    def add(_self, key: str, version: int, value: str):
        if not key:
            raise Exception(f"Wrong key={key}. The key should be neither null, nor empty string.")

        if key not in _self._map:
            _self._map[key] = [(version, value)]
            return

        _self._insert_in_place(_self._map[key], version, value)


if __name__ == "__main__":

    def run_test_get(key: str, version: int, expected: str):

        print("*****************************************************************")
        print(f"Running test: key={key}, version={version}, expected={expected}")

        custom_map: CustomKeyValueMap = CustomKeyValueMap()

        # setup
        custom_dict: dict = dict()
        versions_a: list[Tuple[int, str]] = list()
        versions_a.append((5, "hello"))
        versions_a.append((6, "six"))
        versions_a.append((9, "world"))

        custom_dict["A"] = versions_a

        versions_b: list[Tuple[int, str]] = list()
        versions_b.append((6, "snow"))
        custom_dict["B"] = versions_b
        custom_map._map = custom_dict

        # perform test
        print(str(custom_map))
        ret_val: str = custom_map.get(key, version)
        print(f"ret_val={ret_val}")

        assert ret_val == expected

    def run_test_add():
        custom_map: CustomKeyValueMap = CustomKeyValueMap()
        custom_map.add("A", 3, "a3")
        custom_map.add("A", 5, "a5")
        custom_map.add("A", 4, "a4")
        custom_map.add("A", 8, "a8")
        custom_map.add("A", 9, "a9")
        custom_map.add("A", 6, "a6")
        custom_map.add("A", 1, "a1")
        # the duplicate should be overridden
        custom_map.add("A", 6, "a6-new")
        custom_map.add("A", 7, "a7")
        custom_map.add("A", 2, "a2")
        custom_map.add("C", 4, "c4")

        print(str(custom_map))

        versions: list[Tuple[int, str]] = custom_map._map["A"]
        versions_extracted: list[int] = [v[0] for v in versions]

        print(f"versions_extracted={versions_extracted}")

        assert versions_extracted == [i for i in range(1, 10)]


    run_test_add()

    run_test_get("A", 5, expected="hello")
    run_test_get("A", 9, expected="world")
    run_test_get("B", 6, expected="snow")
    run_test_get("A", 7, expected="six") # return the closest value to the left