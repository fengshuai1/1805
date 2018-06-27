list = []#全局变量
def su():
	for i in range(2,101):
		#i 49
		#i 5
		flag = False
		for j in range(2,i):#验证我的假设
			if i%j == 0:
				flag = True
				break
		if flag == False:#假设成立
			list.append(i)
su()
print(list)
