import random
all_money = 0#消费总钱
for i in range(30):#每月30天
	for j in range(1,3):#每天2次
			a = random.randint(1,100)
			if a <= 6:  
				money = 3   
			elif 6 > a and a <= 12:  
				money = 4  
			elif 12 > a and a <= 22:  
				money = 5  
			elif 22 > a and a <= 33:  
				money = 6  
			elif a > 33:  
				money = (a - 33)/20  
			elif money >= 100 and money <= 150:  
				if a <= 6:  
					money = 3*0.8  
				elif 6 > a and a <= 12:  
					money = 4*0.8  
				elif 12 > a and a <= 22:  
					money = 5*0.8  
				elif 22 > a and a <= 33:  
					money = 6*0.8  
				elif a > 33:  
					money = ((a - 33)/20)*0.8  
				elif money >= 150 and money <= 400:  
					if a <= 6:  
						money = 3*0.5  
					elif 6 > a and a <= 12:  
						money = 4*0.5  
					elif 12 > a and a <= 22:  
						money = 5*0.5  
					elif 22 > a and a <= 33:  
						money = 6*0.5  
					elif a > 33:  
						money = ((a - 33)/20)*0.5  
				elif money >= 400 :  
					if a <= 6:    
						money = 3  
					elif 6 > lngth and a <= 12:  
						money = 4  
					elif 12 > a and a <= 22:  
						money = 5  
					elif 22 > a and a <= 33:  
						money = 6  
					elif a >= 33:  
						money = (a - 33)/20
'''
	j +=1
i +=1
'''    
all_money=all_money+money
print("all_money%.02f"%all_money)
