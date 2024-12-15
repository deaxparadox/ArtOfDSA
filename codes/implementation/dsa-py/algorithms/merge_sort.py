from typing import Optional, Any


def merge(a, b):
    c = []
    mi, ni= 0, 0
    m, n = len(a), len(b)
    
    while mi < m and ni < n:
        if a[mi] < b[ni]:
            c.append(a[mi])
            mi+=1
        else:
            c.append(b[ni])
            ni+=1

    while ni < n:
        c.append(b[ni])
        ni+=1
  
    while mi < m:
        c.append(a[mi])
        mi+=1
    return c



def merge_sort(arr: Optional[list], start: int = 0, stop: int = 0) -> None:
    if start <= stop:
        return
    
    mid = (start + stop) // 2
    
    left_arr = merge_sort(arr, start, mid)
    right_arr = merge_sort(arr, mid+1, stop)
    
        
        
    merge(left_arr, right_arr)
    
if __name__ == "__main__":
    arr = [12, 43, 23, 56, 34, 26]
    print(merge_sort(arr, 0, len(arr)))
    print(arr)