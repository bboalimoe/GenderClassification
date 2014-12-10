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
        self.tCase      = case.Case(train_file)
        self.tCase.printCaseInfo()
        # The list of hypothesis
        # It's a list.
        self.hypothesis = self.tCase.hypothesis
        # The prior probability of every hypothesis
        # It is a list.
        self.prior_p    = []
        # Every item's likelihood at certain hypothesis. It's a 3-dimensional list variable
        # - 1. The size of likelihood is case's item count
        # - 2. Every element of likelihood is [H0, H1, ... Hi ... Hn]
        #   Hi contains the item's every possible result's possibility in Hi (that is likelihood's definition)
        # - 3. Hi's structure is [li0, li1, ... lij ... lim]
        #   lij is the likelihood of items in Hi which result is j
        self.likelihood = []

    # The prediction of new case
    # It's a normalization method
    def predictCase(self, D):
        #start classifying ...
        print "\nThe classifying started"
        print "======================="
        # Init tmp variable
        result = {}
        P = 0
        # Calculate the Denominator
        for h in self.hypothesis:
            P += self.posteriorP(h, D)
            print "- the posterior true probability of", h, "is", self.posteriorP(h, D)
        # Calculate the Molecular
        try:
            for h in self.hypothesis:
                p = self.posteriorP(h, D) / P
                result[h] = p
            return result
        except:
            print "The result is not accuracy enough.Please add more tranning cases."
            for h in self.hypothesis:
                result[h] = "unknown"
            return result

    # It will train the NBC by calculating various of probability with cases' data
    # First, it calcutates the prior probability of every hypothesis.
    def train(self):
        # All hypothesis
        hypothesisCount = self.tCase.hypoCount
        itemCount       = self.tCase.itemCount
        itemValue       = self.tCase.itemValue
        # Init likelihood
        for i in range(0, itemCount):
            hi = []
            for h in range(0, hypothesisCount):
                vi = []
                for v in range(0, len(itemValue[i])):
                    l  = 0
                    vi.append(l)
                hi.append(vi)
            self.likelihood.append(hi)
        #start trainning ...
        print "\nThe trainning started"
        print "====================="
        print "\n1. Calculate the prior probability of every hypothesis"
        print "------------------------------------------------------"
        # Calculate the prior probability of every hypothesis
        for hypo in self.hypothesis:
            p = self.priorP(hypo)
            print "The", hypo, "in cases weighs", p, "%"
            self.prior_p.append(p)
        print "\n2. Calculate every item's likelihood at certain hypothesis"
        print "----------------------------------------------------------"
        # Calculate every item's likelihood at certain hypothesis
        for i in range(0, itemCount):
            print i, ".",
            for h in range(0,hypothesisCount):
                for v in range(0, len(itemValue[i])):
                    # likelihood[i][h][v] = P(i=v|h)
                    self.likelihood[i][h][v] = self.likelihoodP(i, h, v)
                    print self.likelihood[i][h][v],
                    if v < len(itemValue[i])-1:
                        print "|",
                print " , ",
            print "\n"

    # The posterior probability of hypothesis - P(h|D)( * P(D) )
    # - h is hypothesis' name
    # - D is the new case which is waitting for classifying (D = [])
    def posteriorP(self, h, D):
        P = 0
        if len(D) == self.tCase.itemCount:
            # The hypothesis' index num in self.hypothesis
            index_h = 0
            for tmp_h in self.hypothesis:
                if h == tmp_h:
                    break;
                else:
                    index_h += 1
            # Calculate the prior probability
            P = self.prior_p[index_h]
            for i in range(0, len(D)):
                # Calculate the posterior probability
                P = P * self.likelihood[i][index_h][D[i]]
                #print self.hypothesis[index_h]
        else:
            print "The count of case's item is error.Please check your classifying case."
        return P

    # The prior probability of hypothesis - P(h)
    def priorP(self, h):
        h_count     = self.tCase.getHypothesisCount(h)
        total_count = self.tCase.caseCount
        P = decimal.Decimal(h_count) / decimal.Decimal(total_count)
        return P

    # The likelihood of D at a certain hypothesis - P(D|h)
    # - P(itemIndex = value | h)
    # - itemIndex, h, value are index number
    def likelihoodP(self, itemIndex, h, value):
        # The cases in hypothesis 'h'
        caseInHypo           = self.tCase.getCaseInHypo(self.hypothesis[h])
        # The count of cases in hypothesis 'h'
        countCaseInHypo      = len(caseInHypo)
        # The count of cases in hypothesis 'h' which item 'itemIndex' is 'value'
        countCaseItemIsValue = 0
        for case in caseInHypo:
            if case[itemIndex] == value:
                countCaseItemIsValue += 1
        # The likelihood
        P = decimal.Decimal(countCaseItemIsValue) / decimal.Decimal(countCaseInHypo)
        return decimal.Decimal("%.3f" % float(P))




