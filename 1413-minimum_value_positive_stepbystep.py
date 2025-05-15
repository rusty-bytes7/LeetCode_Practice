def minStartValue(self, nums):
        
        startval = 1
        prefix =nums[0]
        
        while True:

            total = startval
            isvalid = True

            for num in nums:
                total +=  num
            
                if total <1:
                    isvalid = False
                    break
            if isvalid == True:
                return(startval)
            else:
                startval += 1
            