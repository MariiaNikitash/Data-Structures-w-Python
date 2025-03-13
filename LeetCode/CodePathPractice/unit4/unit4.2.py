def is_long_pressed(name, typed):
    i,j = 0,0

    while i < len(name) and j < len(typed):
        if name[i] == typed[j]:
            i +=1
            j +=1
        elif j > 0 and typed[j] == typed[j-1]:
            j+=1
        else:
            return False
    
    if i < len(name): # it means some characters were missing
        return False
    
    # Check remaining characters in typed to ensure they are all the same as the last character in name
    while j < len(typed):
        if typed[j] != name[-1]:
            return False
        j += 1
    
    return True

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed)) #True

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2)) #False bc there's 2 e's in saeed

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3)) #True
