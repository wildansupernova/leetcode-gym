class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stk = []
        for item in path:
            if item=="" or item==".":
                continue
            elif item=="..":
                if len(stk)>0:
                    stk.pop()
            else:
                stk.append(item)
        return "/" + "/".join(stk)