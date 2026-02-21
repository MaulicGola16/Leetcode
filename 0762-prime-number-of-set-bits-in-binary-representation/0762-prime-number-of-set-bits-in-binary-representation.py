class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        return sum(665772>>v.bit_count()&1 for v in range(l,r+1))