# Two pointer techniques

**Two pointers** uses two indexes variables to traversae the data structure, typically an array or in string. The poniters move towards each other, away from each other, or in the same direction based on the problem's requirements.

Using this approach, you can reduce the time complexity of many array and string problems from $O(n^2)$ to $O(n)$, or to $O(n log n)$ when sorting is required first.


### What is a Pointer?

A pointer is a variable that represents an index or position within a data structure, such as an array or linked list.

The pointers can represent:

- Boundaries of a range (left and right ends)
- Current position and comparison position (for removing duplicates)
- Two separate arrays (for merging or comparing)
- Fast and slwo travesal speeds (for cyclt detection, covered below under same-direction pointers).

Using pointers at different positions, we can compare elements and make decisions without relying on nested loops, which would otherwise lead to $O(n^2)$ time complexity.

### 1. Opposite Direction (Converging Pointers)

In the most common variant, one pointer start at the begining, the other at the end, and they move towards each other.

This strategy is ideal for problems where we need to compare elements from opposite ends of an array or string.

#### Template

```py
def opposite_direction_template(nums: list[int]) -> None:
    left = 0
    right = len(nums) - 1

    while left < right:
        # Calculate or check current state
        current = calculate_something(nums, left, right)

        if found_answer(current, nums, left, right):
            # Process and possibly return
            return
        elif need_to_increase_value(current, nums, left, right):
            left += 1
        else:
            right -= 1
```


Which pointer to move depends on the comparison. In sorted arrays:

- Moving `left` right incrase value (if sorted ascending).
- MOving `right` left decrases values (sorted ascending).


#### When sorting is required

Opposite-direction two pointers for pair-sum problems such as `Two Sum II` and `3Sum` requires the array to be sorted. The technique relies on monotonicity: increasing `left` only increase the sum, and decreasing `right` only decreases it. Without that property, you cannot decide which ponter to move after a comparison.

Opposite-direction two pointers for pallindrome or mirror checks doesnot require sorting. It relies on position symmetry, not value order, so the comparison is between characters at mirrored indices.

Same-direction variants such as `read/write partition`, `sliding window`, and `fast/slow` pointers generally do not require sorting either.

When sorting is required and the input is unsorted, the overall compexity becomes $O(nlogn)$ for the sort plus $O(n)$ for the two-pointer scan, dominated by the sort.


Time: $O(n)$
Space: $O(1)$


#### Example

**Checking if a string is a pallindrome**

A **palindrome** is a sequence that reads the same forward and backward (e.g., `"racecar"`, `"madam"`).

To check if a string is a pallindrome, we:

- **Initialize two pointers**: one at the **beginning** and one at the **end**.
- Compare characters at both pointers:
    - If they match, move both pointers **inward**.
    - If they do not match, return `false`.
- **Repeat until the pointers meet**.

### 2. Same Direction (Parallel Pointers)

In this approach, both pointers start at the same end (usually the begining) and move in the direction at the different speeds or for different purposes.

These pointers serve two different but complementary roles:

- the `left` pointer is the **write pointer or boundary**, tracking progress and marking where valid elements end.
- the `right` pointer is the **read and explore pointer**, scanning ahead looking for the next element to process.

#### Template

```py
def same_direction_template(nums: list[int]) -> int:
    left = 0  # write pointer / boundary of valid region
    result = 0

    for right in range(len(nums)):
        # Check if current element should be kept
        if should_keep(nums[right]):
            current = calculate_something(nums, left, right)
            update_result()
            left += 1

    # left now represents the count of valid elements
    return result
```

Here are the two popular variations of this approach:

- **Sliding Window Technique**: In this approach, two pointers slide across an array or string while maintaing a dynamic range. It's commonly used to find subarrays or substrings that meet specific criteria, such as:
    - Finding the longest substring without repeating characters.
    - or Finding the smallest subarray with a given sum
- **Fast and Slow Pointers**: Thins involes two pointers moving at different speeds. It's commonly used to detect cycles in linked lists or find the middle node of a linked list.


#### Why FLoyd's cycle detection works

The stand speed choice is 1 step for the slow pointers and 2 steps for the fast pointer. If the linked has a cycle, the slow pointer eventually enters the cycle and starts looping around it. THe fast pointer is also looping around the cycle but move twice as fast.