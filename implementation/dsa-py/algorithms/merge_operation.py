import random 

def sortArray(arr: list[int]) -> list[int]:
    length = len(arr)
    i = 0
    while i < length:
        for j in range(i+1, length):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        i+=1
    return arr


def generateArray(size: int = 5) -> list:
    return [
        random.randint(0, 100) for _ in range(5)
    ]
    
    

def mergeOperation(a, b):
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

def main():
    a = sortArray(generateArray())
    b = sortArray(generateArray())
    print("Array a:", a)
    print("Array b:", b)
    sort = mergeOperation(a, b)
    print("Merged sorted array:", sort)
    
if __name__ == "__main__":
    main()