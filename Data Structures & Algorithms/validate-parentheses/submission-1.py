class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c not in bracket_map:
                # It's an opening bracket
                st.append(c)
            else:
                # It's a closing bracket. Check if stack has items and matches.
                if not st or st[-1] != bracket_map[c]:
                    return False
                st.pop()
                
        # Return True only if the stack is completely resolved
        return not st
                
