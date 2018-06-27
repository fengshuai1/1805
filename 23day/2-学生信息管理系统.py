#添加学员函数
def add_student():  
  
    name = input('请输入学员的姓名:')  
    age = int(input('请输入学员的年龄:'))
    sex = input('请输入学员的性别:')
    phone = int(input('请输入学员的电话:'))
    student = [name,age,sex,phone]  
    student_list.append(student)  
  
  
# 查询学员函数  
def query_student():  
    # 1.查询所有学员  
    # 2.输入学员的姓名查询学员 得到查询的学员序号  
  
    for x in range(0, len(student_list)):  
        # 根据x的值，取出列表中对应索引的数据  
        student = student_list[x]  
        name = student[0]  
        age = student[1]  
        sex = student[2]  
        phone = student[3]  
  
        print ('序号%s ：姓名%s 年龄%s 性别%s 电话%s'%(x,name,age,sex,phone))  
  
  
# 修改学员函数  
def update_student():  
  
    # 判断是否有学员信息，如果没有，直接结束函数的执行  
    if len(student_list) == 0:  
        print ('没有学员信息，无法进行修改！')  
        # 强制结束函数的执行  
        return  
  
    # 1.查询学员信息  
    query_student()  
    # 2.选择要修改的学员序号  
    num = input('请选择要修改的学员序号:')  
    # 3.转换  
    num = int(num)  
    # 4.判断选择学员的序号是否在范围内  
    while num not in range(0,len(student_list)):  
        num = input('没有该序号，请重新选择：')  
        num = int(num)  
    # 5.根据选择的序号取出对应的学员信息小列表  
    student = student_list[num]  
    new_name = input('请输入修改后的姓名（%s）：'%student[0])  
    new_age = int(input('请输入修改后的年龄（%s）：'%student[1]))  
    new_sex = input('请输入修改后的性别（%s）：'%student[2])  
    new_phone = int(input('请输入修改后的电话（%s）：'%student[3]))  
    # 6.修改小列表中的数据  
    student[0] = new_name  
    student[1] = new_age  
    student[2] = new_sex  
    student[3] = new_phone  
    print ('修改完成')  
  
# 删除学员信息  
# 1.根据学员序号删除  2.删除所有学员 3.根据学员姓名删除  
def delete_student():  
  
    # 判断是否有学员信息，如果没有，直接结束函数的执行  
    if len(student_list) == 0:  
        print ('没有学员信息，无法进行删除！')  
        # 强制结束函数的执行  
        return  
  
    print ('1.根据学员的序号删除')  
    print ('2.删除所有学号')  
    # 选择操作  
    num = input('请选择您的操作：')  
    # 转换  
    num = int(num)  
    while num not in range(1, 3):  
        num = input('没有该选项，请重新选择：')  
        num = int(num)  
    if num == 1:  
        # 1.展示所有信息  
        query_student()  
        index = input('请选择要删除的学员序号:')  
        index = int(index)  
        # 4.判断选择学员的序号是否在范围内  
        while index not in range(0, len(student_list)):  
            index = input('没有该序号，请重新选择：')  
            index = int(index)  
        # 删除指定索引的数据  
        del student_list[index]  
        # student_list.pop(index)  
    else:  
        # 确定删除  
        rs = input('确定要删除所有信息？y(确定)/n(取消):')  
        if rs == 'y':  
            # 删除列表中所有数据  
            student_list.clear()  
        else:  
            print ('删除操作已取消！')  
def save_data():  
    # 1.打开文件  
    file_handle = open('studentv2.txt', mode='w')  
    # 2.写入数据  
    for student in student_list:  
        # for循环取出小列表中的每一条数据，  
        # join() 可以使用某个字符，将列表中的数据拼接为一个字符串  
        s = ' '.join(student)  
        # 写入  
        file_handle.write(s)  
        file_handle.write('\n')  
    file_handle.close()  
# 读取数据  
# 引入os模块  
import os  
  
def read_date():  
    rs = os.path.exists('studentv2.txt')  
    if rs == True:  
        file_handle = open('studentv2.txt', mode='r')  
        contents = file_handle.readlines()  
        for msg in contents:  
            msg = msg.strip('\n')  
            student = msg.split(' ')  
            student_list.append(student)  
  
  
  
  
# 声明一个大列表，存放所有学员的信息  
student_list = []  
read_date()  
  
while True:  
    print ('******学员管理系统v2.0******')  
    print ('****** 出品人：feng shuai ******')  
    print ('*    *   1.添加学员   *    *')  
    print ('*    *   2.修改学员   *    *')  
    print ('*    *   3.查询学员   *    *')  
    print ('*    *   4.删除学员   *    *')  
    print ('*    *   0.退出程序   *    *')  
    print ('***************************')  
    print ('***************************')  
    # 选择操作  
    num = input('请选择您的操作：')  
    # 转换  
    num = int(num)  
    # 如果选择的数字不在0~5（不含5），重新选择  
    while num not in range(0, 5):  
        num = input('没有该选项，请重新选择：')  
        num = int(num)  
    #添加    2.添加完一个后可以再接着添加  
    if num == 1:  
        add_student()  
        #while True:  
  
         #   rs = input('你还想再接着添加吗？y（继续）/ n(结束):')  
          #  if rs == 'y':  
                    #  
           #     add_student()  
            #else:  
             #   print ('添加结束！')  
              #  break  
        #save_data()  
  
    # 修改  
    elif num == 2:  
        update_student()  
        save_data()  
  
    # 查询  
    elif num == 3:  
        query_student()  
  
    # 删除  
    elif num == 4:  
        delete_student()  
        save_data()  
  
    # 退出  
    else:  
        break  
