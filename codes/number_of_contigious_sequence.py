from typing import Any

def main(arr: list[Any] | int | float, k: int) -> int:
    """
    Function to find the number of contigious subsequence in a given array.
    
    parameter:
    
    - arr: pass the arr as `list`, or array length of type `int` or `float`.
    - k: length of contigious sequence
    """
    if isinstance(arr, list): 
        return len(arr) - k + 1
    
    if isinstance(arr, int): 
        return arr - k + 1
    
    if isinstance(arr, float): 
        sub_seq = arr - float(k) + 1.0
        return int(sub_seq)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 23, 12, 43, 5]
    
    print("Original array:", arr)
    
    print(f"\n{'Sequence size':^20} | {'No of Seq':^20}")
    for i in range(2, 7):
        no_of_seq = main(11.0, i)
        print(f"{i:^20} | {no_of_seq:^20}")
    print()