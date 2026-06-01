class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=[]
        for i in s:
            l.append(i)
        i=0
        while l:
            s[i]=l.pop()
            i+=1
        return s

        """
        Do not return anything, modify s in-place instead.
        """
        