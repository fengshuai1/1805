list = ["a","b","c","a"]#有序
name = input("请输入你要查的名字")
#position = list.index(name)
#第一种做法
'''
count = 0#记录找的次数
fon i in list:
	if name == i:
		print("找到了索引是%d"%count)
	count += 1
'''
#第二种做法
for position,i in enumerate(list):
	if name == i:
		print(position,i)
