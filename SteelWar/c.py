import string

c = 'uno due tre'

def sos(c):
	a = True
	n = 1
	n2 = len(c)
	while a:
		if n == n2: a = False
		print n
		if c[n-1] == ' ': 
			c = c[0:n-1] + '\\ ' + c[n:]
			print c
			n += 2
		else: n += 1
	return c
	

print sos(c)