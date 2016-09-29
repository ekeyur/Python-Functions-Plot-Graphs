from sys import argv
script, filename = argv
myfile = open(filename)
file_lines = myfile.readlines()
print len(file_lines)
