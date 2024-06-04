class Solution:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        prime_indices = [i for i, num in enumerate(nums) if Solution.is_prime(num)]
        
        if len(prime_indices) < 2:
            return 0
    
        return prime_indices[-1] - prime_indices[0]


