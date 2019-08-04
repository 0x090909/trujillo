# this script creates the mapping for original file-names
# to the corrisponding hashes

from os import listdir, popen
from os.path import isfile, join
import sys

def get_hash(filepath):
	#ipfs add filepath | cut -f 2 -d " "
	print(filepath)
	executed = popen('ipfs add "' + filepath + '" | cut -f2 -d " "').read().split("\n")[0]
	return (executed)

def list_files(mypath):
	onlyfiles = [mypath+f for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles


if __name__=="__main__":
	mypath = sys.argv[1] #this is the location of the static files you want to publish on CDN
	files = list_files(mypath)
	mapping = dict()
	for file in files:
		mapping[file] = get_hash(file)

	print(mapping)
