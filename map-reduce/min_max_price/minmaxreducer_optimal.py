#!/usr/bin/env python

import sys

last_key = None
min_out = sys.maxsize
max_out = 0

for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key, value = input_line.split("\t", 1)
   min_value , max_value = value.split(",",1)
   min_value = int(min_value)
   max_value = int(max_value)

   if last_key == this_key:
       min_out = min(min_out,min_value)
       max_out = max(max_out,max_value)
   else:
       if last_key:
           print( "%s\t%d,%d" % (last_key, min_out, max_out) )
       min_out = min_value
       max_out = max_value
       last_key = this_key

if last_key == this_key:
   print( "%s\t%d,%d" % (last_key, min_out, max_out) )
