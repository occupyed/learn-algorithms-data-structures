"""
Formula to calculate compound interest annually is given by:

Compound Interest = P(1 + R/100)^r
Where,
P is principle amount
R is the rate and
T is the time span
"""

"""
Input : Principle (amount): 1200
        Time: 2
        Rate: 5.4
Output : Compound Interest = 1333.099243
"""


# Python3 program to find compound
# interest for given values.

def compound_interest(principle, rate, time):
    # Calculates compound interest
    CI = principle * (pow((1 + rate / 100), time))
    print("Compound interest is", CI)


# Driver Code
compound_interest(10000, 10.25, 5)