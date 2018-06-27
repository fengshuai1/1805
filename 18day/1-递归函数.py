def calnum(num):
	if num == 1:
		return num
	else:
		return num*calnum(num-1)
a = calnum(5)
print(a)
