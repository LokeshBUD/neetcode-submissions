class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = []

        for i,t in enumerate(temperatures):
            while st and t > st[-1][0]:
                st_temp, st_idx = st.pop()
                res[st_idx] = (i - st_idx)
            st.append([t,i])
        
        return res