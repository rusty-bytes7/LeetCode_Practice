#given an array of integers and an integer k, find the maximum average of all contiguous subarrays of size k in the array.
# The average of a contiguous subarray is the sum of its elements divided by k.

nums = [1,2,56,-3,-7,-35,3,4,5,-7,50,35,1,2,5,3,1,6,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,67,81,]
k=6
def find_max_avg(nums,k):
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
    print("The maximum average is ", maxsum/k)

nums2 = [1,12,-5,-6,50,3]
k2 = 4

find_max_avg(nums2,k2)

