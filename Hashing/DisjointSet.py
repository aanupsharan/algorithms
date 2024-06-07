def are_disjoint(set1, set2):
    m = len(set1)
    n = len(set2)

    s = set()
    for i in range(m):
        s.add(set1[i])
    
    for i in range(n):
        if set2[i] in s:
            return False
    return True
if __name__ == "__main__":
    set1 = [12, 34, 11, 9, 2]
    set2 = [7, 2, 1, 5]

    print(are_disjoint(set1, set2))