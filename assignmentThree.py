#this program was written by Heather Booker, a student in CS1026A at UWO in Nov 2015
#the purpose of this program is to take user-inputted text files, extract the data to determine 'tweets' and 
#their originating time zones, and score tweets and time zones for happiness based on the presence of certain words
#this program also displays the results graphically
########################################################
#PROBLEMS################
# how to handle bad lon/lat?
# actual files have unicode decode error
# happy histogram file flaw
######################################################

def extractTweet(line) :
	if '[' not in line:
		return (0, 0)
	#put lat/lon and tweet text into variables, make tweet all lowercase for easy comparison
	string = line.lstrip('[')
	tupl = string.partition(']')
	latLon = tupl[0].split(', ')
	tweet = tupl[2].lower()
	#date and time make 22 characters, so take string starting after them to the end
	tweet = tweet[23:].rstrip()
	return (latLon, tweet)


def setUpKeywords(keywordsFile) :
	keywords = []
	values = []
	for line in keywordsFile:
		keysAndValues = line.split(',')
		keywords.append(keysAndValues[0])
		values.append(int(keysAndValues[1]))
	return (keywords, values)


def searchTweet(tweet, keysAndValues) :
	if not tweet:
		return False
	keywords = keysAndValues[0]
	values = keysAndValues[1]
	wordsFound = []
	happiness = 0
	for index, word in enumerate(keywords):
		if word in tweet:
			wordsFound.append(word)
			happiness += values[index]
	return(happiness)


def findTimeZone(latLon) :
	if not latLon:
		return False
	lat = float(latLon[0])
	lon = float(latLon[1])
	if lat > 49.189787 or lat < 24.660845 or lon < -125.242264 or lon > -67.444574:
		print('***location not within program constraints***')
		return False
	elif -87.518395 < lon <= -67.444574:
		return 'eastern'
	elif -101.998892 < lon <= -87.518395:
		return 'central'
	elif -115.236428 < lon <= -101.998892:
		return 'mountain'
	elif -125.242264 <= lon <= -115.236428:
		return 'pacific'

def increment(zone, happiness) :
	if not happiness:
		return False
	zone[1] += 1
	zone[2] += happiness
	return zone

def report(info) :
	print('for the {} time zone: {} tweets and a happiness score of {}'.format(info[0], info[1], info[2]))

def drawResults(est, cnt, mnt, pac) :
	#scaling happiness scores to fit between 0 and 10 to make histogram
	maxVal = max(est, cnt, mnt, pac)
	def calcNewValue(value) :
		result = value * 10 / maxVal
		return result
	east = calcNewValue(est)
	centr = calcNewValue(cnt)
	mntn = calcNewValue(mnt)
	pacf = calcNewValue(pac)
	from happy_histogram import drawSimpleHistogram
	drawSimpleHistogram(east, centr, mntn, pacf)


def main() :
	keys = setUpKeywords(keywordsData)
	eastern = ['eastern', 0, 0]
	central = ['central', 0, 0]
	mountain = ['mountain', 0, 0]
	pacific = ['pacific', 0, 0]
	for line in tweetsData:
		data = extractTweet(line)
		timeZone = findTimeZone(data[0])
		happiness = searchTweet(data[1], keys)
		if timeZone == 'eastern':
			increment(eastern, happiness)
		if timeZone == 'central':
			increment(central, happiness)
		if timeZone == 'mountain':
			increment(mountain, happiness)
		if timeZone == 'pacific':
			increment(pacific, happiness)
	report(eastern)
	report(central)
	report(mountain)
	report(pacific)
	tweetsData.close()
	keywordsData.close()
	drawResults(eastern[2],central[2],mountain[2],pacific[2])


try:
	tweetsFile = input('tweets file name: ')
	tweetsData = open(tweetsFile)
	keywordsFile = input('keywords file name: ')
	keywordsData = open(keywordsFile)
	main()
except IOError:
	print('file name incorrect and/or file invalid or nonexistent')