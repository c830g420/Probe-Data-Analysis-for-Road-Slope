from datetime import datetime, date, time
from collections import defaultdict

from Node import Node
from Link import Link
from GerMap import GerMap
from Probe import Probe


class ReadFile:
	def __init__(self, filedir):
		self.dir = filedir
		self.file = open(filedir, 'r', encoding = 'utf8')
		# self.line = filedir

	def readLinks(self):

		mp = GerMap()
		
		line = self.file.readline()
		while len(line):
			
			ftrs = line.split(',')
			latlonst1 =[ll.split('/') for ll in ftrs[14].split('|')]
			latlons = list()
			for ll in latlonst1:
				sl0 = float(ll[0])
				sl1 = float(ll[1])
				if len(ll[2]):
					sl2 = float(ll[2])
				else:
					sl2 = 0
				latlons.append((sl0, sl1, sl2))
			rnode = Node(int(ftrs[1]), latlons[0][0], latlons[0][1], latlons[0][2])
			nrnode = Node(int(ftrs[2]), latlons[-1][0], latlons[-1][1], latlons[-1][2])
			link = Link(int(ftrs[0]), rnode, nrnode, float(ftrs[3]))
			# def setShape(self, lat, lon, elev = None):
			for i in range(1, len(latlons) - 1):
				link.setShape(latlons[i][0], latlons[i][1], latlons[i][2])

			if len(ftrs[15]):
				dstcurt1 =[ll.split('/') for ll in ftrs[15].split('|')]
				dstcurs = list()
				for ll in dstcurt1:
					sl0 = float(ll[0])
					sl1 = float(ll[1])
					dstcurs.append((sl0, sl1))
				# def setCurvature(self, dist, curvature):
				for d, c in dstcurs:
					link.setCurvature(d, c)

			if len(ftrs[16]) > 1:
				dstslpt1 =[ll.split('/') for ll in ftrs[16].split('|')]
				dstslps = list()
				for ll in dstslpt1:
					sl0 = float(ll[0])
					sl1 = float(ll[1])
					dstslps.append((sl0, sl1))
				# def setSlope(self, dist, curvature):
				for d, s in dstslps:
					link.setSlope(d, s)
			mp.addLink(link)

			line = self.file.readline()

		# self.line = self.dir

		return mp

	def readProbes(self, maxlength = 5000):
		prbs = defaultdict(list)
		# (self, sid ,  dtime, scode = 13,latitude, longitude, altitude, spd, hding):
		for i in range(maxlength):
			line = self.file.readline()
			if line:
				# '3496,6/12/2009 6:12:49 AM,13,51.496868217364,9.38602223061025,200,23,339\n'
				ftrs = line.split(',')
				sid = int(ftrs[0])
				# 3496
				dtt1 = ftrs[1].split()
				# [6/12/2009, 6:12:49, AM]
				dt2 = dtt1[0].split('/')
				# [6,12,2009]
				d = date(int(dt2[2]), int(dt2[0]), int(dt2[1]))

				tt3 = dtt1[1].split(':')
				# [6,12,49]
				if dtt1[-1] == 'AM' or int(tt3[0]) == 12:
					t = time(int(tt3[0]), int(tt3[1]), int(tt3[2]))
				elif dtt1[-1] == 'PM':
					t = time(int(tt3[0]) + 12, int(tt3[1]), int(tt3[2]))
				else: 
					continue
				dt = datetime.combine(d, t)
				# scode = int(ftrs[2])
				# latitude = float(ftrs[3])
				# longitude = float(ftrs[4])
				# altitude = float(ftrs[5])
				# spd = float(ftrs[6])
				prb = Probe(sid, dt, int(ftrs[2]), float(ftrs[3]), float(ftrs[4]), float(ftrs[5]), float(ftrs[6]), float(ftrs[7]))
				prbs[sid].append(prb)
			else:
				return prbs

		

		return prbs






