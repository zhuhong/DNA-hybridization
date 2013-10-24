#!/usr/bin/env python

import subprocess 
import os
import sys
import shutil
import math
import random
import datetime
import time

BEGIN = 0
END   = 300

PROCESS=8
oxdna_path="~/oxDNA-modify/src-metadynamics/Release/oxDNA-metadynamics"
in_file="../inputMD"
top_file="../generated.top"
log_file="log"


j = BEGIN
pf=list()
while (j<END):
	di="%d" %(j)
	if not os.path.exists(di):
		os.mkdir(di)
	else:
		shutil.rmtree(di)
		os.mkdir(di)
	os.chdir(di)
	temp_infile="inputMD"
	temp_topfile="generated.top"
	temp_conffile="generated.dat"
	if os.path.exists(in_file):
		shutil.copyfile(in_file,temp_infile)
		shutil.copyfile(top_file,temp_topfile)
		conf_file = "../conf_source/%d.conf" %(random.randint(0,1999))
		shutil.copyfile(conf_file,temp_conffile)
		fp=open(temp_infile,'a')
		bla=random.randint(1,10000)
		temp_string="seed                 = %d\n" %bla
		fp.write(temp_string)
		fp.close()
	else:
		print "Error: no input found."
		sys.exit()
	commd="%s %s > %s" %(oxdna_path,temp_infile,log_file)
	d=datetime.datetime.now()
	print "%s, Replica %d" %(d.isoformat(),j)
	sys.stdout.flush()
	pf.append(subprocess.Popen(commd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True))
	os.chdir("../")
	j += 1

	while(True):
		time.sleep(10)
		# print len(pf)

		for p in pf:
			if p.poll() is not None:
				pf.remove(p)
				d=datetime.datetime.now()
				print "%s, remove a process" %(d.isoformat())
		if len(pf) < PROCESS:
			break

