class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numMap = {}

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] = numMap[num] + 1
        
        
        klist = sorted(numMap.items(), key=lambda keyvalue: -keyvalue[1])
        
        index = 0
        sliceList = []
        while index < k:
            sliceList.append(klist[index][0])
            index = index + 1
        
        return sliceList




        