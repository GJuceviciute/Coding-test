def secondLowest(nums):
    # assumes an array/list is not empty
    set_nums = set(nums)
    if len(set_nums) == 1:
        return nums[0]
    nums.sort()
    if len(set_nums) == len(nums):
        return nums[1]
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    frequencies = sorted(set(d.values()))
    if len(frequencies) == 1:
        second_lowest_frequency = frequencies[0]
    else:
        second_lowest_frequency = frequencies[1]
    low_frequency_elements = sorted([i for i in d if d[i] == second_lowest_frequency])
    if len(low_frequency_elements) == 1:
        return low_frequency_elements[0]
    return low_frequency_elements[1]
