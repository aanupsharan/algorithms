def are_equal(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    if m != n:
        return False
    
    arr1.sort()
    arr2.sort()

    i = 0
    while i < m:
        if arr1[i] != arr2[i]:
            return False

    return True

if __name__ == "__main__":
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]
  
    if (are_equal(arr1, arr2)):
        print("arrays are equal.")
    else:
        print("arrays are not equal")