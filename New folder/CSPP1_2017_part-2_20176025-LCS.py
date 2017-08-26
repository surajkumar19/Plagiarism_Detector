import math
from os import listdir
# def remove_special(s):
# 	k=''
# 	for i in s:
# 		if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95 or ord(i)==32:
# 			k=k+i
# 	return k


class fileread:
	dictionary={}
	euclid_value={}
	def __init__(self,name):
		self.name=name
		self.s=open(self.name).read()
		k=''
		for i in self.s:
			if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95 or ord(i)==32:
				k=k+i
		# k=remove_special(self.s)[::]

		self.ss=k.lower()
		self.l=self.ss.split()
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
		# print(s)
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
	    self.s1=open(self.one).read()
	    k=''
	    for i in self.s1:
	    	if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95 or ord(i)==32:
	    		k=k+i


	    self.ss1=k.lower()
	    s2=open(two).read()
	    k=''
	    for i in s2:
	    	if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95 or ord(i)==32:
	    		k=k+i

	    self.ss=k.lower()
	    ss2=s2.lower()

	    max_string = ""
	    len1, len2 = len(self.ss1), len(ss2)
	    if self.ss1==ss2:
    		max_string=ss2
	    else:
		    for i in range(len1):
		        string = ""
		        for j in range(len2):
		            if (i + j < len1 and self.ss1[i + j] == ss2[j]):
		                string += ss2[j]
		            else:
		                if (len(string) > len(max_string)): 
		                	max_string = string
		                string = ""
	    # print(self.one,' & ',two,' :',max_string.strip())
	    # lis=list(max_string.split())
	    # length=0
	    # for i in lis:
	    # 	length+=len(i)
	    # print(lis)
	    # print(length)
	    # print(max_string)
	    max_string=max_string.strip()
	    # print(max_string,(len(max_string)*2),(len1+len2))
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

print('------------------------')
# for i in long_same_substring.l:
# 	print(i)
print_matrix(long_same_substring.l)
	# mat=[]
	# ty=[]
	# # print(bag.l)
	# for i in long_same_substring.l:
	# 	if len(ty)==len(files):
	# 		mat.append(ty)
	# 		ty=[i]
	# 	else:
	# 		ty.append(i)
	# mat.append(ty)
	# # print(mat)
	# print('             ',end='')
	# for i in files:
	# 	print(i,'   ',end='')
	# print('')
	# nm=0
	# for j in files:
	# 	print(j,'  ',end='')
	# 	for k in mat[nm]:
	# 		print("{:10.3f}".format(k),'  ',end='')
	# 	print('')
	# 	nm+=1





# file1=fileread('file1.txt')
# file2=fileread('file2.txt')
# print(file1.l)
# print(fileread.dictionary)
# bag('file1.txt','file2.txt')
