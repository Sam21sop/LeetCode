class Solution:
    def climbStairs(self, n: int) -> int:
        # If there are 1 or 2 steps, there are exactly 1 and 2 ways to climb, respectively.
        if n <= 2:
            return n

        ways = [0] * (n + 1)

        # Base case
        ways[1] = 1
        ways[2] = 2

        # bottom-up approach
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]
    

    
if __name__ == '__main__':
    n = 2
    obj = Solution()
    res = obj.climbStairs(n)
    print(f'The number of distinct way to climb {n} steps is: {res}')