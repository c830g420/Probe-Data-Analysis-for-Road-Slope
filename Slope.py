
from Node import Node


class Slope:
	def __init__(self, pbcd, mp):
		self.probcan = pbcd
		self.map = mp

	def calSlope(self):
		re = list()
		for i in range(len(self.probcan)):
			pd = self.probcan[i]
			# y, lonx, d, self.id, lat0, lon0
			lid = pd[1][3]
			lk = self.map.lincolle[lid]
			rlat = pd[1][4]
			rlon = pd[1][5]
			if lk.slopeInfo:
				# rlat = pd[1][4]
				# rlon = pd[1][5]
				# def slope(lat0, lon0, elev0, lat1, lon1, elev1):
				relev , j = lk.getElev(rlat, rlon)
				slc = Node.slope(rlat, rlon, relev, pd[0].lat, pd[0].lon, pd[0].alt)
				sl = lk.slopeInfo[j][1]
				re.append((rlat, rlon, sl, slc))
			else:
				re.append((rlat, rlon, 0.0, 0.0))

		return re

	def evalSlope(self, slslc):
		return [sl - slc for sl, slc in slslc]





