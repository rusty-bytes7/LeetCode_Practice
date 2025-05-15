def moveZeroes(self, nums):
        num_zeroes = 0
        if len(nums) == 1:
            return nums
        else: 
            for num in nums:
                if num == 0:
                    num_zeroes+=1
                    nums.remove(num)
                    nums.append(0)
        return(nums)
