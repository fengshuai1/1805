list = []
print("名片管理系统".center(50,"*"))
while True:
	print("1:添加名片".center(50,"*"))
	print("2:查找名片".center(50,"*"))
	print("3:修改名片".center(50,"*"))
	print("4:删除名片".center(50,"*"))
	print("5:退出".center(50,"*"))
	num = int(input("请选择功能"))
	if num == 1:
		good = {}#空字典
		while True:
			name = input("请输入要添加的名字")
			if len(name) > 4:
				print("太长，请重新输入")
				continue
			z = input("请输入要添加的职位")
			if len(z) > 4:
				print("太长，请重新输入")
				continue
			phone = input("请输入手机号")
			if len(phone) != 11 or phone.startswith("1") == False:
				print("手机号输入有误，请重新输入")
				continue
			good["name"] = name
			good["z"] = z
			#添加到列表
			list.append(good)
			print("添加成功")
			break
	elif num == 2:
		name = input("请输入你要查找的名字")
		flag = False#假设没找到
		for n in list:
			if name == n["name"]:
				print("姓名:%s\n职位:%s\n"%(n["name"],z))
				flag = True#找到了
				break
			if flag == False:
				print("查无此人")
	elif num ==3:
		#改之前，得先查到你要找到的那个
		name = input("请输入要修改条件的名字")
		flag = False#假设没成功
		for n in list:
			if name == n["name"]:
				print("1:修改名字")
				print("2:修改职位")
				print("3:修改名字和职位")
				num = int(input("请选择功能"))
				if num == 1:
					name = input("请输入新名字")
					n["name"]=name
				elif num == 2:
					z = input("请输入新职位")
					n["z"]=z
				elif num == 3:
					name = input("请输入新名字")
					z = input("请输入新职位")
					n["name"]=name
					n["z"]=z
				flag = True
				break
			if flag == False:
				print("查无此人")
		print(list)
	elif num == 4:
		name = input("请输入你要删除的名字")
		for position,l in enumerate(list):#把索引遍历出来
			if name == l["name"]:
				list.pop(position)#直接删除
				name=input("删除成功")
				print(list)
				break
	elif num == 5:#打印名片
		print('名字\t职位\t电话')
		for i in list:
			print(" "+i["name"]+"\t"+i["z"]+"\t"+i["phone"])
		break
