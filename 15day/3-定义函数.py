import time
def game():
	i = 0
	while True:
		i += 1
		if i % 2 == 0:
			time.sleep(1)
			print("我喜欢玩游戏")
		else:
			game1()
def game1():
	print("我喜欢打代码")
game()
		
