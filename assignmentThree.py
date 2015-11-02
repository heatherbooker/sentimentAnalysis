#filename = input('tweets file name: ')
tweetsData = open('tweets.txt')
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
	# print(latLon)
	print(tweet)
	return (latLon, tweet)


def setUpKeywords(keywordsFile) :
	keywords = []
	values = []
	for line in keywordsFile:
		keysAndValues = line.split(',')
		keywords.append(keysAndValues[0])
		values.append(int(keysAndValues[1]))
	print(keywords)
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
	if wordsFound:
		print(wordsFound)
	if happiness:
		# print(happiness)
		pass
	print('')

def findTimeZone(latLon) :
	#do i even need these?
	# pacific = (-125.242264, -115.236428)
	# mountain = (-115.236428, -101.998892)
	# central = (-101.998892, -87.518395)
	# eastern = (-87.518395, -67.444574)
	lat = float(latLon[0])
	lon = float(latLon[1])
	if lat > 49.189787 or lat < 24.660845 or lon < -125.242264 or lon > -67.444574:
		#raise ValueError('location not within program constraints')
		print('***location not within program constraints***')
		return False
	elif -87.518395 < lon <= -67.444574:
		# print('EASTERN TIME ZONE')
		return 'eastern'
	elif -101.998892 < lon <= -87.518395:
		# print('CENTRAL TIME ZONE')
		return 'central'
	elif -115.236428 < lon <= -101.998892:
		# print('MOUNTAIN TIME ZONE')
		return 'mountain'
	elif -125.242264 <= lon <= -115.236428:
		# print('PACIFIC TIME ZONE')
		return 'pacific'

def main() :
	keys = setUpKeywords(keywordsData)
	for line in tweetsData:
		data = extractTweet(line)
		timeZone = findTimeZone(data[0])
		searchTweet(data[1], keys)

main()
# p1 = (49.189787, -67.444574)
# p2 = (24.660845, -67.444574)
# p3 = (49.189787, -87.518395)
# p4 = (24.660845, -87.518395)
# p5 = (49.189787, -101.998892)
# p6 = (24.660845, -101.998892)
# p7 = (49.189787, -115.236428)
# p8 = (24.660845, -115.236428)
# p9 = (49.189787, -125.242264)
# p10 = (24.660845, -125.242264)