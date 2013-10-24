#!/usr/bin/env python

import sys
import numpy
import re
import os

DNA_LENGTH     =14
CYCLE          =3000
count_matrix   =numpy.zeros([DNA_LENGTH,DNA_LENGTH],numpy.int32)
succeed_matrix =numpy.zeros([DNA_LENGTH,DNA_LENGTH],numpy.int32)


for i in range(CYCLE):
	if os.path.isfile("%d/count.dat" %i) and os.path.isfile("%d/succedd.dat" %i):
		print "found data file in %d" %i
		count_temp   = numpy.genfromtxt("%d/count.dat" %i)
		succeed_temp = numpy.genfromtxt("%d/succedd.dat" %i)
		# if numpy.sum(succeed_temp) > 0:
		# 	print i,
		# 	for x in range(DNA_LENGTH):
		# 		for y in range(DNA_LENGTH):
		# 			 if succeed_temp[x,y] > 0:
		# 			 	print "(%d,%d)" %(x,y)
	else:
		count_temp   =numpy.zeros([DNA_LENGTH,DNA_LENGTH],numpy.int32)
		succeed_temp =numpy.zeros([DNA_LENGTH,DNA_LENGTH],numpy.int32)
		try:
			fp=open("%d/hb.dat" %i,'r')
			print "loading file %d/hb.dat" %i
		except:
			continue
		lines = fp.readlines()
		fp.close()
		FOUND_INDICATOR=False
		COLSE_INDICATOR=True
		base_pairs=list()
		for line in lines:
			temp=line.split()	

			if int(temp[1])>0 and FOUND_INDICATOR == False and COLSE_INDICATOR == True:
				try:
					base_pairs=re.split('[)(,]+',temp[2])[1:-1]
				except:
					pass
				# print temp[2]
				for x in range(len(base_pairs)/2):
					count_temp[int(base_pairs[2*x]),int(base_pairs[2*x+1])-DNA_LENGTH] += 1
				FOUND_INDICATOR = True
				COLSE_INDICATOR = False

			elif int(temp[1])>0 and FOUND_INDICATOR == True and COLSE_INDICATOR == False:
				if abs(int(temp[1])-DNA_LENGTH) <2 and int(temp[0]) > DNA_LENGTH/2:
					for x in range(len(base_pairs)/2):
						succeed_temp[int(base_pairs[2*x]),int(base_pairs[2*x+1])-DNA_LENGTH] += 1
						# if int(base_pairs[2*i])+int(base_pairs[2*i+1]) < 10+DNA_LENGTH:
						# 	print "Here you are. %d" %i
						# 	sys.exit()

					COLSE_INDICATOR=True
					# FOUND_INDICATOR=False

			elif int(temp[1]) == 0 and FOUND_INDICATOR == True and COLSE_INDICATOR == False:
				COLSE_INDICATOR = True
				FOUND_INDICATOR = False

			else:
				pass

		numpy.savetxt("%d/count.dat" %i,count_temp,fmt="%d")
		numpy.savetxt("%d/succedd.dat" %i,succeed_temp,fmt="%d")

	count_matrix += count_temp
	succeed_matrix += succeed_temp

for i in range(DNA_LENGTH):
	for j in range(DNA_LENGTH):
		print "%6d" %count_matrix[i,j],
	print
print "*"*60
sum_count=numpy.sum(count_matrix)

for i in range(DNA_LENGTH):
	for j in range(DNA_LENGTH):
		print "%6.4f" %(count_matrix[i,j]*1.0/sum_count),
	print
print "*"*60

for i in range(DNA_LENGTH):
	for j in range(DNA_LENGTH):
		print "%6d" %succeed_matrix[i,j],
	print
print "*"*60


for i in range(DNA_LENGTH):
	for j in range(DNA_LENGTH):
		if count_matrix[i,j] > 0:
			print "%6.4f" %(succeed_matrix[i,j]*1.0/count_matrix[i,j]),
		else:
			print "%6.4f" %(0.0),
	print

print "*"*60

# print succeed_matrix
for i in range(DNA_LENGTH):
	for j in range(DNA_LENGTH):
		if count_matrix[i,j] > 0:
			print "%6.4f" %(succeed_matrix[i,j]*1.0/numpy.sum(succeed_matrix)),
		else:
			print "%6.4f" %(0.0),
	print


