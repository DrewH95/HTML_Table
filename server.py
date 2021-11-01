from flask import Flask, render_template
app = Flask (__name__)

@app.route ('/') 
def index():
    user = [
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name' : 'Michael Choi', 'nickname' : 'Coding Master'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name' : 'John Supsupin', 'nickname' : 'Chief'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name' : 'Mark Guillen', 'nickname' : 'MG'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name' : 'KB Tonel', 'nickname' : 'KBT'}
    ]
    return render_template ("index.html", user = user)



if __name__== "__main__":
    app.run (debug=True) 