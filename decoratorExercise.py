import functools

def log(text1, text2):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s call %s():' % (text1, func.__name__)
			f = func(*args, **kw)
			print '%s call' % text2
			return f		
		return wrapper
	return decorator

@log('begin', 'end')
def now():
    print 'Hello'

now()