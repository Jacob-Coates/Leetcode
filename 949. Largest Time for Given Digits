class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        # get largest candidate numbers less than 3
        string = ""
        candidates1 = sorted([x for x in arr if x < 3],reverse=True)
        for num in candidates1:
            string = str(num)
            sub_arr = arr.copy()
            sub_arr.remove(num)
            m = -1
            if num == 2:
                # next num needs to be less than 5
                m_arr = [x for x in sub_arr if x < 4]
                if m_arr == []:
                    break
                else:
                    m = max(m_arr)
            else:
                m = max(sub_arr)
            string = string + str(m) + ":"
            sub_arr.remove(m)
            candidates2 = [x for x in sub_arr if x < 6]
            if candidates2 == []:
                continue
            else:
                m = max(candidates2)
                string += str(m)
                sub_arr.remove(m)
                string += str(sub_arr.pop())
                break
        if len(string) == 5:
            return string
        return ""
