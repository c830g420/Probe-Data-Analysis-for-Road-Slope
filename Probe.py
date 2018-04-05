from datetime import datetime


class Probe:
	def __init__(self, sid , dtime, scode, latitude, longitude, altitude, spd, hding):
		self.id = sid
		self.sourceCode = scode
		self.dttm = dtime
		self.lat = latitude
		self.lon = longitude
		self.alt = altitude
		self.speed = spd
		self.heading = hding