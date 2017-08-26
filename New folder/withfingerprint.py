import math
from os import listdir
def remove_special(s):
	k=''
	for i in s:
		if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95:# or ord(i)==32:
			k=k+i
		else:
			pass
	return k


class fileread:
	d_files={}
	dictionary={}
	euclid_value={}
	def __init__(self,name):
		self.name=name
		self.s=files[self.name]
		
		if self.name in fileread.d_files:
			pass
		else:
			k=remove_special(self.s)[::]
			fileread.d_files[self.name]=k

			self.l=self.s.split()
			y={}
			for i in self.l:
				if i in y:
					y[i]+=1
				else:
					y[i]=1
			value=y.values()
			s=0
			for i in value:
				s=s+(i*i)
			fileread.euclid_value[self.name]=math.sqrt(s)
			fileread.dictionary[self.name]=y



class bag:
	l=[]
	def __init__(self,one,two):
		self.one=one
		# print(two)
		a=fileread.dictionary[self.one]
		b=fileread.dictionary[two]
		vec_sum=[]
		for i in a:
			if i in b:
				z=a[i]*b[i]
				vec_sum.append(z)
		try:
			plag=sum(vec_sum)/(fileread.euclid_value[self.one]*fileread.euclid_value[two])
		except:
			plag=0
		bag.l.append(round(plag,5)*100)

class long_same_substring:
	l=[]
	def __init__(self,one,two):
		self.one=one


		a=fileread.d_files[self.one]
		len1=len(a)
		b=fileread.d_files[two]
		len2=len(b)
		if len(a)==0 or len(b)==0:
			max_string=''
		else:

			if a==b:
				max_string=a[::]
			else:

				max_string=''
				string=a[0]
				index1=0
				index2=0
				while index1<len(a) and index2<len(b):
					while True:
						if string in b:
							index2+=1
							if index2>=len(b):
								break
							if len(max_string)<=len(string):
								max_string=string[:]
							if index1+index2<len(a):
								string=string[::]+a[index1+index2]
						else:
							index1+=1
							if index1>=len(a):
								break
							index2=0
							string=a[index1]

		
		# print('long=',max_string)

		try:
			plag_string=((len(max_string)*2)/(len1+len2))*100
		except:
			plag_string=0
		z=round(plag_string,3)
		long_same_substring.l.append(z)

class fingerprint():
	l=[]
	def __init__(self,one,two):
		self.one=one
		a=fileread.d_files[self.one]
		parting1=[]
		k=5
		i=0
		while i<(len(a)-4):
			parting1.append(((ord(a[i])*(10**4))+(ord(a[i+1])*(10**3))+(ord(a[i+2])*(10**2))+(ord(a[i+3])*(10**1))+(ord(a[i+4])*(10**0)))%10007)
			i+=1
		pair_list1=[]
		i=0
		while i <(len(a)-4):
			pair_list1.append(parting1[i:i+5])
			i+=5
		min_list1=[]
		i=0
		while i<len(pair_list1)-1:
			min_list1.append(min(min(pair_list1[i]),min(pair_list1[i+1])))
			i+=2


		b=fileread.d_files[two]
		parting2=[]
		k=5
		i=0
		while i<(len(b)-4):
			parting2.append(((ord(b[i])*(10**4))+(ord(b[i+1])*(10**3))+(ord(b[i+2])*(10**2))+(ord(b[i+3])*(10**1))+(ord(b[i+4])*(10**0)))%10007)
			i+=1
		pair_list2=[]
		i=0
		while i <(len(b)-4):
			pair_list2.append(parting2[i:i+5])
			i+=5
		min_list2=[]
		i=0
		while i<len(pair_list2)-1:
			min_list2.append(min(min(pair_list2[i]),min(pair_list2[i+1])))
			i+=2
		# if len(min_list1)>len(min_list2):
		# 	list_range=len(min_list2)
		# 	list1=min_list2[::]
		# 	list2=min_list1[]::
		# else:
		# 	list_range=len(min_list1)
		# 	list1=min_list1[::]
		# 	list2=min_list2[]::

		# list_range=min(len(min_list1),len(min_list2))
		count=0

		for i in min_list1:
			if i in min_list2:
				count+=1
		# print('count=',count)
		try:
			z=(count*2/(len(min_list1)+len(min_list2)))*100
		except:
			z=0
		z=round(z,3)
		fingerprint.l.append(z)



def print_matrix(n):
	mat=[]
	ty=[]
	for i in n:
		if len(ty)==len(files):
			mat.append(ty)
			ty=[i]
		else:
			ty.append(i)
	mat.append(ty)
	# print(mat)
	print(' '*len(max(files)),'   ',end='')
	for i in files:
		print(i,'   ',end='')
	print('')
	nm=0
	for j in files:
		print(j,'  ',end='')
		for k in mat[nm]:
			print("{:10.2f}".format(k),'  ',end='')
		print('')
		nm+=1

		



path='C:/Users/suraj kumar/Desktop/plag_project/Plagiarism_Detector'
files={p:open(p).read() for p in listdir(path) if p.endswith('.txt')}

for i in files:
	fileread(i)

for i in files:
	for j in files:

		bag(i,j)
		long_same_substring(i,j)
		fingerprint(i,j)

print('Plagiarism : Bag of Words'.center(130, ' '))
print(' ')
print_matrix(bag.l)
print('-'*len(max(files))*14)
print(' ')
print('Plagiarism : LCS'.center(130, ' '))
print(' ')
print_matrix(long_same_substring.l)
print('-'*len(max(files))*14)
print(' ')
print('Plagiarism : Fingerprint'.center(130, ' '))
print(' ')
print_matrix(fingerprint.l)
