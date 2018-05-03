import base64

def safe_base64(s):
	return base64.b64decode(s + '='*(4-len(s)%4))



if __name__ == '__main__':
	result = safe_base64("YWJjZA")
	print result