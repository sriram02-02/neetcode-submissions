class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        for i in nums:
            s[i]=1+s.get(i,0)
            if s[i]>len(nums)/2:
                return i
        return -1