list = []
while True:
	a = int(input("请选择功能:1添加2删除"))
	if a == 1:
		b = input("请输入名字")
		list.append(b)
	elif a == 2:
		b = input("请输入要删除的名字")
		if b in list:
			list.remove(b)
		else:
			print("查无此人")
	print(list)
