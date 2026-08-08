class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == '+':
                op1 = st.pop()
                op2 = st.pop()
                st.append(op1+op2)
            elif t == '-':
                op1 = st.pop()
                op2 = st.pop()
                st.append(op2-op1)
            elif t == '*':
                op1 = st.pop()
                op2 = st.pop()
                st.append(op1*op2)
            elif t == '/':
                op1 = st.pop()
                op2 = st.pop()
                st.append(int(op2/op1))
            else:
                st.append(int(t))
                
        return st[0]