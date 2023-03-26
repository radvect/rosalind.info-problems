#the soultion of the problem is based on the binomial distribution
#https://en.wikipedia.org/wiki/Binomial_distribution


import math

generation,atLeast=map(int,input().split())

numberofSpecies = 2**generation

prob_success = 1/4
prob_fail = 3/4

probability = 0
for i in range(atLeast, numberofSpecies+1):
    probability += (math.factorial(numberofSpecies))/(math.factorial(numberofSpecies-i))/(math.factorial(i))*(prob_success**i)*(prob_fail**(numberofSpecies-i))
print(probability)
