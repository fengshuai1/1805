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
	elif a == 3:
		b = input('请输入你要修改的姓名：')
		if b in list:
			position = list.index(b)
			b = input('请输入你要的新姓名：')
			list[position] = b
		else:
			print('查无此人')
	elif a == 4:
		b = input('请输入你要查找的姓名：')
		if b in list:
			position = list.index(b)
			print("你要查的人的索引是%d"%position)
			print(list)
