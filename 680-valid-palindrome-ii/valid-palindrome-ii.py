class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        # First pass - choose left to delete
        
        left = 0
        right = n-1
        deleteAlready = False
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                if deleteAlready:
                    break
                left+=1
                deleteAlready = True

        if left>=right:
            return True
        
        left = 0
        right = n-1
        deleteAlready = False
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                if deleteAlready: return False
                right-=1
                deleteAlready = True
        return left>=right

