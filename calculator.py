def add(a, b):
  return a+b
  
def subtract(a, b):
  return a-b

def multiply(a, b):
 	return a*b

def devide_new(a, b):
	return a/b

def get_Median(a, b):
	return (a*b)/2

def get_Sum_ver1(n):
	return n(n+1)/2

def get_Sum_ver2(n):
	sum = 0

	for i in range(1, n+1):
		sum = sum + i

	return sum

def factorial(n):
	sum = 1

	for i in range(1,i):
		sum = sum * i
	return sum