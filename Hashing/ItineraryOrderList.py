def print_itinerary(d):
    reverse_dict = dict()

    for i in d:
        reverse_dict[d[i]] = i

    for i in reverse_dict:
        if reverse_dict[i] not in reverse_dict:
            starting_point = reverse_dict[i]
            break
    
    while starting_point in d:
        print(starting_point, "-->", d[starting_point], end=", ")
        starting_point = d[starting_point]
        
if __name__=="__main__": 
    d = dict() 
    d["Chennai"] = "Banglore"
    d["Bombay"] = "Delhi"
    d["Goa"] = "Chennai"
    d["Delhi"] = "Goa"
  
    print_itinerary(d) 