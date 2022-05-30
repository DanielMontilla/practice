from typing import List

# My first solution... a bit bruteforce-ish
# def twoSum(numbers: List[int], target: int) -> List[int]:
#     for i in range(len(numbers)):
#         for j in range(len(numbers) - i):
#             i1 = i
#             i2 = i + j
#             if numbers[i1] + numbers[i2] == target and i1 != i2:
#                 return [i1 + 1, i2 + 1]


def twoSum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while numbers[l] + numbers[r] != target:
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

    return [l + 1, r + 1]
