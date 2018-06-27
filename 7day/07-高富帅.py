input("请选择性别")
sex = input("1:男""2:女")
if sex == "1":
	s = int(input("请输入身高"))
	c = int(input("请输入财富"))
	y = int(input("请输入颜值"))
	if (s >180 and c > 1000) and y >90:
		print("高富帅")
	else:
		print("打印稳住，别哭")
elif sex == "2":
	p = input("请输入皮肤颜色")
	f = int(input("请输入财富"))
	z = int(input("请输入颜值"))
	if p == "白" and f > 800 and z > 90:
		print("白富美")
	else:
		print("哈哈哈")
else:
	print("输入有误")
