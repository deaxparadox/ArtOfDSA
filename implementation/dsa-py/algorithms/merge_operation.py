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
    newArray = [
        random.randint(0, 100) for _ in range(5)
    ]
    sort = sortArray(newArray)
    return sort

def mergeOperation(a, b):
    c = []
    na, nb= 0, 0
    m, n = len(a), len(b)
    
    while na < m and nb < n:
        if a[na] < b[nb]:
            c.append(a[na])
            na+=1
        else:
            c.append(b[nb])
            nb+=1

    while nb < n:
        c.append(b[nb])
        nb+=1
  
    while na < m:
        c.append(a[na])
        na+=1
    return c

def main():
    a = generateArray()
    b = generateArray()
    print(a, b)
    c = []
    sort = mergeOperation(a, b)
    print(sort)
    
if __name__ == "__main__":
    main()