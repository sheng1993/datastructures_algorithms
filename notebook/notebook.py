class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        rf = [0] * n
        nrf = [0] * n

        rf[0] = rf[1] = nums[0]
        nrf[1] = nums[1]

        for i in range(2, n - 1):
            rf[i] = max(rf[i - 2] + nums[i] if i > 1 else 0, rf[i - 1] if i > 0 else 0)
            nrf[i] = max(nrf[i - 2] + nums[i] if i > 1 else 0, nrf[i - 1] if i > 0 else 0)
        
        return max(rf[-2], max(nrf[-3] + nums[n - 1], nrf[-2]))

s = Solution()
print(s.rob([2,3]))