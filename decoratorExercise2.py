import functools
import string

def log(text = 'calling'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			msg = string.Template("$time $text $function")
			if callable(text):
				before_msg = msg.substitute({"time":"Before", "text":"calling", "function":text.__name__})
				after_msg = msg.substitute({"time":"After", "text":"calling", "function":text.__name__})
			else:
				before_msg = msg.substitute({"time":"Before", "text":text, "function":func.__name__})
				after_msg = msg.substitute({"time":"After", "text":text, "function":func.__name__})

			print before_msg
			f = func(*args, **kw)
			print after_msg
			return f
		return wrapper
	return decorator(text) if callable(text) else decorator

@log
def f1():
	print 'Hello'

f1()

@log('excute')
def now():
	print 'Hello'

now()


