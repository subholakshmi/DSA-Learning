from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        result = 0  # Initialize result before using it

        # Count pairs (a, b) such that a * b is the same
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Calculate the number of valid tuples
        for count in product_count.values():
            if count > 1:
                result += (count * (count - 1) // 2) * 8  # Each pair can form 8 valid permutations

        return result  # Ensure result is returned at the end
