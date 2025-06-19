# Standart Problem Set 2

def remove_low_rated_destinations(destinations, rating_threshold):
    to_remove = []
    for key, val in destinations.items():
        if val < rating_threshold:
            to_remove.append(key)
    for  key in to_remove:
        del destinations[key]

    return destinations


destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

#print(remove_low_rated_destinations(destinations, 4.0))
#print(remove_low_rated_destinations(destinations2, 4.9))

def unique_souvenir_counts(souvenirs):
    dic = {}
    seT = set()
    for souv in souvenirs:
        if souv in dic:
            dic[souv] +=1
        else:
            dic[souv] = 1
    for val in dic.values():
        if val in seT:
            return False
        seT.add(val)
    return True



souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))


def arrange_guest_arrival_order(arrival_pattern):
    
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  

#123549876
#4321
