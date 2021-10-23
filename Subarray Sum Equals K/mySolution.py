class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        d = {0: 1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in d:
                count += d[sum-k]
            if sum in d:
                d[sum] += 1
            else:
                d[sum] = 1

        return count
