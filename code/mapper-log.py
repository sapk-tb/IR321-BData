#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re
import pprint

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?) (.*?) (HTTP/.*?)" (\d+) (.+)'

for line in sys.stdin:
    data = re.search(regex, line)
    if data:
      print data.group(1), "\t", data.group(4)
#    else:
#      print line



#    pprint.pprint(data)
#    pprint.pprint(data.group(1))
#.groups()
#    if len(data) == 5:
#    if 1:
#        ip, time, method, url, version, response, size = data
#        print "{0}\t{1}".format(ip, url)

