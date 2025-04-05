# Recursion

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)