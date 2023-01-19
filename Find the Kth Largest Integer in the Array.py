class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        num_int=[]
        for i in nums:
            num_int.append(int(i))
        num_int.sort()
        e=len(num_int)-1
        ans=num_int[e]
        while k>=1:
            ans=num_int[e]
            e-=1
            k-=1
        return str(ans)
