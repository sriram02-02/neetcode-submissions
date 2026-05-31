class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        strs.sort()
        f=strs[0]
        l=strs[-1]
        for i in range(len(f)):
            if f[i]==l[i]:
                res=res+f[i]
            else:
                break
        return res
        
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i==len(s) or s[i] != strs[0][i]:
        #             return res
        #     res+=strs[0][i]
        # return res
        # strs=sorted(strs)
        # l=[]
        # for i in range(len(strs)) :
        #     if strs[i][0:2]==strs[i+1][0:2]:

        #         l.append(strs[i][0:2])
                
    
            
        # if l:
        #     return 
        # else:
        #     return ""