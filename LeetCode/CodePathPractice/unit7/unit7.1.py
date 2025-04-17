# Recursion

def repeat_hello(n):
	if n > 0:
		print("Hello", n)
    
		repeat_hello(n - 1)
		
repeat_hello(5)



def count_recursive(num):
    # Action to repeat
    print(f"Count {num}!")

    # Base Case: If num is 1 we want to stop counting down
    if num == 1:
        # Terminate the function by returning
        return

    # Recursive Case: If num is larger than 1
    else:
       # Call count_recursive() again, but decrement the input value by 1
       count_recursive(num - 1)