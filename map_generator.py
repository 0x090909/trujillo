# this script creates the mapping for original file-names
# to the corrisponding hashes

from os import listdir
from os.path import isfile, join


def list_files(mypath):
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	for static in onlyfiles:
		print(static)


if __name__=="__main__":
	mypath = "./example/static" #this is the location of the static files you want to publish on CDN


