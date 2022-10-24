# Contains Duplicate - LeetCode
# https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_sofar = set()
        for num in nums:
            if num in nums_sofar:
                return True
            else:
                nums_sofar.add(num)
        
        return False