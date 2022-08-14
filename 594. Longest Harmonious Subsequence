Runtime: 376 ms, faster than 73.96% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 15.9 MB, less than 48.94% of Python3 online submissions for Longest Harmonious Subsequence.
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        store = {}
        largest = 0
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
            if num + 1 in store:
                largest = max(largest,store[num] + store[num+1])
            if num - 1 in store:
                largest = max(largest,store[num] + store[num-1])
        return largest
