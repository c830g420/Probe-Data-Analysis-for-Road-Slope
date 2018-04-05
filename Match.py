from scipy.stats import norm
from collections import defaultdict

from GerMap import GerMap
from Link import Link
from Node import Node

class Match:
	def __init__(self, plist, mp):
		self.prbls = plist
		self.map = mp

	def probeCandidates(self):
		tre = list()
		for pb in self.prbls:
			lks = self.map.searchLinks(pb.lat, pb.lon)
			cps = list()
			for lk in lks:
				# Link. calProjDist(self, lat, lon):
				cpst1 = lk.calProjDist(pb.lat, pb.lon)
				cps.extend(cpst1)
			tre.append(cps)

		return tre

	def Vc0c1(self, p0, p1, cp0, cp1):
		nmn = Node.dist(p0.lat, p0.lon, p1.lat, p1.lon)
		dnm = Node.dist(cp0[0], cp0[1], cp1[0], cp1[1])
		if dnm:
			return nmn / dnm
		else:
			return nmn / 0.01



	def findMatchedSequence(self, pcps):
		f = defaultdict(float)
		pre = dict()
		for cp in pcps[0]:
			f[cp] = norm.pdf(cp[2], 0, 20)
		for i in range(1, len(pcps)):
			for ccp in pcps[i]:
				print('\t%f,%f,%f,%d,%f,%f' % ccp)
				mx = 0
				for prp in pcps[i - 1]:
					alt = f[prp] + norm.pdf(ccp[2], 0, 20) * self.Vc0c1(self.prbls[i - 1], self.prbls[i], list(prp), list(ccp))
					if alt > mx:
						mx = alt
						pre[ccp] = prp
					f[ccp] = mx

		ptat1 = sorted([(lp, f[lp]) for lp in pcps[-1]], key = lambda x:-x[1])
		if not len(ptat1):
			return list()
		pta = ptat1[0][0]
		re = list()
		for i in range(len(pcps) - 1, 0, -1):

			re.insert(0, pta)

			if pta in pre.keys():
				pta = pre[pta]
			else:
				return zip(self.prbls[-len(re):], re)

		re.insert(0, pta)

		return zip(self.prbls, re)










