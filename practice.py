# 1 Two Sum - LeetCode
# https://leetcode.com/problems/two-sum/description/

class Solution:
    # brute force O(N2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
              return [i, j]

    # Use a dict to lookup O(N) in TC and SC
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      d = {item: i for i, item in enumerate(nums)}
      for i, item in enumerate(nums):
        item_needed = target - item
        # handle case where item is half of target - this would lead to yes when that item does NOT exist
          
        if item_needed in d:
          j = d[item_needed]
          if item_needed == item:
            # check whether there is one more occurence of the item in the dictionary
            # the 2nd item would have overwritten the 1st items - hence we can check indexes
            if i == j:
              continue
          return [i, j]

    # sort the array and use 2 pointers on opposite sides
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      sorted_nums = sorted(nums)
      i = 0
      j = len(nums)-1
      while i < j: 
        total = sorted_nums[i] + sorted_nums[j]
        if  total == target:
          # we found the match, but we need the original index
          i_original = nums.index(sorted_nums[i])
          j_original = nums.index(sorted_nums[j])
          if i_original == j_original:
            j_original = nums.index(sorted_nums[j], j_original+1)
          return [i_original, j_original ]
        elif total < target:
          # this means that we need more to add to the total, so move to the right
          i += 1
        else:
          # this means we need to reduce from the total, so move to the left
          j -= 1    

# v2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target :
                    return [i, j]

    # use hashmap for lookup
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {item: i for i, item in enumerate(nums)}
        for i, item in enumerate(nums):
            item_needed = target - item
            if item_needed in map and map[item_needed] != i: 
                return [i, map[item_needed]]
    
    # single pass with hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, item in enumerate(nums):
            item_needed = target - item
            if item_needed in map:
                return [i, map[item_needed]]
            else:
                map[item] = i
                
    # sort the array and use 2-pointers
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        i = 0
        j = len(nums) - 1
        while i < j: 
            total = sorted_nums[i] + sorted_nums[j]

            if total < target:
                i += 1
            elif total > target :
                j -= 1
            else:
                break
        
        # now we need to find these items in the original unsorted array
        item1 = sorted_nums[i]
        item2 = sorted_nums[j]

        item1_index = nums.index(item1)
        item2_index = nums.index(item2)

        # TODO Got this part wrong
        if item1_index == item2_index:
            item2_index = nums.index(item2, item1_index + 1)

        return [item1_index, item2_index]
          

# 2 Add Two Numbers - LeetCode
# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None

        while l1 or l2:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            total = l1_val + l2_val + carry
            rem = total % 10
            carry = total //10

            newNode = ListNode(rem)
            if head is None:
                head = newNode
                currentNode = head
            else:
                currentNode.next = newNode
                currentNode = currentNode.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry > 0:
            newNode = ListNode(carry)
            currentNode.next = newNode
        
        return head

# v2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        current = ListNode(0)
        dummyHead = current
        while l1 or l2 or total:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            newNode = ListNode(total %10)
            current.next = newNode
            current = current.next

            # use total as carry for the next iteration
            total = total // 10
        
        return dummyHead.next
    

# 3 Longest Substring Without Repeating Characters - LeetCode
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = ''
        for i in range(len(s)):
            substr = []
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    substr.append(s[j])
                else:
                    break
            if len(result) < len(substr):
                result = substr
            seen.clear()
        return len(result)

# v2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break
            ans = max(ans, len(seen))

        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                ans = max(ans, len(seen))
            else:
                seen.remove(s[i])
                i += 1
        return ans
    
    
# 4 Median of Two Sorted Arrays - LeetCode
# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
          if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
          else:
            result.append(nums2[j])
            j += 1
        
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        
        result_len = len(result)
        median_index = result_len // 2
        if result_len % 2 == 1:
          return result[median_index]
        else:
          return (result[median_index] + result[median_index-1])/2