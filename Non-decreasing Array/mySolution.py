def checkPossibility(self, nums: List[int]) -> bool:
    count = 0
    for i in range(1, len(nums)):
        if count >= 2:
            return False
        if nums[i] < nums[i-1]:
            count += 1
            if i > 1 and i < len(nums)-1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]:
                count += 1
    if count < 2:
        return True
    else:
        return False
