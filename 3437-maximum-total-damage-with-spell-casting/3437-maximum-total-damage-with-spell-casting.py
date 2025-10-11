class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        freq = {}
        unique = []
        
        for num in power:
            freq[num] = freq.get(num, 0) + 1
            if len(unique) == 0 or unique[-1] != num:
                unique.append(num)

        n = len(unique)
        dp = [0] * n
        dp[0] = unique[0] * freq[unique[0]]

        for i in range(1, n):
            damage = unique[i]
            dp[i] = max(dp[i - 1], damage * freq[damage])
            
            if unique[i] - unique[i - 1] > 2:
                dp[i] = max(dp[i], dp[i - 1] + damage * freq[damage])
            elif i - 2 >= 0 and unique[i] - unique[i - 2] > 2:
                dp[i] = max(dp[i], dp[i - 2] + damage * freq[damage])
            elif i - 3 >= 0:
                dp[i] = max(dp[i], dp[i - 3] + damage * freq[damage])
        
        return dp[-1]