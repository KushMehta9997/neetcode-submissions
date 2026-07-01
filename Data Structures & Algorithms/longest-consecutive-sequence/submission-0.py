class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 1. Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # 2. Check if 'num' is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # 3. Count how far the sequence goes
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # 4. Keep track of the maximum length found
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak