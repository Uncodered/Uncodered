# author: Uncodered
# python
print("Star pattern\n")
one = int(input("Enter how many rows do you want to print\n"))
two = bool(int(input("Enter 1 or 0\n")))
if two == True:
	for i in range (0, one+1):
		print("*" * i)
elif two == False:
	for i in range (one, 0, -1):
		print("*" * i)
