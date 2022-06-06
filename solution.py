class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_arr=[0]*len(nums)
        def Dpsum(a,nums):
            if a==0:
                max_sum_arr[a]=nums[a]
                return nums[a]
            else:
                max_sum_arr[a]=max(Dpsum(a-1,nums)+nums[a],nums[a])
                return max_sum_arr[a]
        x=Dpsum(len(nums)-1,nums)
        maxm=-99999
        for i in max_sum_arr:
            maxm=max(maxm,i)
        return maxm
