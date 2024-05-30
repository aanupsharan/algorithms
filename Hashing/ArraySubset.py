
def isSubset(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    s = set()

    for i in range(n):
        s.add(arr1[i])
    
    p = len(s)

    for i in range(n):
        s.add(arr2[i])
    
    if(len(s) < (m+n)):
        return True
    
    return False

if __name__ == '__main__':

    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]


    if (isSubsetApproachTwo(arr1, arr2)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[] ")
    