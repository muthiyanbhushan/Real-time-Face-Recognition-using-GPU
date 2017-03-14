import signal
import time
import sys
import subprocess
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def run_program():
    proc = subprocess.Popen('testing/cascadeclassifier --cascade testing/haarcascade_frontalface_default.xml --camera 1', shell = True, stdout=subprocess.PIPE);
    while True:
        continue

def run_program2():
	inputfile = "roi.jpg";
	modelfile = "testing/googlenet_trial2_basic_iter_40000.caffemodel";
    
	cmd = subprocess.Popen('testing/classification.bin testing/deploy_g.prototxt %s testing/project_mean.binaryproto testing/numbered_14.txt %s' % (modelfile, inputfile), shell = True, stdout=subprocess.PIPE)
	i = 0
	qflag = 0 
	for line in cmd.stdout:
		i = i+1
		print line
		if(i == 2):
			part1,part2 = line.split("-")
			fpart1 = float(part1)
			if abs(fpart1) > 0.7:
				qflag = 1

	if(qflag == 0):	
		title1 = 'Image does not belong to top-1 category of the class'	
		print title1
		image = mpimg.imread(inputfile)
		plt.axis("off")
		plt.imshow(image)
		plt.title(title1)
		plt.show()

	else:
		part3,part4 = part2.split()
		part5 = part4.split('"')
		part6 = part3.split('"')
		print "Image belongs to class %s whose label is %s" % (part5[0],part6[1])
		print '\n\n'	
        	with open('info.csv','rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if(row[0] == part5[0]):
					print row[1]
			print '\n\n'		
		
		f.close()
		
		image = mpimg.imread(inputfile)
		plt.axis("off")
		plt.imshow(image)
		title = "Must be " + part6[1];
		plt.title(title)
		xlabel = row[1]
		#plt.text(-100, 100, xlabel)
		plt.show()


    

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nClassify who it is? (y/n)> ").lower().startswith('y'):
            run_program2();
            time.sleep(3);
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
