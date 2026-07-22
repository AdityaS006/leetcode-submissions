class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 1. Setup the initial window
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        max_vowels = current_vowels
        
        # 2. Slide the window
        for right in range(k, len(s)):
            # Add the incoming character
            if s[right] in vowels:
                current_vowels += 1
                
            # Subtract the outgoing character
            # The character falling out is exactly 'k' steps behind 'right'
            left = right - k 
            if s[left] in vowels:
                current_vowels -= 1
                
            # Update the max
            max_vowels = max(max_vowels, current_vowels)
            
        return max_vowels