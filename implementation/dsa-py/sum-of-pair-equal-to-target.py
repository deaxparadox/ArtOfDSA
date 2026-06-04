# Function to check whether any pair exists
# whose sum is equal to the given target value
def two_sum(arr, target):
    # Sort the array

    left, right = 0, len(arr) - 1

    # Iterate while left pointer is less than right
    while left < right:
        sum = arr[left] + arr[right]

        # Check if the sum matches the target
        if sum == target:
            return True
        elif sum < target: 
            left += 1  # Move left pointer to the right
        else:
            right -= 1 # Move right pointer to the left

    # If no pair is found
    return False


def main():
    
    arr = [-3, -1, 0, 1, 2]
    target = -2

    # Call the two_sum function and print the result
    if two_sum(arr, target):
        print("true")
    else:
        print("false")
        
        
if __name__ == '__main__':
    main()