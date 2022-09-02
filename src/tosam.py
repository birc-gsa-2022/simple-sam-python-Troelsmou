import argparse
import sys

parser = argparse.ArgumentParser(prog = "tosam")
parser.add_argument("-path", nargs = 1, type = str)

args = parser.parse_args()

file_object = open(r"{path}".format(path=args.path[0]), "r")

listy = list()
for line in file_object:
	listy.append(line.strip().split("\t"))

for i in listy:
	readname = i[1]
	refname = i[0]
	position = i[3]
	CIGAR = str(len(i[2])) + "M"
	readstring = i[2]
	sys.stdout.write(readname + "\t" + refname + "\t" + position + "\t" + CIGAR + "\t" + readstring + "\n")