#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import os
import re
import time

try:
    import argparse
except ImportError:
    from optparse import OptionParser

# distinct dst with srcs (It is csv or txt files commonly.)
def distinct(dst, *srcs):
	data = {}
	
	for src in srcs: 
		f = None
		
		try:
			f = open(src)
			for l in f.xreadlines():
				l = l.lower().strip()
				data[l] = True
		except:
			pass
			
		finally:
			if f is not None:
				f.close()
			
	f = open(dst, 'w')	
	for d in data:
		if d:
			f.write(d)
			f.write('\n')
		
	f.close()

if __name__ == '__main__':
	l_argv = len(sys.argv)
	parser = argparse.ArgumentParser(description='distinct for Python')
	parser.add_argument('dst', metavar='dst', nargs=1, default='output.txt', help='Dst path of file.')
	parser.add_argument('srcs', metavar='srcs', nargs='*', help='Src path of file(s).')
	args = parser.parse_args()

	if l_argv > 2:
		distinct(args.dst[0], args.srcs[0])
	else:
		print(args.accumulate(args.integers))	
	