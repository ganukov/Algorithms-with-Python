def reverse_array(nums, idx):
    if idx == len(nums) // 2:
        return
    swap_idx = len(nums) - 1 - idx
    nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
    reverse_array(nums, idx + 1)


nums = input().split()

reverse_array(nums, 0)
print(' '.join(nums))
