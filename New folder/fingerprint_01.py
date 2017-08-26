def remove_special(s):
	k=''
	for i in s:
		if (ord(i)>47 and ord(i)<58) or (ord(i)>96 and ord(i)<123) or ord(i)==95:# or ord(i)==32:
			k=k+i
		else:
			pass
	return k

a='plagiarism is an act or instance of using or closely imitating the language and thoughts of another author without authorization'
b=remove_special(a)
d1=[]
k=5
i=0
count=1
# print(len(b))
while i<(len(b)-4):
	# print(b[i:i+5])
	d1.append(((ord(b[i])*(10**4))+(ord(b[i+1])*(10**3))+(ord(b[i+2])*(10**2))+(ord(b[i+3])*(10**1))+(ord(b[i+4])*(10**0)))%10007)
	i+=1
pair_list1=[]
i=0
# print(d1)
# print(len(d1))
while i<(len(b)-4)	:
	pair_list1.append(d1[i:i+5])
	i+=5
# print(pair_list1)

min_list1=[]

i=0
while i<len(pair_list1)-1:
	# print(min(pair_list1[i]),min(pair_list1[i+1]))
	min_list1.append(min(min(pair_list1[i]),min(pair_list1[i+1])))
	i=i+2
print(min_list1)

# index_positin1=[]
# for i in min_list1:
# 	index_positin1.append([i,d1.index(i)])
# print(index_positin1)


c='plagiarism is an act of copying the ideas or words of another person without giving credit to that person'
d=remove_special(c)
d2=[]
k=5
i=0
count=1
# print(len(d))
# while i<(len(b)-4):
# 	print(b[i:i+5],'=',count)
# 	count+=1
# 	i+=1

while i<(len(d)-5):
	d2.append(((ord(d[i])*(10**4))+(ord(d[i+1])*(10**3))+(ord(d[i+2])*(10**2))+(ord(d[i+3])*(10**1))+(ord(d[i+4])*(10**0)))%10007)
	i+=1
	
pair_list2=[]
i=0
# print(d2)
# print(len(d1))
while i<(len(d)-4)	:
	pair_list2.append(d2[i:i+5])
	i+=5
# print(pair_list1)

min_list2=[]

i=0
while i<len(pair_list2)-1:
	# print(min(pair_list1[i]),min(pair_list1[i+1]))
	min_list2.append(min(min(pair_list2[i]),min(pair_list2[i+1])))
	i=i+2
print(min_list2)
index_positin2=[]
for i in min_list2:
	index_positin2.append([i,d2.index(i)])
# print(index_positin2)
