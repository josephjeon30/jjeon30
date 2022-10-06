# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

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