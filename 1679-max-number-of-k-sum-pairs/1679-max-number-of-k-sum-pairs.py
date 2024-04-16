class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = {}
        max_operations = 0
    
        for num in nums:
            complement = k - num
            if num_count.get(complement, 0) > 0:
                max_operations += 1
                num_count[complement] -= 1
            else:
                num_count[num] = num_count.get(num, 0) + 1
        return max_operations
