class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def fact(n):
            if n <= 1:
                return 1
            else:
                return n * fact(n-1)
        return int(fact(n+m-2)/((fact(n-1))*(fact(m-1))))
