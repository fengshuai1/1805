a = 0
list=[]
for i in range(100,201):
	for j in range(2,i):
		if i%j == 0:
			break
	if i == j+1:
		list.append(i)
print(list)
for i in list:
	a +=i
list.reverse()
print(list)
