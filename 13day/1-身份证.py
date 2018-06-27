id_card = {"name":"冯帅","sex":"男","出生年月":"1990.12.13",}
'''
print(id_card)
id_card["name"] = "小丑"
print(id_card)
id_card.setdefault("name")
print(id_card.get("name"))
id_card["aaa"] = "女"
print(id_card)
id_card.pop("aaa")
print(id_card)
d = {"qq":"ww","aa":"ss"}
id_card.update(d)
print(id_card)
'''
for k,v in id_card.items():
	print(k,v)
