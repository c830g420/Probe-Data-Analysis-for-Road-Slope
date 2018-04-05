from Node import Node
import math

class Link:
	def __init__(self, lid, rnode, nrnode, leng):
		self.id = lid
		self.refNode = rnode
		self.nrefNode = nrnode
		self.length = leng
		self.shapeInfo = list()
		self.shapeInfo.append((rnode.lat, rnode.lon, rnode.elev))
		self.shapeInfo.append((nrnode.lat, nrnode.lon, nrnode.elev))
		self.curvatureInfo = None
		self.slopeInfo = None

	def setShape(self, lat, lon, elev = None):
		self.shapeInfo.insert(-1, (lat, lon, elev))

	def setCurvature(self, dist, curvature):
		if not self.curvatureInfo:
			self.curvatureInfo = list()
		self.curvatureInfo.append((dist, curvature))

	def setSlope(self, dist, slope):
		if not self.slopeInfo:
			self.slopeInfo = list()
		self.slopeInfo.append((dist, slope))

	def getElev(self, lat, lon):
		for i in range(len(self.shapeInfo)):
			si = self.shapeInfo[i]
			if lat == si[0] and lon == si[1]:
				return si[2], i
		return 0, -1



	def calSegProjection(self, lat, lon, lat0, lon0, lat1, lon1):
		y0 = lat0
		x0 = lon0
		y1 = lat1 - y0
		x1 = math.cos(lat1/ 180 * math.pi) * (lon1 - x0)
		y2 = lat - y0
		x2 = math.cos(lat / 180 * math.pi) * (lon - x0)
		x = (x1 * x2 + y1 * y2) / (x1 + y1)
		if x1:
			y = y1 * x / x1
		else:
			y = y1 * x / 0.0001
		lonx = x / math.cos(y / 180 * math.pi)
		if x < 0:
			d = Node.dist(lat, lon, lat0, lon0)
		elif x > x1:
			d = Node.dist(lat, lon, lat1, lon1) #((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
		else:
			d = Node.dist(y, lonx, lat, lon) #((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5 
		return y + lat0, lonx + lon0, d, self.id, lat0, lon0

	def calProjDist(self, lat, lon):
		tem = list()
		for i in range(len(self.shapeInfo) - 1):
			p = self.calSegProjection(lat, lon, self.shapeInfo[i][0], self.shapeInfo[i][1], self.shapeInfo[i + 1][0], self.shapeInfo[i + 1][1])
			tem.append(p)
		return sorted(tem, key = lambda s:s[2])

	def MidPoint(self):
		return (self.shapeInfo[0][0] + self.shapeInfo[-1][0]) / 2 , (self.shapeInfo[0][1] + self.shapeInfo[-1][1]) / 2


		
