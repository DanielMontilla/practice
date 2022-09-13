from typing import List

# My first solution... a bit bruteforce-ish
def twoSum_1(numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        for j in range(len(numbers) - i):
            i1 = i
            i2 = i + j
            if numbers[i1] + numbers[i2] == target and i1 != i2:
                return [i1 + 1, i2 + 1]


def twoSum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while numbers[l] + numbers[r] != target:
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

    return [l + 1, r + 1]

# Inputs:
numbers_1 = [2,7,11,15] 
target_1 = 9

numbers_2 = [2,3,4]
target_2 = 6

numbers_3 = [-1,0]
target_3 = -1

if __name__ == '__main__':
    res = twoSum(numbers_1, target_1)
    print(res)
