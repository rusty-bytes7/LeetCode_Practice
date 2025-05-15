def runningSum(self, nums):
        prefix = [nums[0]]
        for x in range (1,len(nums)):
            prefix.append(nums[x]+prefix[-1])
        return(prefix)