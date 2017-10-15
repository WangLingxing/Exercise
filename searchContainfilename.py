import os,sys

search_name = sys.argv

start_path = os.path.abspath('.')

def search(name, path):
	for i in os.listdir(path):
		current_path = os.path.join(path, i)
		if os.path.isfile(current_path) and name in i:
			print current_path
		elif os.path.isdir(current_path):
			search(name, current_path)

if __name__ == '__main__':
	search(search_name[1], start_path)