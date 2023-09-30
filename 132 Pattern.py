from itertools import accumulate

class Solution:
    def find132pattern(self, nums):
        mins = list(accumulate(nums, min))
        st = [] 
        n = len(nums)
        
        for j in range(n-1, -1, -1):
            if nums[j] > mins[j]:
                while st and st[-1] <= mins[j]:
                    st.pop()
                if st and st[-1] < nums[j]:
                    return True
                st.append(nums[j])           
        return False