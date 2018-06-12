b = int(input("请输入数字"))
a = 0
ouhe = 0
ji = 0
zonghe = 0
while a <= b:
	zonghe = zonghe + a
	if a%2 == 0:
		print("偶数是%d"%a)
		ouhe = ouhe + a
	else:
		print("奇数是%d"%a)
		ji = ji + a
	a = a+ 1
print("偶数的和是%d"%ouhe)
print("奇数和是%d"%ji)
print("总和是%d"%zonghe)
