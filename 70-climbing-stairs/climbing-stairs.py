class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def knapsack(n) ->int:
            if n<1 or n>45:
                return 0
            if n==1:
                return 1
            if n==2:
                return 2
            return (knapsack(n-2)+knapsack(n-1))
        return knapsack(n)    