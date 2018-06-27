def fanc1(n):
	for i in range(1,n):
		for j in range(1,i+1):
			yield("{0}*{1}={2}".format(j,i,j*i))
		print("\n")
for i in fanc1(10):
	print(i)
