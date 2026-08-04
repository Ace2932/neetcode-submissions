class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, num in enumerate(nums):
            neededNum = target - num
            if (neededNum in numMap):
                return [numMap.get(neededNum), index]
            numMap[num] = index
            

            
            # if (numMap.get(neededNum) != numMap.get(num)):
            #     return [numMap.get(neededNum), index]

        