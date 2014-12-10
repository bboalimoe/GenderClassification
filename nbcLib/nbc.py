__author__ = 'woodie'

import case
import decimal

# @class:       Naive Bayes Classifier
# @author:      Woodie
# @createAt:    Wed 10 Dec, 2014
# @description:
#   Bayes Formula:
#       - P(male|D) = P(male) * P(D|male) / P(D)
#       - P(female|D) = P(female) * P(D|female) / P(D)
#   The True Probability:
#       - P'(male|D) = P(male|D) / ( P(male|D) + P(female|D) )
#       - P'(female|D) = P(female|D) / ( P(male|D) + P(female|D) )

class NBC:
    case = 0
    def __init__(self, train_file):
        # Get trainning cases from json file.
        self.tCase = case.Case(train_file)
        self.tCase.printCaseInfo()

    # The prediction of new case
    def predictCase(self):
        result = 0

        return result

    # It will train the NBC by calculating various of probability with cases' data
    # First, it calcutates the prior probability of every hypothesis.
    def train(self):
        # All hypothesis
        hypothesis      = self.tCase.hypothesis
        hypothesisCount = self.tCase.hypoCount
        itemCount       = self.tCase.itemCount
        # The prior probability of every hypothesis
        prior_p    = []
        # Every item's likelihood at certain hypothesis. It's a 3-dimensional variable
        # - 1. The size of likelihood is case's item count
        # - 2. Every element of likelihood is [H0, H1, ... Hi ... Hn]
        #   Hi contains the item's every possible result's possibility in Hi (that is likelihood's definition)
        # - 3. Hi's structure is [li0, li1, ... lij ... lim]
        #   lij is the likelihood of items in Hi which result is j
        likelihood = []
        # Init likelihood
        for i in range(0, itemCount):
            hi = []
            for h in range(0, hypothesisCount):
                vi = []
                for v in range(0, len(self.tCase.itemValue[i])):
                    l  = 0
                    vi.append(l)
                hi.append(vi)
            likelihood.append(hi)
        #start trainning ...
        print "\nThe trainning started"
        print "====================="
        print "\n1. Calculate the prior probability of every hypothesis"
        print "------------------------------------------------------"
        # Calculate the prior probability of every hypothesis
        for hypo in hypothesis:
            p = self.priorP(hypo)
            print "The", hypo, "in cases weighs", p, "%"
            prior_p.append(hypo)
        print "\n2. Calculate every item's likelihood at certain hypothesis"
        print "----------------------------------------------------------"
        # Calculate every item's likelihood at certain hypothesis
        for i in range(0, itemCount):
            print i, ".",
            for h in range(0,hypothesisCount):
                for v in range(0, len(self.tCase.itemValue[i])):
                    likelihood[i][h][v] = self.likelihoodP(i, h, v)
                    print likelihood[i][h][v],
                    if v < len(self.tCase.itemValue[i])-1:
                        print "|",
                print " , ",
            print "\n"

    # The posterior probability of hypothesis - P(h|D)( * P(D) )
    def posteriorP(self, h, D):
        P = 0
        return P

    # The prior probability of hypothesis - P(h)
    def priorP(self, h):
        h_count     = self.tCase.getHypothesisCount(h)
        total_count = self.tCase.caseCount
        P = decimal.Decimal(h_count) / decimal.Decimal(total_count)
        return P

    # The likelihood of D at a certain hypothesis - P(D|h)
    # - P(itemIndex = value | h) (itemIndex, h, value are index number)
    def likelihoodP(self, itemIndex, h, value):
        P = 0

        return P




