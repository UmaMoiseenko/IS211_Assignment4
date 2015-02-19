from __future__ import division
import operator
import argparse
import csv
import re
import urllib2
import datetime

# test URL:
# http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv

def main():
    def downloadData(url):
        content = urllib2.urlopen(url)
        return content

    def processData(content):
        dictionary = csv.reader(content)

        dateFormat = '%Y-%m-%d %H:%M:%S'
        hits = imgHits = 0 
        safari = chrome = firefox = msie = 0
		
		# create arr for 24 hours
        times = {} 
        for i in range(0, 24):
        	times[i] = 0


        for row in dictionary:
            result = {'path':row[0], 'date':row[1], 'browser': row[2], 'status': row[3], 'size': row[4]}
            browser = result['browser']
            
            date = datetime.datetime.strptime(result['date'], dateFormat)
            counter = times[date.hour] + 1
            times[date.hour] = counter

            hits += 1
            if re.search(r"\.(?:jpg|jpeg|gif|png)$", result['path'], re.I | re.M): 
                imgHits += 1

            
            if re.search('chrome', result['browser'], re.I ): 
                chrome += 1

            if re.search('safari', result['browser'], re.I) and not re.search("chrome/\d+", result['browser'], re.I): 
                safari += 1

            if re.search('firefox', result['browser'], re.I): 
                firefox += 1

            if re.search("msie", result['browser'], re.I): 
                msie += 1

        tempTimes = times
        sortedTimes = {}

        # pop max keys and print 0 key vals in order
        for i in range(0, 24):
	        id = (max(tempTimes.iteritems(), key=operator.itemgetter(1))[0])
	        if id == 0:
	        	print "Hour %02d has %s hits" % (id, tempTimes[id])
	        else:
	       	 	print "Hour %02d has %s hits" % (id, tempTimes[id])
	        tempTimes.pop(id)

        imageRequest = (imgHits/hits)*100
        browsers = {'Safari': safari, 'Chrome':chrome, 'Firefox': firefox, 'MSIE':msie}
        print browsers
        print "Image requests account for {0:0.1f} of all requests".format(imageRequest)
        print "The most popular browser today is %s" % (max(browsers.iteritems(), key=operator.itemgetter(1))[0])

        
    url_parser = argparse.ArgumentParser()
    url_parser.add_argument("--url", help='enter URL to CSV file', type=str)
    args = url_parser.parse_args()


    if args.url:
        try:
            csvData = downloadData(args.url)
            getHits = processData(csvData)       

        except:
            print "Invalid URL"
    else:
        print "insert url for csv file after --url or type --help to see more details. Bye"

if __name__ == "__main__":
    main()
