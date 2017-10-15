def nameCheck(string):
	s1 = string[0].upper()
	s2 = string[1:].lower()
	return s1 + s2

result = map(nameCheck, ['adam', 'LISA', 'barT'])
print result

