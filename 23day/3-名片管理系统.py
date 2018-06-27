card_list = []	#定义一个空的列表用来储存名片
def print_menu():
	print("="*50)
	print("名片管理系统v0.1".center(50,' '))
	print("1.添加一个名片".center(50,' '))
	print("2.删除一个名片".center(50,' '))
	print("3.修改一个名片".center(50,' '))
	print("4.查询一个名片".center(50,' '))
	print("5.显示所有名片".center(50,' '))
	print("6.退出管理系统".center(50,' '))
	print("="*50)
def add_card_lists():
	new_name = input("请输入一个名字:")
	new_jop = int(input("请输入手机号"))
	new_qq = input("请输入QQ号:")
	new_weixin = input("请输入微信号:")
	new_addr = input("请输入地址:")
	#定义一个新的字典，用来储存一个新的名片
	new_lists = {}
	new_lists["name"] = new_name
	new_lists["jop"] = new_jop
	new_lists["qq"] = new_qq
	new_lists["weixin"] = new_weixin
	new_lists["addr"] = new_addr
	#将字典添加到列表中
	card_list.append(new_lists)
	#print(card_list)	#for test
def dele_card_lists():
	dele_name = input("请输入要删除的姓名:")
	find_flag = 0	#默认表示没有找到
	for temp in card_list:
		if dele_name==temp["name"]:
			find_flag = 1	#表示找到了   
			card_list.remove(temp)
			print("删除成功！")  
			break
	if find_flag==0:
		print("查无此人!")
def update_card_lists():
	update_name = input("请输入要修改的人的姓名：")	#输入要修改的姓名
	find_flag = 0	#默认表示没有找到
	update_flag = 0	#默认修改失败
	sign = 0
	for temp in card_list:
	
		if update_name==temp["name"]:
			find_flag = 1
			print("1.修改姓名")	#打印修改菜单
			print("2.修改手机号")
			print("3.修改QQ")
			print("4.修改微信")
			print("5.修改地址")
			print("6.退出修改")
			while True:
				num2 = int(input("请输入要修改信息的编号：")) 
				if num2==1:
					card_name = input("请输入您要修改后的姓名:")
					temp['name'] = card_name  
					update_flag = 1
				elif num2==2:
					card_jop = input("请输入您要修改后的手机号:")
					temp['jop'] = card_jop
					update_flag = 1
				elif num2==3:
					card_qq = int(input("请输入您要修改后的QQ:"))
					temp['qq'] = card_jop
					update_flag = 1
				elif num2==4:
					card_weixin = input("请输入您修改后的微信:")
					temp['weixin'] = card_weixin
					update_flag = 1
				elif num2==5:
					card_addr = input("请输入您要修改后的地址:")
					temp['addr'] = card_addr
					update_flag = 1
				elif num2==6:
					break
				else:
					print("输入有误，请重新输入:")
				if update_flag==1:                
					print("修改成功！")
				print("")
			break
	if find_flag==0:
		print("查无此人！")
def find_card_lists():
	find_name = input("请输入你要查找的姓名:")
	find_flag = 0	#默认表示没有找到
	for temp in card_list:
		if find_name==temp["name"]:
			print("name:%s\tjop:%d\tqq:%s\tweixin:%s\taddr:%s"%(temp['name'],temp['jop'], temp['qq'], temp['weixin'], temp['addr']))
			find_flag = 1	#表示找到了
			break
	if find_flag==0:
		print("查无此人!")
def show_card_lists():
	print("姓名\t手机号\tQQ\t微信\t地址")
	for temp in card_list:
		print("name:%s\tjop:%d\tqq:%s\tweixin:%s\taddr:%s"%(temp['name'],temp['jop'],temp['qq'],temp['weixin'],temp['addr']))
def main():
	print('欢迎使用名片管理系统'.center(45,"*"))
	while True:
		print_menu()	#添加打印功能提示
		num = int(input("请输入功能序号:"))	#获取用户的选择
		#根据用户的选择执行相应的功能
		if num==1:
			add_card_lists()
		elif num==2:
			dele_card_lists()
		elif num==3:
			update_card_lists()
		elif num==4:
			find_card_lists()
		elif num==5:
			show_card_lists()
		elif num==6:
			break
		else:
			print("你的输入有误，请重新输入！")
		print("")

main()	#调用主函数
