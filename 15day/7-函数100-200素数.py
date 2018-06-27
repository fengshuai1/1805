#coding=utf-8
#函数用于判断某一个数是不是素数
def test(num):
	list = [] #定义列表，用于存储计算
	i = num -1#去除本身
	while i > 1:#去除1
		if num%i == 0: #判断是否有余数
			list.append(i)#将所以有的能整除它数加入列表
		i -= 1
	if len(list) == 0:#如果列表为空，就是表示除了1个它本身能整除
		print(num,end=" ")

#此函数用于判断计算出需要判断的所有数字100～200
def test2(star_num,and_num):
	j = star_num
	while j < and_num:
		test(j)
		j += 1

test2(100,200)
print("")
