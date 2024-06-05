from collections import Counter 

def get_group_words(words):

    dict = {}
    for word in words:
        word_dict = Counter(word)
        key = sorted(word_dict.keys())
        key = "".join(key)
        
        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = [word]
    
    return(dict)

if __name__ == "__main__":
    input=['may','student','students','dog','studentssess','god','cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle']
    result = get_group_words(input)

    for key in result.keys():
        print(result[key])