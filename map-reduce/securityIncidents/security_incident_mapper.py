#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split('\t')

    locality = keys[5].strip();
    security_incidents = keys[22];
    if(len(locality) == 0):
        continue
    try:
      security_incidents = int(security_incidents)
    except ValueError:
        continue
    print( "%s\t%d" % (locality, security_incidents ))


