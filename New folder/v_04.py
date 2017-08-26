import math
from os import listdir
def remove_special(s):
	print(1,s)
	k=''
	for i in s:
		if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95:# or ord(i)==32:
			k=k+i
		else:
			pass
	print(2,k)
	return k


class fileread:
	d_files={}
	dictionary={}
	euclid_value={}
	def __init__(self,name):
		self.name=name
		self.s=open(self.name).read().lower()
		
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
		# print('a=',a)
		b=fileread.d_files[two]
		len2=len(b)
		# print('b=',b)
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

		
		print('long=',max_string)
		# print(max_string)
	 #    # print(max_string,(len(max_string)*2),(len1+len2))
		try:
			plag_string=((len(max_string)*2)/(len1+len2))*100
		except:
			plag_string=0
		z=round(plag_string,3)
		long_same_substring.l.append(z)

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
files=[p for p in listdir(path) if p.endswith('.txt')]
# print(files)
for i in range(len(files)):
	f1=fileread(files[i])
	
	for j in range(len(files)):
		f2=fileread(files[j])

		bag(files[i],files[j])
		long_same_substring(files[i],files[j])

print_matrix(bag.l)

print('-'*len(max(files))*len(files))

print_matrix(long_same_substring.l)

