def findMiddleIndex(self, nums):
        #build prefix sum
        prefix = [nums[0]]
        for num in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[num])

        #define left and right
        for p in range(len(prefix)):
            #this gives the zero
            if p == 0:
                left = 0
            else: left = prefix[p-1]
            right = prefix[-1]-prefix[p]
            
            if left == right:
                return(p)
        return(-1)