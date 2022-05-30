from typing import List


# first solution
# def threeSum(nums: List[int]) -> List[List[int]]:
#     indices = {}
#     res = []

#     # construct indices dict
#     for i in range(len(nums)):
#         n = nums[i]
#         if n in indices:
#             indices[n].append(i)
#         else:
#             indices[n] = [i]

#     # generate combinations and check sum
#     for i in range(len(nums)):
#         ai = i
#         for j in range(len(nums) - i):
#             bi = i + j

#             a = nums[ai]
#             b = nums[bi]

#             sum = a + b

#             if -sum in indices:
#                 for ci in indices[-sum]:
#                     if ci != ai and ci != bi:
#                         c = nums[ci]
#                         res.append([a, b, c])

#     return res

def threeSum(nums: List[int]) -> List[List[int]]:
    pass
