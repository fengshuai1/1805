def d_sum(a,b,*args,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
t = (1,2,3,4,5,6)
d = {"args":12,"weight":24}
d_sum(1,2,*t,**d)
sum = 1+2
for i in t:
	sum+=i
for i in d.values():
	sum+=i
print(sum)
