# Time Complexity: O(n²)
# Space Complexity: O(n)

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[-1]

    left = []
    right = []

    for num in nums[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [5, 2, 8, 1, 3]

print(quick_sort(nums))