from matplotlib.pylab import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy

data=numpy.genfromtxt("blabla")
matplotlib.rcParams.update({'font.size': 16})

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111)
# axins = inset_axes(ax,
#                     width="50%", # width = 10% of parent_bbox width
#                     height="50%", # height : 50%
#                     loc=1)
# axins.xaxis.set_ticks_position("bottom")
# xx=axes([0.1,0.1,36,0.9])
(a,b)=numpy.shape(data)
caxx = ax.matshow(data,extent=[15.5, 0.5, 15.5, 0.5],aspect=1)
# caxx = ax.matshow(data[1:,1:],extent=[0.5, 38.5, 10.5, 0.5])
# margins(0.2,0.2)
ax.set_xlabel('sequence 2')
ax.set_ylabel('sequence 1')
ax.set_xticks(range(1,16))
ax.set_yticks(range(1,16))
ax.set_xticklabels(['G','G','A','G','G','T','C','T','T','T','G','A','G','G','A'])
ax.set_yticklabels(['C','C','T','C','C','A','G','A','A','A','C','T','C','C','T'])
caxx.axes.xaxis.set_label_position("bottom")
caxx.axes.xaxis.set_ticks_position('bottom')


cax = axes([0.86, 0.152, 0.03, 0.75])
# colorbar(caxx)
fig.colorbar(caxx,cax=cax,ticks=[0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1])


subplots_adjust(left=0.1, right=0.85, top=0.9, bottom=0.15)
# colorbar()
# show()
savefig('test.pdf', format='pdf',dpi=600) 
