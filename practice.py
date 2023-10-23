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


# Switching track to follow the problem list of Colin Galen (CG)
# Code With Me: 24 FAANG Interview Questions - YouTube
# https://www.youtube.com/watch?v=4uJFdTEDpds&ab_channel=ColinGalen

# Longest Continuous Increasing Subsequence - LeetCode
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    '''
    returns True when all elements are in increasing order
    '''
    def check(self, arr: List[int]) -> int:
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True
    
    # brute force passed 33/35 test cases but failed with TLE as it is O(N2)
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)) :
            for j in range(i,len(nums)) :
                subarray = nums[i: j+1]
                if self.check(subarray):
                    ans = max(ans, len(subarray))
                else:
                    # one element out of sequence is enough to stop
                    break
        return ans
    
    # sliding window - O(N)
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # handle edge cases - empty and 1-element array
        if len(nums) <= 1 :
            return len(nums)
        ans = 1
        left = 0
        for right in range(1, len(nums)):
            if nums[right] > nums[right-1] :
                ans = max(ans, right - left + 1)
            else:
                left = right
        return ans

    # sliding window - handle edge cases gracefully - idea from editorial
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = left = 0
        for right in range(len(nums)):
            if nums[right - 1] >= nums[right]:
                left = right
            ans = max(ans, right - left + 1)
        return ans

    # even simpler impl from Colin Galen (CG)
    # https://www.youtube.com/watch?v=4uJFdTEDpds&ab_channel=ColinGalen
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        current_len = best_len = 0
        for i in range(len(nums)):
            if (i == 0 or nums[i-1] >= nums[i]):
                current_len = 1
            else:
                current_len += 1
            best_len = max(best_len, current_len)
        return best_len

# Merge Two Sorted Lists - LeetCode
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return head.next

#TODO recursive approach

# Find the Difference - LeetCode
# https://leetcode.com/problems/find-the-difference/description/

class Solution:
    # first approach using hashmap failed the case "a" and "aa"
    # then used dict to store the frequency
    def findTheDifference(self, s: str, t: str) -> str:
        map = {}
        for letter in s:
            if letter in map:
                map[letter] += 1
            else:
                map[letter] = 1

        for letter in t:
            if letter in map:
                if map[letter]: 
                    map[letter] -=1
                else:
                    return letter
            else:
                return letter

    # wowed by the ASCII sum approach in the solutions
    def findTheDifference(self, s: str, t: str) -> str:
        total = 0
        for letter in t:
            total += ord(letter)
        for letter in s:
            total -= ord(letter)
        
        return chr(total)

    # xor approach even more impressive
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for letter in t:
            xor ^= ord(letter)
        for letter in s:
            xor ^= ord(letter)
        return chr(xor)

    # retry freq approach using array rather than hashmap
    def findTheDifference(self, s: str, t: str) -> str:
        # freq count of each of the 26 lowercase letters
        freq = [0] * 26

        for letter in s:
            freq[ord(letter) - ord('a')] -= 1
        for letter in t:
            freq[ord(letter) - ord('a')] += 1
        
        for i, count in enumerate(freq):
            if count:
                return chr(i + ord('a'))
            


# Count Primes - LeetCode
# https://leetcode.com/problems/count-primes/description/

class Solution:
    def isPrime(self, n: int) -> int:
        if n <= 1:
            return False
        if n == 2:
            return True
        # all even numbers at one go
        if n % 2 == 0:
            return False
        # go through all odd numbers from 3
        for i in range(3, math.isqrt(n)+1, 2):
            if n % i == 0:
                return False
        return True
    
    # TLE error for n=5 millio
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            count += int(self.isPrime(i))
        return count
    
    import math
    # Sieve of Eratosthenes Algo
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        # outer loop can run till sqrt(n)
        for i in range(2, math.isqrt(n)+1):
            # strike off mulitples of the prime
            if prime[i]:
                # we can start off at i*i as every multiple of i till then would have been covered before - from Editorial
                for j in range(i*i, n, i):
                    prime[j] = False
        
        # first 2 numbers 0 and 1 are NOT prime
        return sum(prime[2:])        
    
# Plus One - LeetCode
# https://leetcode.com/problems/plus-one/?source=submission-ac

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = digits
        # we use carry to increment the unit digit by 1 only once
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            a[i] += carry
            if a[i] == 10:
                carry = 1
                a[i] = 0
            else:
                carry = 0
                break
        if carry:
            a.insert(0, carry)
        return a
    
    # taking ideas from elegant community solution by bgautam1254
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9 :
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # only edge case is all 9s - 9999
        # above code will have made it all 0s. 
        # need to add 1 at the front
        digits.insert(0, 1)
        return digits

# Sqrt(x) - LeetCode
# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        
        return high

# Unique Email Addresses - LeetCode
# https://leetcode.com/problems/unique-email-addresses/description/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split("@")

            if "+" in local:
                index = local.index("+")
                local = local[:index]
            local = local.replace(".","")
            email = f"{local}@{domain}"
            result.add(email)
        return len(result)

    # concise way of extracing local from solutions
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split("@")

            local = local.split("+")[0]
            local = local.replace(".","")
            result.add(f"{local}@{domain}")
        return len(result)

    # CG approach - low level DIY
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local = []
            domain = []
            in_local = True
            before_plus = True

            for letter in email:
                if letter == '@':
                    in_local = False
                    continue
                
                if letter == '+':
                    before_plus = False
                    continue
                
                if in_local:
                    if before_plus and letter != ".":
                        local.append(letter)
                else:
                    domain.append(letter)
            local = "".join(local)
            domain= "".join(domain)
            result.add(local + "@" + domain)
            # print(email, local + "@" + domain)
        return len(result)
    
# Best Time to Buy and Sell Stock - LeetCode
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    # test case failed - [2,4,1]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        min_index = 0

        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
                min_index = i
        
        if min_index == n - 1:
            return 0

        max_price = 0
        for price in prices[min_index+1:] :
            max_price = max(price, max_price)
        
        return max_price - min_price
    
    # try O(n2) approach - find profit for every pair and then find max
    # TLE as expected as input is 10^5
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n-1):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max_profit

    # reduce 2 loops by storing min, max so far -> O(n)
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max_price = prices[0]
        best_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
                # this is the key - reset max when we see a new min
                max_price = min_price
            if price > max_price:
                max_price = price

            profit = max_price - min_price
            best_profit = max(profit, best_profit)
        
        return best_profit

    # CG's idea and code looks so simple and elegant - can i simplify my code?
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            best_profit = max(best_profit, profit)
            min_price = min(min_price, price)

        return best_profit

# Rotate String - LeetCode
# https://leetcode.com/problems/rotate-string/description/

