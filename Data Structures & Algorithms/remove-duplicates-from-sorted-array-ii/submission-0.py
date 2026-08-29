class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        
        n = len(nums)

        if n <= 2:
            return n
        
        read=2
        write = 2

        for read in range(2, len(nums)): 
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        
        return write


        