"""
i12iz4n
i 12 i z 4 n
  |
internationalization
        |

"""

def isNumber(c):
    return ord('0')<=ord(c)<=ord('9')

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        iWord = 0
        iAbb = 0

        while iWord<len(word) and iAbb<len(abbr):
            if isNumber(abbr[iAbb]):
                if abbr[iAbb] == "0":
                    return False
                curNumber = 0
                while iAbb<len(abbr) and isNumber(abbr[iAbb]):
                    curNumber = curNumber*10 + int(abbr[iAbb])
                    iAbb+=1
                iWord += curNumber
                continue
            elif abbr[iAbb]!=word[iWord]:
                return False
            else:
                iWord+=1
                iAbb+=1
        return iWord==len(word) and iAbb==len(abbr)

