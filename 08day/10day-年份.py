a = int(input("请输入年份"))
if (a % 4 == 0 and a % 100 == 0) or (a % 400 == 0):
	print("平年")
else:
	print("闰年")
