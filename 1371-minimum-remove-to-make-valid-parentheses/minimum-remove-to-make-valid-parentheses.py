class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        stk = []
        n = len(s)
        for i in range(n):
            if s[i]=="(":
                stk.append(("(", i))
            if s[i]==")":
                if len(stk)==0 or stk[-1][0]==")":
                    stk.append((")", i))
                elif stk[-1][0]=="(":
                    stk.pop()
        removeIndexSet = set()
        for _, i in stk:
            removeIndexSet.add(i)
        return "".join([ s[i] for i in range(n) if i not in removeIndexSet ])