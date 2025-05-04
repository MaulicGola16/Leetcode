from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes):
        count_map = defaultdict(int)
        count = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            count += count_map[key]
            count_map[key] += 1
        return count