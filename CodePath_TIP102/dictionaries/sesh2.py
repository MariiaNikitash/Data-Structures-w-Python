#Problem 2: Verifying Authenticity
# The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it 
# array of length n + 1 containing the integers from 1 to n - 1 exactly once, and int n twice. Ex: base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

#Write a func that accepts arr of integers art_pieces and returns True if given array is authentic array, else False.
def is_authentic_collection(art_pieces):
    n = max(art_pieces)
    if len(art_pieces) != n+1: # bc nums are ordered, no skips so biggest num should appear twice
        return False
    
    counts = {}
    for num in art_pieces:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for i in range(1, n):
        if counts.get(i, 0) == 1:
            return True
    
    return counts.get(n, 0) == 2
    



collection1 = [2, 1, 3] # F
collection2 = [1, 3, 3, 2] # T
collection3 = [1, 1] # T

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))