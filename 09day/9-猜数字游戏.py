import random
i = 0
a = random.randint(1,100)#电脑
while i <= 10:
	b = int(input("请输入数字"))
	if b > a:
		print("数大了")
	elif b < a:
		print("数小了")
	else:
		print("猜对了")
		i = 10
	i+=1
