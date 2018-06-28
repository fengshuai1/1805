list = [20,32,1,4,79,6]
#list.sort系统默认的排
for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)
