#声明一个类
class person:
	list = {}
	def add(a):
		name = input('请输入要添加的联系人姓名')
		if name in person.list:
			print('联系人已存在')
		else:
			telephone = input('请输入联系人电话')
			addr = input('请输入联系人地址')
			adds ={'电话':telephone,'地址':addr}
			person.list[name]=adds

	def dele(a):
		name = (input('请输入要删除的联系人姓名'))
		if name in person.list:
			del person.list[name]
			print ("%s"%person.list.items())
		else:
			print('联系人 %s 不存在'%name)
	def search(self):
		name = (input('请输入要搜索的联系人姓名'))
		if name in person.list:
			print('联系人%s的电话号码是%s,地址是%s'%(name,person.list[name]['电话'],person.list[name]['地址']))
		else:
			print('联系人 %s 不存在'%name)
	def modify(self):
		name = (input('请输入要编辑的联系人姓名'))
		if name in person.list:
			telephone = input('请输入联系人电话号码')
			addr = input('请输入联系人地址')
			person.list[name]['电话']=telephone
			person.list[name]['地址']=addr
		else:
			print('联系人%s不存在,若要编辑请选择添加选项'%name)
	def write(self):
		f = open('联系人.txt','wb+')
		p.dump(person.list,f)
		f.close()
	def read(self):
		file = '联系人.txt'
		try:
			f = open(file ,'rb+')
			people.list = p.load(f)
			f.close()
		except:
			f = open(file ,'w')
			f.close()
	def show(self):
		print(person.list)
def menu():
    print('''系统提供以下功能
    1：添加
    2：删除
    3：修改
    4：搜索
    5：退出
    6: 显示全部联系人信息''')
people = person()
people.read()
while True:
	try:
		menu()
		choice = int(input('请输入相应数字操作'))
		if choice == 1:
			people.add()
		elif choice == 2:
			people.dele()
		elif choice == 3:
			people.modify()
		elif choice == 4:
			people.search()
		elif choice == 5:
			people.write()
			break
		elif choice == 6:
			people.show()
		else:
			print('输入不合法，请输入合法数字')
	except ValueError:
		print('请输入数字选项')
