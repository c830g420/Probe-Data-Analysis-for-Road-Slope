import math

class Node:
	def __init__(self, nid, latitude, longitude, elevation = None):
		self.id = nid
		self.lat = latitude
		self.lon = longitude
		self.elev = elevation
		pass

	@staticmethod
	def dist(lat1, lon1, lat2, lon2):
		# haversine
		return math.asin((math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lat2 - lat1) / 2) ** 2) ** 0.5)

	@staticmethod
	def degree(lat0, lon0, lat1, lon1):
		y = lat1 - lat0
		if not y:
			return 90.0
		x = math.cos(lat1 / 180 * math.pi) * (lon1 - lon0)
		return math.atan(x / y) / math.pi * 180

	@staticmethod
	def slope(lat0, lon0, elev0, lat1, lon1, elev1):
		return 180 / math.pi * math.atan(Node.dist(lat0, lon0, lat1, lon1) / (elev1 - elev0))
