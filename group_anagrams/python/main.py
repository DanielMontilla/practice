from typing import List

# https://leetcode.com/problems/group-anagrams


def groupAnagrams(strs: List[str]) -> List[List[str]]:

    def isAnagram(n: str, m: str):
        if len(n) != len(m):
            return False

        for letter in n:
            if letter in m:
                m = m.replace(letter, '', 1)
            else:
                return False

        return True

    arrs: List[List[str]] = [[]]

    for s in strs:
        for arr in arrs:
            if len(arr) == 0:
                arr.append(s)
                arrs.append([])
                break
            elif isAnagram(s, arr[0]):
                arr.append(s)
                break

    arrs.pop()

    return arrs


# Notes:
""""
    Runtime: 9643 ms, faster than 5.03% of Python3 online submissions for Group Anagrams.
    Memory Usage: 17.1 MB, less than 96.63% of Python3 online submissions for Group Anagrams.
    
    Very slow... but super memory efficient
"""

# Inputs:
strs_1 = ["eat","tea","tan","ate","nat","bat"]
strs_2 = [""]
strs_3 = ["a"]

if __name__ == '__main__':
    res = groupAnagrams(strs_1)
    print(res)