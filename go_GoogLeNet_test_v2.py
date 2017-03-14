#!/usr/bin/python
import subprocess
import sys, getopt
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def main(argv):
	inputfile = ''
	modelfile = "testing/googlenet_trial2_basic_iter_40000.caffemodel"
	try:
		opts, args = getopt.getopt(argv,"hi:",["ifile="])
	except getopt.GetoptError:
		print '\nUsage: ./python go_GoogLeNet_test_v2.py -i <image.jpg>\n'
		sys.exit(2)

	if not opts:
		print '\nUsage: ./python go_GoogLeNet_test_v2.py -i <image.jpg>\n'
		sys.exit(2)

	for opt,arg in opts:
	    if opt in ("-i", "--ifile"):
	        inputfile = arg
       
		cmd = subprocess.Popen('testing/classification.bin testing/deploy_g.prototxt %s testing/project_mean.binaryproto testing/numbered_14.txt %s' % (modelfile, inputfile), shell = True, stdout=subprocess.PIPE);
		i = 0
		qflag = 0
		for line in cmd.stdout:
			i = i+1
			print line
			if(i == 2):
				part1,part2 = line.split("-")
				fpart1 = float(part1)
				if abs(fpart1) > 0.9:
					qflag = 1						
		if(qflag == 0):		
			title = 'Image does not belong to top-1 category of the class'
			print title	
			image = mpimg.imread(inputfile)
			plt.axis("off")
			plt.imshow(image)
			plt.title(title)
			plt.show()

		else:
			part3,part4 = part2.split()
			part5 = part4.split('"')
			part6 = part3.split('"')
			print "Image belongs to class %s whose label is %s" % (part5[0],part6[1])	
			with open('info.csv','rb') as f:
				reader = csv.reader(f)
				for row in reader:
					if(row[0] == part5[0]):
						print row[1]
				print '\n'		
			f.close()

			image = mpimg.imread(inputfile)
			plt.axis("off")
			plt.imshow(image)
			title = "Must be " + part6[1];
			plt.title(title)
			xlabel = row[1]
			#plt.text(-100, 100, xlabel)
			plt.show()
	
if __name__ == "__main__":
   main(sys.argv[1:])
