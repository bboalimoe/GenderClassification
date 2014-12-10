__author__ = 'woodie'

import nbcLib.nbc as nbc

#
# Use this file to load cases and run.
#
# * Create a casefile in the 'cases' folder
# * Use a script from the 'scripts' folder
# * The finished network is saved in the 'networks' folder.
#

NBC = nbc.NBC("test.json")
NBC.train()