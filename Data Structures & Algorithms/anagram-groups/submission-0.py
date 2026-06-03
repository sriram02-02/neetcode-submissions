class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            key = ''.join(sorted(s))
            hashMap.setdefault(key, []).append(s)
        return list(hashMap.values())
        
        # x={}
        # for i in strs:
        #     x[i.sort()]=x.get(i.sort(),[]).append(i)
        # return list(x.values())



        
        