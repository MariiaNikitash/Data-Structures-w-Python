# time complexity: O(N^2)
# space complexity: O(N x M)
def func(A,B,target):
    arr = []
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            if A[i] + B[j] == target:
                arr.append((A[i], B[j]))
    return arr



test = func([1,2,3,5], [2,4,5,1], 3)  
print(test)


# time complexity: O(N)
# space complexity: O(N + M)
def mapping(A,B,target):
    setB = set(B)
    arr = []
    for i in range(0, len(A)):
        complement = target - i
        if complement in setB:
            arr.append(complement)
    return arr
        
test = func([1,2,3,5], [2,4,5,1], 3)  