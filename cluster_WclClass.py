#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Gong

from math import sqrt
from collections import defaultdict
def sim_distance(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0: return 0
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2) for item in si ] )
    return 1/(1 + sqrt(sum_of_squares))

def sim_person(prefs , person1 , person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    n = len(si)
    if n == 0: return 1
    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])
    sum1sq = sum([pow(prefs[person1][item], 2) for item in si])
    sum2sq = sum([pow(prefs[person2][item], 2) for item in si])
    pSum = sum([prefs[person1][item] * prefs[person2][item] for item in si])
    num = pSum-(sum1*sum2/n)
    den = sqrt((sum1sq - pow(sum1, 2)/n) * (sum2sq - pow(sum2, 2)/n))
    if den == 0:return 0
    r = num/den
    return r

def topMatches(prefs , person , n = 5 , similarity = sim_person):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, person, similarity = sim_person):
    totals = defaultdict{float}
    simSums  = defaultdict{float}
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)
        if sim <= 0: continue
        for item in prefs[other]:
            if not item in prefs[person] or prefs[person][item] == 0:
                totals[item] += sim * prefs[other][item]
                simSums[item] += sim
        ranking = [(total/simSums[item], item) for item, total in totals.items()]
        ranking.sort()
        ranking.reverse()
        return ranking
    







