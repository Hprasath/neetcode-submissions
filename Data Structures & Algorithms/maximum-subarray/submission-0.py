class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # # 1. left and right pointer to start of the array
        # #2. initialise max_sum = 0
        # 3. max_sum is initialised to the first element
        # move the right pointer to the next index and see if the sum increases with each step
        # if it increases, keep moving the right pointer by 1 step.
        # if it decreases, move the left pointer by one step and set the max_sum to the value of the left pointer

        left = 0
        max_sum = nums[left]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum




        