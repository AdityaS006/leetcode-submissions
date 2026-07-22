class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store {number_we_have_seen: its_index}
        seen_map = {} 
        
        for i in range(len(nums)):
            current_number = nums[i]
            
            # The exact number we need to find to hit the target
            needed_number = target - current_number
            
            # If we've seen the needed number before, we found our pair!
            if needed_number in seen_map:
                # Return the index of the needed number, and our current index
                return [seen_map[needed_number], i]
            
            # If not, log the current number and its index into the map for the future
            seen_map[current_number] = i
            
        return []