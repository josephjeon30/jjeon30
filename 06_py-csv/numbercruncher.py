'''
Team J: Joshua Liu, Joseph Jeon
DISCO: 
    rsplit() splits the element from the right, and you can add another argument to determine how many times to split.
    random.choices() can be used to choose from a weighted list. The second argument sets the weights for each of the corresponding elements in the first list.
QCC:
    We still have to test if the weighted choices are chosen with the correct weights.
'''

import random


def main():
    jobs = []
    weight = []
    # parseinfo takes in a csv file and 2 lists. It parses the jobs in the csv file to the jobs list and the weights to the weight list, not including the total
    parseinfo("occupations.csv", jobs, weight)
    print(random.choices(jobs, weights = weight))
    
def parseinfo(file, jobs, weight):
    occ_wei = open(file, "r").read()
    
    # Creates a list of all occupation,weight pairs, excluding the first line, which isn't relevant.
    occ_wei = occ_wei.split("\n")[1:]
    
    for pair in occ_wei:
        # first see if pair is empty.
        if(len(pair) != 0):
            # rsplit() splits from  the left, and the second argument decides how many times to split.
            job_percent_pair = pair.rsplit(",", 1)
            # Dont include the Total,percent pair
            if(job_percent_pair[0] != "Total"):
                jobs.append(job_percent_pair[0])
                # Because we are using the choices method, the weights list has to only include integers, since
                weight.append(int(float(job_percent_pair[1]) * 10))
                

main()