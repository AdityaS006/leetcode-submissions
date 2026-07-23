class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum={0:1}
        currentsum=0
        count=0
        for num in nums:
            currentsum+=num
            target=currentsum-k
            if target in prefixsum:
                count += prefixsum[target]
            if currentsum in prefixsum:
                prefixsum[currentsum]+=1
            else:
                prefixsum[currentsum]=1
            
        return count
            