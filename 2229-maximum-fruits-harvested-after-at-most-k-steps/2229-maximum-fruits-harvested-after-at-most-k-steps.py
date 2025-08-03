import math
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        positions = [fruit[0] for fruit in fruits]
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + fruits[i][1]

        max_fruits = 0
        left = 0
        for right in range(n):
            pos_l, pos_r = positions[left], positions[right]
            
            cost = (pos_r - pos_l) + min(abs(startPos - pos_l), abs(startPos - pos_r))

            while left <= right and cost > k:
                left += 1
                if left > right:
                    break
                pos_l, pos_r = positions[left], positions[right]
                cost = (pos_r - pos_l) + min(abs(startPos - pos_l), abs(startPos - pos_r))

            if left <= right:
                current_fruits = prefix_sum[right + 1] - prefix_sum[left]
                max_fruits = max(max_fruits, current_fruits)
                
        return max_fruits
