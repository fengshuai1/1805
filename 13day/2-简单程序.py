names = ["a","b"]
print(names[0])
print(names[1])
for name in names:
	print("hello",name)
tools = ["bike","motor","bus"]
for tool in tools:
	print("I would like to own a Honda motorcycle",tool)
names = ['a','b','c']
for name in names:
	print('invite',name,'to dinner')
names = ['a','b','c']
for i in range(2):
	print('invite',names[i],'to dinner')
print(names[2],'cannot come')
names[2] = 'h'
print('invite',names[2],'to dinner')
names = ['a','b','c']
print('Find big desk')
names.insert(0, 'h')
names.insert(2, 'z')
names.append('t')
for name in names:
	print('Invite to dinner',name)
names = ['a', 'b', 'c']
print('Find big desk')
names.insert(0, 'h')
names.insert(2, 'z')
names.append('t')
print('Sorry desk cannot arrive in time')
while len(names)>2:
    name=names.pop()
    print('Sorry cannot invite',name)
for i in names:
    print('Invite for dinner',i)
while len(names)>0:
    names.remove('h')
    names.remove('a')
print(names)
city = ['Shanghai', 'Guangzhou', 'Beijing', 'Shenzhen']
print(city)
print(sorted(city))
print(city)
print(sorted(city,reverse=True))
print(city)
city.reverse()
print(city)
city.reverse()
print(city)
city.sort()
print(city)
city.sort(reverse=True)
print(city)
names = ['a', 'b', 'c']
print('Invite ',str(len(names)),'people to dinner')
