def twoSum(self, nums, target):
        nums2 = sorted(nums)
        left = 0
        right = len(nums2)-1
        while left < right:
            current = nums2[left] + nums2[right]
            #if we find a solution we need to get the ORIGINAL indices back
            if current == target:
                #get numbers
                val1 = nums2[left]
                val2 = nums2[right]

                #find index of first number
                first = nums.index(val1)

                if val1 != val2:
                    second = nums.index(val2)
                #if they're equal we don't want the same index given b/c index returns first instance
                else:
                    for i in range(len(nums)):
                        if nums[i] == val2 and i != first:
                            second = i
                            break

                return (first, second)

            elif current < target:
                left += 1
            elif current > target:
                right -= 1