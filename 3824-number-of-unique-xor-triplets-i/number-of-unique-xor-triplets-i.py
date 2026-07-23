class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base cases where we can't form a 0
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # For n >= 3, the answer is just the next power of 2!
        # .bit_length() gets the number of bits in 'n'. 
        # (e.g., if n=4 (100), bit_length is 3. 1 << 3 equals 8).
        return 1 << n.bit_length()