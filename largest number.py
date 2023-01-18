class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if len(nums) == 1:
            return str(nums[0])
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            for j in range(i+1,len(nums)):
                nums[j] = str(nums[j])
                if nums[j]+nums[i] > nums[i] +nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        output = "".join(nums)
        if output == '0'*len(output):
            return '0'
        else:
            return output
