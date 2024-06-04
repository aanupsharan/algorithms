def findDuplicate(arr):
    if arr == None:
        return None

    n = len(arr)
    s = set()
    for i in range(n):
        if arr[i] in s:
            return arr[i]
        s.add(arr[i])
    
    return None

if __name__ == "__main__":
  arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
  print(findDuplicate(arr))
