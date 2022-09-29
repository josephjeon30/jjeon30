"""
Team Roster: Joseph Jeon, Joshua Liu

DISCO:
    The existence and function of python tuples
    Opening and reading files
    
QCC:

"""

import random as rng

def populate(fileName):
    file = open(fileName, "r").read()
    krewes = {2:[],7:[],8:[]}
    
    profiles = file.split("@@@")
    
    for i in profiles:
        j = i.split("$$$")
        krewes[int(j[0])].append((j[1],j[2]))
    
    return krewes

def randdevo(dnary):
    try:
        alldevos = list(dnary.keys())
        period = rng.choice(alldevos)
        devo_ducky = rng.choice(dnary[period])
        return devo_ducky[0] + ", a student from period " + str(period) + ", has a ducky named " + devo_ducky[1]
    except:
        print("Error, dict is length 0") 

print(randdevo(populate("krewes.txt")))