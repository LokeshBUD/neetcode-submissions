class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic stack - it stores decreasing orders.  
        res = [0]*len(temperatures)
        st = [] #storing pair: [temp, idx]

        for i,t in enumerate(temperatures):
            while st and t > st[-1][0]:
                st_temp, st_idx = st.pop()
                res[st_idx] = (i - st_idx)
            st.append([t,i])
        
        return res