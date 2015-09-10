#!/usr/bin/env python

import sys
import random

random.seed()

pick = [ "Favorite", "Underdog" ]

teamnames = [ "Arizona",
		"Atlanta",
		"Baltimore",
		"Buffalo",
		"Carolina",
		"Chicago",
		"Cincinnati",
		"Cleveland",
		"Dallas",
		"Devner",
		"Detroit",
		"Green Bay",
		"Houston",
		"Indianapolis",
		"Jacksonville",
		"Kansas City",
		"Miami",
		"Minnesota",
		"New England",
		"New Orleans",
		"New York (NYG)",
		"New York (NYJ)",
		"Oakland",
		"Philadelphia",
		"Pittsburgh",
		"San Diego",
		"San Francisco",
		"Seattle",
		"St. Louis",
		"Tampa Bay",
		"Tennessee",
		"Washington" ]
		

# Game Picks
print "Game Picks"
print "----------"
for x in range(0, int(sys.argv[1])):
	print "Game #%s: %s" % (x+1, pick[random.randint(0,1)])

# Tiebreaker #1
print
print "Tiebreaker #1"
print "-------------"
print "Game #1: %d @ %d" % (random.randint(0,50), random.randint(0,50))
print "Game #2: %d @ %d" % (random.randint(0,50), random.randint(0,50))
print "-------------"

# Tiebreaker #2
most = random.choice(teamnames)
fewest = most

while (fewest == most):
	fewest = random.choice(teamnames)

print
print "Tiebreaker #2"
print "-------------"
print "MOST points: %s" % most
print "FEWEST points: %s" % fewest
print "-------------"
