import numpy as np
from collections import defaultdict

from Link import Link

class GerMap:
	# bounding rectangle - 50.62500, 8.43751, 53.43750, 11.25000
	def __init__(self):
		self.ERADIUS = 6371000
		self.MAXLAT = 53.4375
		self.MINLAT = 50.6250
		self.MAXLON = 11.25
		self.MINLON = 8.4375
		self.UNIT = 0.003
		self.index = defaultdict(list)
		self.lincolle = dict()

	def calXY(self, lat, lon):
		x = int((lon - self.MINLON) / self.UNIT)
		y = int((lat - self.MINLAT) / self.UNIT)

		return x, y


	def addLink(self, link):
		self.lincolle[link.id] = link
		self.addLinkIdx(link)

	def addLinkIdx(self, link):
		lat, lon = link.MidPoint()
		x , y = self.calXY(lat, lon)
		# y = int((lat - self.MINLAT) / self.UNIT)
		self.index[(x, y)].append(link.id)

	def searchLinks(self, lat, lon):
		x, y = self.calXY(lat, lon)
		lids = self.index[(x, y)]
		return [self.lincolle[id] for id in lids]



