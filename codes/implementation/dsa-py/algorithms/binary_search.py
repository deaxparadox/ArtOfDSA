import random

def binary_search():
    nums = sorted([
        random.randint(1, 100) for x in range(10)
    ])
    start = 0
    end = len(nums)
    target = nums[4]
    
    print(nums, f'target: {target}')

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return None

if __name__ == "__main__":
    print(binary_search())