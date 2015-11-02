filename = input('file name: ')
print(filename)
tweetsData = open(filename)


string = '[41.923916200000001, -88.777469199999999] 6 2011-08-28 19:24:18 My life is worst love moviee.'

def extractTweet(line) :
	#put lat/lon and tweet text into variables, make tweet all lowercase for easy comparison
	string = line.lstrip('[')
	tupl = string.partition(']')
	latLon = tupl[0].split(', ')
	tweet = tupl[2].lower()
	#date and time make 22 characters, so take string starting after them to the end
	tweet = tweet[23:].rstrip()
	print(latLon)
	print(tweet)
	return tweet


keywords = ('excited', 'love', 'worst', 'fml')
values = (7, 10, 2, 3)

def searchTweet(tweet) :
	wordsFound = []
	happiness = 0
	for index, word in enumerate(keywords):
		if word in tweet:
			wordsFound.append(word)
			happiness += values[index]

	if wordsFound:
		print(wordsFound)
	if happiness:
		print(happiness)
	print('')

for line in tweetsData:
	tweet = extractTweet(line)
	searchTweet(tweet)
