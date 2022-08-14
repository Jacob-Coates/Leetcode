# Runtime: 99 ms, faster than 98.78% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.6 MB, less than 71.30% of Python3 online submissions for Top K Frequent Elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {} # Store keys for DP
        #Count occurances
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        #Sort list and return array of numbers to k
        q = sorted(list(store.keys()),key = lambda x: -store[x])
        return q[:k]
