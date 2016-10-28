#!/usr/bin/python

import sys

nb = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisIP, thisURL = data_mapped

    if oldKey and oldKey != thisURL:
        print oldKey, "\t", nb
        oldKey = thisURL;
#        print "Changement de cle"
        nb = 0 #Reset

    oldKey = thisURL
    nb += 1

if oldKey != None:
    print oldKey, "\t", nb


