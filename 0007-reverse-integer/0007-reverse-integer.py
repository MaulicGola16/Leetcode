class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign

        reversed_x = 0
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        reversed_x *= sign

        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
print(solution.reverse(0))
        