tweetsFile = input('tweets file name: ')
try:
	open(tweetsFile)
except:
	pass
# tweetsData = open('tweets.txt')
#filename2 = input('keywords file name: ')
keywordsData = open('keys.txt')


def extractTweet(line) :
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
	lat = float(latLon[0])
	lon = float(latLon[1])
	if lat > 49.189787 or lat < 24.660845 or lon < -125.242264 or lon > -67.444574:
		#raise ValueError('location not within program constraints')
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
	zone[1] += 1
	zone[2] += happiness
	return zone

def report(info) :
	print('for the {} time zone: {} tweets and a happiness score of {}'.format(info[0], info[1], info[2]))

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
	# print(eastern, central, mountain, pacific)
	report(eastern)
	report(central)
	report(mountain)
	report(pacific)

main()