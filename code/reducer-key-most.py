#!/usr/bin/python

import sys

nb = 0
oldKey = None
bestKey = None
bestKeyNb = 0
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

    thisKey, thisData = data_mapped

    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", nb
        oldKey = thisKey;
        nb = 0 #Reset

    oldKey = thisKey
    nb += 1
    if nb > bestKeyNb:
      bestKeyNb = nb
      bestKey = thisKey

if bestKey != None:
    print bestKey, "\t", bestKeyNb


