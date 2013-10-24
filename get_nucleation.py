#!/usr/bin/env python

import sys
import numpy
import re
import os

DNA_LENGTH     =14
CYCLE          =3000
count_matrix   =numpy.zeros(DNA_LENGTH,numpy.int32)
succeed_matrix =numpy.zeros(DNA_LENGTH,numpy.int32)
log_file = "nucleation.log"
fp2=open(log_file,'w')

for i in range(CYCLE):
	if os.path.isfile("%d/reach.dat" %i) and os.path.isfile("%d/got.dat" %i):
		print "found data file in %d" %i
		count_temp   = numpy.genfromtxt("%d/reach.dat" %i)
		succeed_temp = numpy.genfromtxt("%d/got.dat" %i)
	else:
		count_temp   =numpy.zeros(DNA_LENGTH,numpy.int32)
		succeed_temp =numpy.zeros(DNA_LENGTH,numpy.int32)
		try:
			fp=open("%d/hb.dat" %i,'r')
			print "loading file %d/hb.dat" %i
		except:
			continue
		lines = fp.readlines()
		fp.close()
		FOUND_INDICATOR=False
		# COLSE_INDICATOR=True
		BIGGEST_BASEPAIRS=0
		base_pairs=list()
		for mm,line in enumerate(lines):
			temp=line.split()	

			if (int(temp[1])>DNA_LENGTH-2 and int(temp[1]) < DNA_LENGTH+2) and FOUND_INDICATOR == False:
				if int(temp[0]) > BIGGEST_BASEPAIRS:
					BIGGEST_BASEPAIRS = int(temp[0])
					# print mm,line,
				# print temp[2]
				# for x in range(len(base_pairs)/2):
					# count_temp[int(base_pairs[2*x]),int(base_pairs[2*x+1])-DNA_LENGTH] += 1
				FOUND_INDICATOR = True
				# COLSE_INDICATOR = False

			elif (int(temp[1])>DNA_LENGTH-2 and int(temp[1]) < DNA_LENGTH+2) and FOUND_INDICATOR == True:
				# print mm,line,
				if int(temp[0]) > BIGGEST_BASEPAIRS:
					# print int(temp[0]),BIGGEST_BASEPAIRS
					BIGGEST_BASEPAIRS = int(temp[0])
						# if int(base_pairs[2*i])+int(base_pairs[2*i+1]) < 10+DNA_LENGTH:
						# 	print "Here you are. %d" %i
						# 	sys.exit()

					# COLSE_INDICATOR=True
					# FOUND_INDICATOR=False

			elif int(temp[1]) == 0 and FOUND_INDICATOR == True:
				if BIGGEST_BASEPAIRS > DNA_LENGTH -3:
					for x in range(DNA_LENGTH):
						succeed_temp[x] += 1
						count_temp[x] += 1
				else:
					for x in range(BIGGEST_BASEPAIRS):
						count_temp[x] += 1
				# COLSE_INDICATOR = True
				FOUND_INDICATOR = False
				BIGGEST_BASEPAIRS = 0

		if BIGGEST_BASEPAIRS > DNA_LENGTH -3:
			if BIGGEST_BASEPAIRS > DNA_LENGTH -3:
				for x in range(DNA_LENGTH):
					succeed_temp[x] += 1
					count_temp[x] += 1			

			# else:
			# 	pass

		numpy.savetxt("%d/reach.dat" %i,count_temp,fmt="%d")
		numpy.savetxt("%d/got.dat" %i,succeed_temp,fmt="%d")

	count_matrix += count_temp
	succeed_matrix += succeed_temp

	if i % 10 ==0:
		for x in range(DNA_LENGTH):
			print "%6d" %count_matrix[x],
		print
		for x in range(DNA_LENGTH):
			print "%6d" %succeed_matrix[x],
		# print "*"*60
		print 
		fp2.write("%10d    " %i)
		for x in range(DNA_LENGTH):
			print "%6.3f" %(succeed_matrix[x]*1.0/count_matrix[x]),
			fp2.write("%6.3f" %(succeed_matrix[x]*1.0/count_matrix[x]))
		fp2.write("\n")
		fp2.flush()
		print

fp2.close()





