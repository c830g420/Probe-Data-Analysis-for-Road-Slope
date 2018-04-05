import sys
from collections import defaultdict

from ReadFile import ReadFile
from Match import Match
from WriteFile import WriteFile
from Slope import Slope

def main():
	print('Start reading links ...')
	readlink = ReadFile('Partition6467LinkData.csv')
	mp = readlink.readLinks()
	print('Links reading complete ...')
	# print('Unit ready ...')
	print('Start reading probe points ...')
	readprobe = ReadFile('Partition6467ProbePoints.csv')
	if (len(sys.argv) > 1):
		print('Start reading %d probes ...' % int(sys.argv[1]))

		prbs = readprobe.readProbes(int(sys.argv[1]))
	else:
		print('Start reading %d probes ...' % 5000)

		prbs = readprobe.readProbes()

	sampleIds = prbs.keys()
	# print(prbs.items())
	mtsq = list()
	print('Probes reading complete ...')
	for sid in sampleIds:
		print('Analyzing probes from sample No.%d ...' % sid)
		 # __init__(self, plist, mp):
		mc = Match(prbs[sid], mp)
		print('\tStart calculating candidate points ...')
		pcps = mc.probeCandidates()
		print('\tCandidate points calculating complete ...')
		print('\tStart matching sequence ...')
		mtsq.extend(mc.findMatchedSequence(pcps))
		print('\tSequence matching complete ...')

	print('Start writing matched sequence ...')
	wf = WriteFile()
	
	wf.writeMP(mtsq)
	print('Sequence writing complete ... ')
	print('Start calculating slopes ...')
	slope = Slope(mtsq, mp)
	slp = slope.calSlope()
	print('Slopes calculating complete ...')
	print('Start writing slopes ...')
	wf.writeS(slp)
	print('Slopes writing complete ...')








if __name__ == '__main__':
	main()