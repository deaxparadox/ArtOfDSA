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

The relative speed of the fast pointer with respect to the slow pointer is 1 step per iteration: fast advances 2, slow advances 1, and the net difference is 1. Once both pointers are inside the cycle, the fast pointer gains exactly 1 step on slow every itration. Since the cycle has the finite length `L`, fast catches up to slow within at most `L` iterations.

IF the list has no cycle, the fast pointer reaches the end of the list (`null`) first. THat is the termination condition of the no-cycle case.

To find the starting node of the cycle after detection, reset on pointer to the head and advance both pointers at speed 1. They meet at the cycle's entry node. This is a standard interview follow-up to plain cycle detection.

TIme: $O(n)$
Space: $O(1)$

The general same-direction template (read/write partition) also runs in:

TIme: $O(n)$ and 
Space: $O(1)$, 

since each pont4er advances at most n times across the array.

### 3. Fixed-Offset Pointers (Same Direction)

This is a specific same-direction pattern, not a seprate variant. Both pointers move in the same direction, but on is advanced first to create a fixed gap between them before they more together.

In this approach, we move the first pointer independently until it finds an element that meets a certain conditions. After this, we start traversing with the second pointer to find additional information related to what the first pointer found.

The pattern applies when we need to process elements in stages or maintain a fixed distance between two pointers.

#### Template


```py
def trigger_based_template(nums: list[int]) -> None:
    first = 0
    second = 0
    triggered = False

    while first < len(nums):
        # 1) TRIGGER PHASE: advance first until a condition becomes true
        if not triggered:
            if meets_condition(nums[first]):
                triggered = True
                second = 0  # or some_start_index, depending on the problem
            first += 1
            continue

        # 2) COUPLED PHASE: now advance second (or both) to extract info
        while second < first:
            process_pair(nums, second, first - 1)
            second += 1

        # optional: reset trigger if the stage ends
        triggered = False
```

A good example of this approach is finding the Nth node from the end of a linked list.
- Initailize both pointers (`fast` and `slow`) at the head.
- Advance the `fast` pointer `n` steps.
- Then move both pointers one step at a time until the `fast` pointer reaches the end.
- The `slow` pointer is now at the Nth node from the end.

Time: $O(n)$
Space: $O(1)$

### When to use two pointers pattern?

A **Two-Pointer algorithm** is generally applied to **liear data structures**, such as: array, strings or linked lists.

Two pointers fits patterns where the input data follows a predictable pattern, such as a sorted array or pallindrome string. Common patterns include:

**1. Sorted array with pair/triplet finding**

If the array is sorted (or can be stored) and you need to find elements that satisfy some relationship, tow pointers can often replace nested loops.

**2. In-place array modification**

When you need to modify an array without using extra space, the read-write pointer pattern works well.

**3. Palindrome or symmetry checking**

Comparing elements from both ends leads to two pointers converging.

**4; Merging or comparing sorted sequences**

When working with two sorted arrays, using a pointer for each is the natural approach.

**5. Subarray problems with monotonic conditions**

If expanding a window changes a conditions in a predictable direction, two pointers can work. This overlaps with sliding window, which is two pointers with specific sementics.

| Problem Type | Variant | Example |
|-|-|-|
| Find prai with target sum | Opposite direction | Two Sum II (sorted array) |
| Check palindrome | Opposite direction | Valid Palindrome |
| Remove duplicates | Same direction  | Remove Duplicates from Sorted Array | 
| Partition array | Same direction  | Move Zeroes, Sorted Colors |
| Merge sorted arrays | Two arrays | Merge Sorted Array |
| Maximim area | Opposite direction | Container With Most Water |


### When Not to use two pointers:
- Array is not sorted and sorting would change the answer (e.g., need original indices).
- No monotonic relationshpi between pointer positions and the condition.
- You need to find all pairs, not just check existence (may still need $O(n^2)$)
- THe problem requires looking at non-contiguous elements in arbitrary combinations.