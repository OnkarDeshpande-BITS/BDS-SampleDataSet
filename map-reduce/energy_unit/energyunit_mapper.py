#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split('\t')

    builder = keys[12];
    project = keys[16];
    energy_save_units = keys[26];

    try:
      energy_save_units = int(energy_save_units)
    except ValueError:
        continue
    print( "%s\t%d" % (builder+"-"+project, energy_save_units ))


