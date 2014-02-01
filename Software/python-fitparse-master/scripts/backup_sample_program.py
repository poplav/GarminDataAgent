#!/usr/bin/env python

import os
import sys

# Add folder to search path

PROJECT_PATH = os.path.realpath(os.path.join(sys.path[0], '..'))
sys.path.append(PROJECT_PATH)

from fitparse import Activity

quiet = 'quiet' in sys.argv or '-q' in sys.argv
filenames = None

startTime = None
totalDistance = None
avgSpeed = None
totalElapsedTime = None

if len(sys.argv) >= 2:
    filenames = [f for f in sys.argv[1:] if os.path.exists(f)]
    index = sys.argv[1].rfind('/')
    fOut = sys.argv[1][index+1:]
    fOut = fOut.replace(".fit", ".txt")
    f1=open('./garmin_data.csv', 'a')

if not filenames:
    filenames = [os.path.join(PROJECT_PATH, 'tests', 'data', 'sample-activity.fit')]


def print_record(rec, ):
    global record_number
    record_number += 1
    print ("-- %d. #%d: %s (%d entries) " % (record_number, rec.num, rec.type.name, len(rec.fields))).ljust(60, '-')
    #f1.write(("-- %d. #%d: %s (%d entries) \n" % (record_number, rec.num, rec.type.name, len(rec.fields))).ljust(60, '-'))
    for field in rec.fields:
	if "start_time" in field.name:
	    global startTime
            startTime = field.data
	    print "start time******************************\n"
	    print field.data
	    print
        if "total_distance" in field.name:
	    global totalDistance
            totalDistance = field.data
	    print "total distance [m]***********************************\n"
            print field.data
	    print
	if "avg_speed" in field.name:
	    global avgSpeed
            avgSpeed = field.data
	    print "avg speed [m/s]******************************\n"
	    print field.data
	    print
	if "total_elapsed_time" in field.name:
	    global totalElapsedTime
            totalElapsedTime = field.data
	    print "total elapsed time [s]******************************\n"
	    print field.data
	    print

        to_print = "%s [%s]: %s" % (field.name, field.type.name, field.data)
        if field.data is not None and field.units:
            to_print += " [%s]" % field.units
        print to_print
    print startTime
    print totalDistance
    print avgSpeed
    print totalElapsedTime
        #f1.write(to_print)
        #f1.write("\n")
    print
    #f1.write("\n")

for f in filenames:
    if quiet:
        print f
    else:
        print ('##### %s ' % f).ljust(60, '#')

    print_hook_func = None
    if not quiet:
        print_hook_func = print_record

    record_number = 0
    a = Activity(f)
    a.parse(hook_func=print_hook_func)
    if startTime is not None:
        f1.write("%s,%s,%s,%s\n" % (startTime,totalDistance,avgSpeed,totalElapsedTime))
