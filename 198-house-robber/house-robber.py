class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        
        def knapsack(n) -> int:
            if n==1:
                return nums[0]
            if n==2:
                return max(nums[0],nums[1])
            return max(knapsack(n-1),nums[n-1]+knapsack(n-2))   

        return knapsack(n)    