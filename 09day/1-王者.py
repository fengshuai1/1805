i = 0
while i <= 3:
	a = input("请输入账号")
	b = input("请输入密码")
	if a == "fs" and b == "123456":
		print("登录成功")
		print("*"*35)
		e =input("0:ADC 1:肉 2:法师")
		if e == "0":
			print("鲁班大师")
		elif e == "1":
			print("程咬金")
		elif e == "2":
			print("王昭君")
	else:
		print("登录失败")
	i+=1
