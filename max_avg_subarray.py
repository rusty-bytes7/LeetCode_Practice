def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])

        totalsum = 0
        for i in range(k):
            totalsum += nums[i]

        #initialize maximum sum
        maxsum = totalsum

        #start the sliding window
        startindex = 0
        endindex = k
        while endindex < len(nums):
            totalsum -= nums[startindex]
            startindex += 1
            totalsum += nums[endindex]
            endindex += 1
            maxsum  = max(maxsum,totalsum)
       
        return(maxsum/k)