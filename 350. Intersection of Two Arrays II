# Runtime: 55 ms, faster than 87.27% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14 MB, less than 52.00% of Python3 online submissions for Intersection of Two Arrays II.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #O(n + m)
        store = {}
        intersect = []
        for x in nums1:
            if x in store:
                store[x] += 1
            else:
                store[x] = 1
        for x in nums2:
            if x in store and store[x] > 0:
                store[x] -= 1
                intersect.append(x)
        return intersect
