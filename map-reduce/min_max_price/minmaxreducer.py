#!/usr/bin/env python

import sys

last_key = None
min_value = sys.maxsize
max_value = 0

for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key, value = input_line.split("\t", 1)
   try:
      value = int(value.strip())
   except ValueError:
      continue

   if last_key == this_key:
       min_value = min(min_value,value)
       max_value = max(max_value,value)
   else:
       if last_key:
           print( "%s\t%d,%d" % (last_key, min_value, max_value) )
       min_value = value
       max_value = value
       last_key = this_key

if last_key == this_key:
   print( "%s\t%d,%d" % (last_key, min_value, max_value) )
