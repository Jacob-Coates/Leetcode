class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        store = {x: arr.count(x) for x in arr}
        values = set()
        for i, (k,v) in enumerate(store.items()):
            if v in values:
                return False
            else:
                values.add(v)
        return True
