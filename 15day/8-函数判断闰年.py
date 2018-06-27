# 定义函数判断闰年
def year(num):
	# 判断能否整除400，或者（能整除4但是不能整除100）
	if(num % 400 == 0) or ((num % 4 == 0) and (num % 100 !=0)):
		print("%s是闰年"%num)
	else:
		print("%s不是闰年"%num)
while True:
	# 获取输入的年份，转为int
	year_input = int(input("请输入年份是否是闰年"))
# 调用函数判断
year(year_input)
