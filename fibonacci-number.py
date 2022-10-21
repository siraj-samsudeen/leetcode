# Fibonacci Number - LeetCode
# https://leetcode.com/problems/fibonacci-number/
class Solution:
#     DP style
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b = 0, 1

        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c
            
        return c           
    
#     recursive
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        return self.fib(n-1) + self.fib(n-2)

#     clever version of DP style without a 3rd variable
    def fib(self, n: int) -> int:
        if n < 2: return n
        a, b = 0, 1
        
        for _ in range(1, n):
            a, b = b, a+b
        return b     
