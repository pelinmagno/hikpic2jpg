import argparse
import os
import sys
import glob

PicFiles = glob.glob('*.pic')
#print('PicFiles {}'.format(PicFiles))
for archivo in PicFiles:
	f=open(archivo,'rb')
	tdata = f.read()
	f.close()
	print(archivo)
	os.path.splitext(archivo)
	nomfile = os.path.splitext(archivo)[0]

	ss = '\xff\xd8'
	se = '\xff\xd9'

	count = 0
	start = 0
	while True:
		x1 = tdata.find(ss,start)
		if x1 < 0:
			break
		x2 = tdata.find(se,x1)
		jpg = tdata[x1:x2+1]
		count += 1
		fname = nomfile + '_' + '%d.jpg' % (count)
		fw = open(fname,'wb')
		fw.write(jpg)
		fw.close()
		start = x2+2