# TNPG: Steve, Roster: Samson, Joseph, Ryan


from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'_MinecraftSTEVE'

validuser = 'admin'
validpass = 'admin'


@app.route('/')
def index():
    login_status = False
    if 'username' in session:
        login_status = True
        return render_template("response.html", loginstatus=login_status, user=session['username'])
    return redirect(url_for('login')) #'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] == validuser and request.form['password'] == validpass:
        # print(request.form['username'])
        # print(request.form['password'])
        session['username'] = request.form['username']
        print("Cookie stuff: " + str(session))
        return redirect(url_for('index'))
    if request.method == 'POST' and not request.form['username'] == validuser and not request.form['password'] == validpass:
        return render_template('login.html', failmsg='Wrong username and password!')
    return render_template("login.html", failmsg='')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    login_status = False
    return redirect(url_for('index'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()


# def display_login_page():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
#     print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
#     print(request.args)
#     print("***DIAG: request.headers ***")
#     print(request.headers)
#     return render_template( "login.html" )

# @app.route("/auth", methods=['POST'])
# def authenticate():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
#     print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
#     #print(request.args)
#     print("***DIAG: request.form ***")
#     print(request.form)
#     print("***DIAG: request.args['username']  ***") #Works only when its uncommented here
#     #print(request.args['username']) #prints the inputted user
#     username = request.form['username']
#     print("***DIAG: request.headers ***")
#     print(request.headers) #Accesses the args and puts them in a list
#     return render_template( "response.html", user=username )  #response to a form submission