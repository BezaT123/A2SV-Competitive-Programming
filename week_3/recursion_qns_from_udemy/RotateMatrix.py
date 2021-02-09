from typing import List


def rotateMatrix(nums):
    arr = nums
    for i in range(len(nums)):
        for j in range(len(nums)):
            arr[j][i] = nums[i][j]
            print(i,j, nums[i][j], arr[i][j])
    return arr


print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))