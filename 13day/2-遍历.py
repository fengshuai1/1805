list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
for i in list:
	print(i)
	for k,v in i.items():
			for p,j in v.items():
				print(k,p,j)
