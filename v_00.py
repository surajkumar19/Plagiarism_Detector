import math
text1=(open('file2.txt'))
l1=list(text1.read().split())
print(l1)
text2=open('file3.txt')
l2=list(text2.read().split())
print(l2)
d1={}

for i in l1:
	if i in d1:
		d1[i]+=1
	else:
		d1[i]=1
print(d1)
d2={}
for i in l2:
	if i in d2:
		d2[i]+=1
	else:
		d2[i]=1
print(d2)
v1=list(d1.values())
v2=list(d2.values())
x=0
e=[]
for i in v1:
	x=x+i**2
e.append(math.sqrt(x))
# print(e1)
x=0
for i in v2:
	x=x+i**2
e.append(math.sqrt(x))
q=[]
for i in d1:
	if i in d2:
		z=d1[i]*d2[i]
		q.append(z)
print(q)
print(e)
print(sum(q)/(e[0]*e[1]))

