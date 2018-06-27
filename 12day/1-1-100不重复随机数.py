import random
ali = []
a = 0
while len(ali)<10:
	b=random.randint(1,100)
	ali.append(b)
	c=ali[a]
	a=a+1
if ali.count(c)>1:
		ali.pop()
		print("重复")
		a=a-1
print(ali)
