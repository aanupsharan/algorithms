def assign_and_print(d):

    num_of_report = dict()

    for i in d:
        num_of_report[i] = 0

    for i in d:
        if i == d[i]:
            continue
        if d[i] in num_of_report:
            num_of_report[d[i]] += 1

    return num_of_report

if __name__=="__main__":
    d = dict() 
    d["A"] = "C"
    d["B"] = "C"
    d["C"] = "F"
    d["D"] = "E"
    d["E"] = "F"
    d["F"] = "F"

    print(assign_and_print(d))