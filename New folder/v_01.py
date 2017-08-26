from difflib import SequenceMatcher
def longsamesubstring(s1, s2):
    max_string = ""
    len1, len2 = len(s1), len(s2)
    if s1==s2:
    	max_string=s1
    else:
    # print(len1,len2)
	    for i in range(len1):
	        string = ""
	        for j in range(len2):
	            if (i + j < len1 and s1[i + j] == s2[j]):
	                string += s2[j]
	                # print(string)
	            else:
	                # print(len(string),len(max_string))
	                if (len(string) > len(max_string)): 
	                	max_string = string
	                	# print(max_string)
	                string = ""
    return max_string.strip()






def common_start(sa, sb):
    """ returns the longest common substring from the beginning of sa and sb """
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return

    return ''.join(_iter())




text1=open('file2.txt')
# j=text1.read()
s1=text1.read()
l1=list(s1.split())
# print("j=",j,len(j))


print(s1)
text2=open('file5.txt')
s2=str(text2.read())
l2=list(s2.split())
print(s2)
print(longsamesubstring(s1,s2))

# s1 = "apple pie available"
# string2 = "come have some apple pies"

# match = SequenceMatcher(None, s1, s2).find_longest_match(0, len(s1), 0, len(s2))

# # print(match)  # -> Match(a=0, b=15, size=9)
# print(s1[match.a: match.a + match.size])  # -> apple pie

# print(common_start(s1,s2))
# count=0
# m1=0

# s3=''.join(l1)
# s4=''.join(l2)
# print(l1)
# print(l2)

# i=0
# z=[]
# m=[]
# while i <len(l1):
# 	j=0
# 	while j <len(l2) and i<len(l1):
# 		if l1[i]==l2[j]:
# 			z.append(l1[i])
# 			i+=1
# 			j+=1
			
# 			print(z)
# 		else:
# 			z=[]
# 			j+=1
# 		if len(m)<len(z):
# 			m=z
# 	i+=1

# print(m)


# if m1<count:
# 	m1=count
# print(m1)