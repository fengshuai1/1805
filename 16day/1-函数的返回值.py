def a(account,pwd):
	b = isphone(account)
	if b:
		print("呵呵呵呵")
def c(account,pwd):
	b = isphone(account)
	if b:
		print("哈哈哈哈")
def isphone(account):
	if len(account) == 11 and account.startswith("1"):
		return True
	else:
		return False
a(12345678900,122)
c(12345678900,122)
