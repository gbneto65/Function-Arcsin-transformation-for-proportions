# Guilherme Borchardt - April 21
# statistics functions - arc sin transformation for percentages

"""
Cohen's Effect Size "h": The Arcsin / Arcsine Transformation of Probabilities
Cohen, Jacob (2008). Statistical power analysis for the behavioral sciences. Second Edition. Hillsdale, New Jersey: Lawrence Erlbaum Associates, Inc.. Google Books. Amazon.
https://people.ucalgary.ca/~ramsay/cohen-effect-size-h-arcsin-transformation.htm

Not multiplying by two makes the scale stop at pi/2. The choice is arbitrary.


Recommendations -  http://strata.uga.edu/8370/rtips/proportions.html
 
For regression, the logit transformation is preferred for three reasons (Warton and Hui 2011).
 First, the logit scale covers all of the real numbers instead of being limited to a particular
 range. For example, just as proportion is limited to 0–1, the arcsine square root scale is limited
 to 0 to pi. In constrast, the limits of the logit scale are negative infinity and positive infinity.
 This is particularly important where prediction is needed, as having a bounded scale could give
 nonsensical results (e.g., more than 100% or less than 0%). Second, the logit scale is more intuitive
 in that it is the log-odds. This is particularly useful in interpreting slopes from a logistic regression,
 in which the logit transformation is central. Third, the logit scale correctly models the relationship
 between the mean and variance in binomial data, where variance is p(1-p)/n.

In multivariate studies, like ordination or cluster analysis, the arcsine transformation is preferred.
 For ecological data, proportions of 0% are common, such as when a species doesn’t occur in a sample.
 Values of 100% are also possible, such as when only a single species is present in a sample.
 In these cases, the range of the logit scale becomes a problem because values of negative infinity
 will occur whenever a species is absent from a sample and values of positive infinity will be arise in
 any monospecific sample. Although one could add a small value to prevent a zero proportion or subtract a
 small value to prevent a proportion of one, such values are arbitrary and the effect of the chosen value
 would have to be evaluated. An arcsine square root transformation would be more straightforward for these
 types of problems. Finally, because both transformations are essentially linear over the range of 0.3–0.7,
 neither transformation is necessary if all of your data falls in this range.


others ref:
 http://statisticalconcepts.blogspot.com/2010/02/transformation-of-data-validity-of.html

"""

import numpy as np
import sys



def arcsin_transf(np_list):
    
    #verifiy possible error on the dataset
    min = np.min(np_list)
    max = np.max(np_list)
        
    if min <0 or max >1:
         print ('\n@@@ ERROR - some values are below 0 or above 1 - verifiy your data @@@\n')
         sys.exit() # abort execution

    # if no error (above 1 or below 0)  - proceed to transformation of data - numpy array
    else:
        np_transf_list = 2 * np.arcsin(np.sqrt(np_list))

    return np_transf_list # array to be used on parametric stats






# Example of use

percentage_data = np.array([0., 1, .5, .8, .8, .9])
print(percentage_data) # the data
print(arcsin_transf(percentage_data)) # transformed data


