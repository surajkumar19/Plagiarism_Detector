import math
import sys
from os import listdir

def remove_special(s):
	''' This function takes a string as input and removes all the
		special symbols/characters contained in the string even spaces except "_" 
		and returns a plain string'''
	k=''
	for i in s:
		if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95:# or ord(i)==32:
			k=k+i
		else:
			pass
	return k


class fileread:
	''' This class gets name of a text file and creates 3 dictonaries 
		1:- containing text name as key and its frequency as value
		2:- containing text name as key and plain text with out any special 
			characters as value
		3:- text name as key and euclid value as value '''
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
	''' This class takes two strings as input and gets the corespondent key 
		value from the dictonary 1 created in the class fileread and plagarism is calculated and
		stored in a list'''
	l=[]
	''' In this function dot product is calculated between the two files importes'''
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
		''' percentage of plagarism is calculated in the below code and appended to the list
			in class'''
		try:
			plag=sum(vec_sum)/(fileread.euclid_value[self.one]*fileread.euclid_value[two])
		except:
			plag=0
		bag.l.append(round(plag,5)*100)

class long_same_substring:
	''' This class takes two strings as inputs and calculates the longest common string between 
		'''
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

		b=fileread.d_files[two]
		parting2=[]
		k=5
		i=0
		while i<(len(b)-4):
			parting2.append(((ord(b[i])*(10**4))+(ord(b[i+1])*(10**3))+(ord(b[i+2])*(10**2))+(ord(b[i+3])*(10**1))+(ord(b[i+4])*(10**0)))%10007)
			i+=1

		set1=list(set(parting1))
		count=0
		for _ in set1:

			indices = [i for i, x in enumerate(parting2) if x == _]
			count=count+len(indices)
		
		try:
			z=(count*2/(len(parting1)+len(parting2)))*100
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
	print(' '*len(max(files)),'     ',end='')
	for i in files:
		print(i,'    ',end='')
	print('')
	nm=0
	for j in files:
		print(j,'  ',end='')
		for k in mat[nm]:
			print("{:10.2f}".format(k),'%  ',end='')
		print('')
		nm+=1

def printall():
	# sys.stdout=('log.txt',"w")

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
	# printall()
	# sys.stdout.close()




####################################### INPUT ####################################
path='C:/Users/suraj kumar/Desktop/plag_project/Plagiarism_Detector'
files={p:open(p).read() for p in listdir(path) if p.endswith('.txt') }

for i in files:
	fileread(i)

for i in files:
	for j in files:

		b=bag(i,j)
		l=long_same_substring(i,j)
		f=fingerprint(i,j)

####################################### OUTPUT ####################################

printall()
