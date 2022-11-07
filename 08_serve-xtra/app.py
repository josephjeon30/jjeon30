"""
TNPG: sadidas; Roster: Joseph Jeon, Jeffery Tang, Jian Hong Li
SoftDev
K08
2022-10-06
Time Spent:
"""

from flask import Flask
import random

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?

def main():
    jobs = []
    weight = []
    # parseinfo takes in a csv file and 2 lists. It parses the jobs in the csv file to the jobs list and the weights to the weight list, not including the total
    parseinfo("occupations.csv", jobs, weight)
    ans = str(random.choices(jobs, weights = weight)[0])
    ans = ans.strip('\"')
    words = ans.split(' ')
    link = "https://www.google.com/search?channel=fs&q="
    for i in words:
        link += i + "+"
    link += "jobs"
    print(__name__) 
    return(
        """
        <style>
            body{
                font-size: 50px;
                background-color:rgb(200,200,200);
            }
            
            #main{
                margin-top:15%;
                width:80%;
                height:30%;
                text-align:center;
                background-color:rgba(0,0,0,0.5);
                border-radius: 400px;
                color:rgb(255,255,255);
                margin-right:auto;
                margin-left:auto;
                padding-top:50px;
            }
        </style>
        """+
        "<body>"+
        "<div id = \"main\">You Got:<br>"+ans+"<br><a href=\"" + link + "\">Learn more about the job</a><br><a href=\"http://127.0.0.1:5000\">RELOAD</a>" + "</div>"
        
        )
        
    
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
                


app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. I have not seen similar syntax anywhere, unless the underscores are just normal characters 
1. Maybe the slash is the separator between the directories when you find the path to the file?
2. To the terminal
3. The name of this program?
4. No, because it's only the returntype and it's not being printed anywhere
5. Processing's run method? 
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''