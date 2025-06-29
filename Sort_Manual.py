def sort_dicts_by_key_manual(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i].get(key) > data[j].get(key):
                data[i], data[j] = data[j], data[i]
    return data

#- Slower: Loops through the data (less efficient).
#- Simple: Good for learning how sorting works.
#- Not Ideal: Not great for big data or scaling.
