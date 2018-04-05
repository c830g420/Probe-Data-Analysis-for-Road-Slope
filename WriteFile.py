from Node import Node

class WriteFile:
	def __init__(self):
		self.DIRMP = 'Partition6467MatchedPoints.csv'
		self.DIRS = 'Partition6467Slopes.csv'
		# self.file = open(self.DIR, 'w', encoding = 'utf8')

	def writeMP(self, mtsq):
		# sampleID	is a unique identifier for the set of probe points that were collected from a particular phone.
		# dateTime	is the date and time that the probe point was collected.
		# sourceCode	is a unique identifier for the data supplier (13 = Nokia).
		# latitude	is the latitude in decimal degrees.
		# longitude	is the longitude in decimal degrees.
		# altitude	is the altitude in meters.
		# speed		is the speed in KPH.
		# heading		is the heading in degrees.
		# linkPVID	is the published versioned identifier for the link.
		# direction	is the direction the vehicle was travelling on thelink (F = from ref node, T = towards ref node).
		# distFromRef	is the distance from the reference node to the map-matched probe point location on the link in decimal meters.
		# distFromLink	is the perpendicular distance from the map-matched probe point location on the link to the probe point in decimal meters.
		file = open(self.DIRMP, 'w', encoding = 'utf8')
		for mq in mtsq:
			# sid = mq[0].sid
			# dt = mq[0].dttm
			# sc = mq[0].sourceCode
			# lat = mq[0].lat
			# lon = mq[0].lon
			# alt = mq[0].lat
			hd = mq[0].heading
			dg = Node.degree(mq[1][4], mq[1][5], mq[1][0], mq[1][1])
			if abs(hd - dg) > 90:
				direction = 'T'
			else:
				direction = 'F'
			dfr = Node.dist(mq[1][4], mq[1][5], mq[1][0], mq[1][1])
			file.write('%d,%s,%d,%f,%f,%f,%f,%f,%d,%s,%f,%f\n' % (mq[0].id, mq[0].dttm, mq[0].sourceCode, mq[0].lat, mq[0].lon, mq[0].alt, mq[0].speed, mq[0].heading, mq[1][3], direction, mq[1][2], dfr))
		file.close()


	def writeS(self, slp):
		file = open(self.DIRS, 'w', encoding = 'utf8')
		for s in slp:
			file.write('%f,%f,%f,%f\n' % s)
		file.close()

