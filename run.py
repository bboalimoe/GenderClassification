__author__ = 'woodie'

import nbcLib.nbc as nbc

#
# Use this file to load cases and run.
#
#
#

# Instantiate the Object of NaiveBayesClassifier(NBC)
NBC = nbc.NBC("case.json")
# Train the NBC with the data in case.json
NBC.train()
# Predict result of new case.
case   = [0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1]
result = NBC.predictCase(case)
# Output the result
print "\nThe NBC's result"
print "================"
print "The probability of male is", result["male"]
print "The probability of female is", result["female"]