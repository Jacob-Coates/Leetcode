# Runtime: 147 ms, faster than 84.88% of Python3 online submissions for Minimum Number of Refueling Stops.
# Memory Usage: 14.2 MB, less than 74.58% of Python3 online submissions for Minimum Number of Refueling Stops.

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # A priority queue can be used to achieve O(n log n time)
        seen = []
        count = 0
        for distance, fuel in stations:
            if target <= startFuel:
                break
            while startFuel < distance and seen:
                #pop
                startFuel += -heapq.heappop(seen)
                count += 1
            if startFuel < distance:
                break
            # change inequality before queue
            heapq.heappush(seen, -fuel)
        while seen and startFuel < target:
            #revert original value before adding
            startFuel += -heapq.heappop(seen)
            count += 1
        if target <= startFuel:
            return count
        return -1
