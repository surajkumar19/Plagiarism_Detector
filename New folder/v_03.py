import math
from os import listdir
def fileread(name):
	s=open(name).read()
	s=s.lower()
	l=s.split()
	return l,s

def makedict(x,l):
	global d
	y={}
	for i in l:
		if i in y:
			y[i]+=1
		else:
			y[i]=1
	if x in d:
		pass
	else:
		d[x]=y
	a=0
	
	v=list(y.values())
	for i in v:
		a=a+i**2
	euclid_value[x]=math.sqrt(a)

def bag(x1,x2):
	vec_sum=[]
	for i in d[x1]:
		if i in d[x2]:
			z=d[x1][i]*d[x2][i]
			vec_sum.append(z)
	return vec_sum

def long_string(l1,l2):
	i=0
	z=[]
	m=[]
	while i <len(l1):
		j=0
		while j <len(l2) and i<len(l1):
			if l1[i]==l2[j]:
				z.append(l1[i])
				i+=1
				j+=1
				
				# print(z)
			else:
				z=[]
				j+=1
			if len(m)<len(z):
				m=z
		i+=1
	les=0
	les2=0
	print(m)
	for i in m:
		les=les+len(i)
	for i in l1:
		les2=les2+len(i)
	for i in l2:
		les2=les2+len(i)
	
	print('les:',les,'les2:',les2)
	return ((les*2)/les2)*100


	
	


d={}
path='C:/Users/suraj kumar/Desktop/plag_project/Plagiarism_Detector'

files=[p for p in listdir(path) if p.endswith('.txt')]
print(files)
euclid_value={}
for i in range(len(files)):

	l1,s1=fileread(files[i])
	makedict(files[i],l1)

	for j in range(i+1,len(files)):
		
		l2,s2=fileread(files[j])
		makedict(files[j],l2)
		
		
		dot_product_sum=bag(files[i],files[j])
		t=sum(dot_product_sum)/(euclid_value[files[i]]*euclid_value[files[j]])
		length=long_string(l1,l2)
		print("plagarism string",length,'%')



		print(files[i],'bag',files[j],':-',round(t,4)*100,'%')
		# print(files[i],'string',files[j],':-',(length*2)/(len(s1)+len(s2))*100)
		print('')
		print('')

		print('')



print(d)
print(euclid_value)

