class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
             return False


        
        
        
        # return Counter(s)==Counter(t)
        
        
        
        # x=len(s)
        # y=len(t)
        # if x==y:
        #     for i in s:
        #         if i in t:
        #             continue
        #         else:
        #             return False
        #     return True
        # else:
        #     return False