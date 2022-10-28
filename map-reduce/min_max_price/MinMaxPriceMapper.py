#!/usr/bin/env python

import sys
def find_category(sqft) :
    if(sqft < 600):
        return 'SMALL-1'
    elif(601 < sqft < 800):
        return 'SMALL-2'
    elif(801 < sqft < 1200):
        return 'MEDIUM-1'
    elif(1201 < sqft < 1500):
        return 'MEDIUM-2'
    elif(1501 < sqft < 1800):
        return 'LARGE-1'
    else:
        return 'LARGE-2'

for line in sys.stdin:
    line = line.strip()
    keys = line.split('\t')

    builder = keys[12];
    project = keys[16];
    area = keys[20];
    price = keys[15];
    try:
      price = int(price)
      area = int(area)
    except ValueError:
      continue

    category = find_category(area);
    print( "%s\t%d" % (builder+"-"+project+"#"+category, int(price) ))


