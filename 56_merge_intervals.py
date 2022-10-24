# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals are NOT sorted - so, sort them first based on start, and then end
        intervals = sorted(intervals, key=lambda x: (x[0],x[1]))

        ans = [intervals[0]]
        
        for index in range(1, len(intervals)):
            i1 = ans[-1]
            i2 = intervals[index]
            
            # int2 is to the right of int1 - not even touching - hence no overlap
            # if i1.end < i2.start:
            if i1[1] < i2[0]:
                ans.append(i2)
            else:
                # there is overlap - hence we need to merge
                # 2 cases - i2 can be totally contained in i1 or can be partially contained
                # start = i1.start 
                start = i1[0]
                # end = max(i1.end, i2.end)
                end = max(i1[1], i2[1])
                # pop the last interval and put the merged interval
                ans.pop()
                ans.append([start,end])
        return ans
                
                