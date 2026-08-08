class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                st.append(int(t))
            else:
                op1 = st.pop()
                op2 = st.pop()
                if t == '+':
                    st.append(op1+op2)
                elif t == '-':
                    st.append(op2-op1)
                elif t == '*':
                    st.append(op1*op2)
                else:
                    st.append(int(op2 / op1))
        return st[-1]