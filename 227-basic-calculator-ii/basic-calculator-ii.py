def isNumber(c):
    return ord("0")<=ord(c)<=ord("9")

def parse(s):
    s = [c for c in s if c!=" " ]
    tokens = []
    i = 0
    while i<len(s):
        if isNumber(s[i]):
            curNumber = 0
            while i<len(s) and isNumber(s[i]):
                curNumber = curNumber*10 + int(s[i])
                i+=1
            tokens.append(curNumber)
        else:
            tokens.append(s[i])
            i+=1
    return tokens

class Solution:
    def calculate(self, s: str) -> int:
        
        tokens = parse(s)

        stk = []
        for item in tokens:
            if len(stk)==0:
                stk.append(item)
            elif stk[-1]=="+" or stk[-1]=="-":
                stk.append(item)
            elif stk[-1]=="/":
                stk.pop()
                stk.append(stk.pop()//item)
            elif stk[-1]=="*":
                stk.pop()
                stk.append(stk.pop()*item)
            else:
                stk.append(item)
        if len(stk)==1:
            return stk[0]
        result = stk[0]
        for i in range(2, len(stk), 2):
            if stk[i-1]=="-":
                result-=stk[i]
            else:
                result+=stk[i]
        return result