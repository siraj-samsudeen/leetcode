# Largest Rectangle in Histogram - Problem | Scaler Academy
# https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/
class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        def prevSmallerIndex(arr):
            n = len(arr)
            ans = [-1]* n
            
            stack = []
            for i in range(n):
                # we are storing indexes in the stack and in the answer - not the elements
                while stack and arr[i] <= arr[stack[-1]]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1]
                stack.append(i)
            
            return ans

        def nextSmallerIndex(arr):
            n = len(arr)
            # default value on the right is X - one plus the last index
            ans = [n]* n
            
            stack = []
            # start from rightmost index n-1 and go till index 0
            for i in range(n-1,-1,-1):
                while stack and arr[i] <= arr[stack[-1]]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans

        arr = A
        left = prevSmallerIndex(arr)
        right = nextSmallerIndex(arr)
        # safe to initialize with first element
        ans = arr[0]
        for i in range(len(arr)):
            height = arr[i]
            width = right[i] - left[i] - 1
            area = height * width
            ans = max(ans, area)
        return ans