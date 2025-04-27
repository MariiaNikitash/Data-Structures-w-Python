# Problem 1: Neatly Nested
def is_nested(s):
	if s == '':
		return True
	
	if len(s) >= 2 and s[0] == '(' and s[-1] == ')':
    #After binary search, low might move past the
    # array bounds if no 1s exist. I check to avoid IndexError and ensure correctness
		return is_nested(s[1:-1])
	return False
	
#print(is_nested("(()"))


# Problem 2: How Many 1s
# Step by step visual
def count_ones(lst):
    low, high = 0, len(lst) - 1
    step = 1  # Just to number the steps

    print(f"\nInitial array: {lst}\n")

    while low <= high:
        mid = (low + high) // 2
        print(f"Step {step}: low={low}, mid={mid}, high={high}, lst[mid]={lst[mid]}")

        if lst[mid] == 0:
            print(f"  lst[mid] == 0 → Move right: low = mid + 1")
            low = mid + 1
        else:
            print(f"  lst[mid] == 1 → Move left: high = mid - 1")
            high = mid - 1
        
        step += 1
        print(f"  After move: low={low}, high={high}\n")

    print(f"Search finished: low={low}, high={high}")
    
    if low < len(lst) and lst[low] == 1:
        count = len(lst) - low
        print(f"First 1 found at index {low}, number of 1s = {count}")
        return count
    else:
        print(f"No 1s found.")
        return 0
lst = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(lst))
# Expected Output: 3