def bag(l1,l2):
	e=e[:1]
	# print(e)
	
	print(s2)
	d2={}
	for i in l2:
		if i in d2:
			d2[i]+=1
		else:
			d2[i]=1
	print(d2)
	v2=list(d2.values())
	x=0
	for i in v2:
		x=x+i**2
	e.append(x)

def String(l1,l2):
	q=[]
	for i in d1:
		if i in d2:
			z=d1[i]*d2[i]
			q.append(z)
	print('dot product:',q)
	print('euclid value:',e)
	comp.append(sum(q)/(e[0]*e[1]))
	tl=len(s1)+len(s2)
	mul=1
	for i in l1:
	# print(i)
		if i in l2:
			mul=mul*len(i)
	comp2.append(mul/tl)



















text1=open('file3.txt')
s1=text1.read()
l1=list(s1.split())
print(s1)
comp=[]
comp2=[]
d1={}
for i in l1:
	if i in d1:
		d1[i]+=1
	else:
		d1[i]=1
print(d1)
v1=list(d1.values())
x=0
e=[]
for i in v1:
	x=x+i**2
e.append(x)
print('')
print('')
print('')
for i in [2,3,4]:
	# e=e[:1]
	# # print(e)
	x='file'+str(i)+'.txt'
	text2=open(x)
	s2=str(text2.read())
	l2=list(s2.split())
	bag(l1,l2)
	# print(s2)
	# d2={}
	# for i in l2:
	# 	if i in d2:
	# 		d2[i]+=1
	# 	else:
	# 		d2[i]=1
	# print(d2)
	# v2=list(d2.values())
	# x=0
	# for i in v2:
	# 	x=x+i**2
	# e.append(x)
	# q=[]
	# for i in d1:
	# 	if i in d2:
	# 		z=d1[i]*d2[i]
	# 		q.append(z)
	# print('dot product:',q)
	# print('euclid value:',e)
	# comp.append(sum(q)/(e[0]*e[1]))
	# tl=len(s1)+len(s2)
	# mul=1
	# for i in l1:
	# # print(i)
	# 	if i in l2:
	# 		mul=mul*len(i)
	# comp2.append(mul/tl)
	print('')
	print('')
	print('')
print(comp)
print('string check:',comp2)



	




