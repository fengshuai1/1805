print("请输入星期几")
s = input("星期一 星期二 星期三 星期四 星期五 星期六 星期天")
if s == "1"or"2"or"3"or"4"or"5":
	a = input("1上午 2下午")
	if a == "1":
		d = float(input("请输入时间"))
		if d > 8 and d < 10:
			print("正在上课")
		if d > 10 and d < 12:
			print("正在玩游戏")
	if a == "2":
		c = float(input("请输入时间"))
		if c > 14 and c <15:
			print("正在上课")
	else:
		print("除非不知道在干什么")
elif s == "6":
	print("全天上课")
elif s == "7":
	print("逛街")
