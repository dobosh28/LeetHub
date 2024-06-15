class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                # Calculate the increment needed
                increment = nums[i - 1] - nums[i] + 1
                # Apply the increment
                nums[i] += increment
                # Accumulate the moves
                moves += increment
        
        return moves