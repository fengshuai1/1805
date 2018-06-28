list = [1,2,3,4,5,6,7,8,9]

min = 0
max = len(list) - 1
a = 8 
while True:
	center = int((min + max)/2)
	if list[center] > a:
		max = max - 1
	elif list[center] < a:
		min = min + 1
	elif list[center] == a:
		print("索引的值%d"%center)
		break
'''
position = list.index(56)
print("值%d"%position)
'''
