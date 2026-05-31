class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset=set(nums)
        if len(nums)!=len(hset):
            return True
        else:
            for i in nums:
                if i in hset:
                    return False
            else:
                return False
            