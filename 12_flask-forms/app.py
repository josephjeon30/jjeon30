# TNPG: Steve, Roster: Samson, Joseph, Ryan

from flask import Flask, render_template, request;

app = Flask(__name__)

@app.route("/")
def display_login_page():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( "login.html" )

@app.route("/auth",methods=['POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    #print(request.args)
    print("***DIAG: request.form ***")
    print(request.form['username'])
    print("***DIAG: request.args['username']  ***") #Works only when its uncommented here
    #print(request.args['username']) #prints the inputted user
    username = request.form['username']
    print("***DIAG: request.headers ***")
    print(request.headers) #Accesses the args and puts them in a list
    return render_template( "response.html", user=username )  #response to a form submission

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
