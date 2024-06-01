class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
    
        xor_result = 0
        for num in nums:
            xor_result ^= num

        differentiating_bit = xor_result & -xor_result

        unique1, unique2 = 0, 0
        for num in nums:
            if num & differentiating_bit:
                unique1 ^= num
            else:
                unique2 ^= num

        return [unique1, unique2]
