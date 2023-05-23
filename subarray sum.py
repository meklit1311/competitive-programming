class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = 0
        count = 0
        size = len(nums)

        dic = defaultdict(int)
        dic[0] = 1

        for i in range(size):
            pref += nums[i]
            if pref - k in dic:
                count += dic [pref - k]
            dic[pref] += 1

        return count 
