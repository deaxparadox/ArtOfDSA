# Sliding window pattern


### Find averages of sub arrays

```py

def average_sums(nums: list[int], k: int) -> list[int]:
    sums = []
    nums_len = len(nums)
    for i in range(0, nums_len-k+1):
        s = 0
        for j in range(i, i+k):
            s += nums[j]
        sums.append(s)
    return sums
        
if __name__ == "__main__":
    num_list = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(average_sums(num_list, 5))

```

```bash
[11, 14, 12, 18, 14]
```