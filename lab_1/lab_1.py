def find_sum(nums, target):

    if type(nums) != list or type(target) != int:
        return None

    for i in range(len(nums)):

        for j in range(len(nums)):

            if type(nums[j]) != int:
                return None

            if i == j:
                continue

            if nums[i] + nums[j] == target:
                return [i, j]

    else:
        return None

