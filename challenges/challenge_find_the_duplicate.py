def validate_input(num):
    if not isinstance(num, int):
        return False
    if num < 0:
        return False
    return True


def find_duplicate(nums):
    if not nums:
        return False

    nums.sort()
    for i in range(len(nums) - 1):
        if not validate_input(nums[i]):
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
