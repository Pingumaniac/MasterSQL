"""
Note that many of the codes have been reused from my CSE 416 Software Engineering final project.

Here is the link for the reference code:
https://github.com/Pingumaniac/TheALLDictionaries/blob/main/app.py
"""

from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from python.masterSQLAPI import DB
import pymysql
import time
import datetime
import re
import json
from error_pages import error_pages
from my_pages import my_pages
from sql_pages import sql_pages

# Codes for initialising the flask application
app = Flask(__name__)
app.register_blueprint(error_pages)
app.register_blueprint(my_pages)
app.register_blueprint(sql_pages)
app.secret_key = "pingu moon".encode('utf8')
app.config['USE_SESSION_FOR_NEXT'] = True

# Code for using flask-bootstrap
bootstrap = Bootstrap(app) 

"""
function before_request is executed before the first request is made.
There is a separate function called teardown_request which is executed once every request has been completed.
Since teardown_request is not needed for this application, I have not created.
e.g. if teardown_request is used to disconnect the database, every time the client has finished its request,
the database will be disconnected and therefore have to reconnect the database whenever he or she makes a new request.

g is a global variable for flask. Hence I have used the variable 
1. g.dbObject to maintain the connection til the client closes the web applicaiton,
2. g.userName to store the userName and thereby not use try except method to check the userName for each page
"""
@app.before_request
def before_request():
    if 'dbObject' not in g:
        g.dbObject = DB()
    else:
        g.dbObject.connectDB()

    if 'userName' in session:
        g.userName = str(escape(session['userName']))
        checkAdmin = g.dbObject.checkAdmin(g.userName)
        
         # Case: the user has not deleted its account
        if checkAdmin != None:
            g.adminStatus = checkAdmin[0]
        # Case: the user has deleted its account
        else: 
            g.adminStatus = None
    else:
        g.userName = None
        g.adminStatus = None

"""
HTTP status code 400 is given when there is a bug while running the app locally.
To check the cause of the bug, 
1. Make bad_request + page400 functions have been commented(?)
2. Make sure you are running the app in debug mode (it is currently executed in debug mode though)
"""
@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html', userName = g.userName, adminStatus = g.adminStatus), 400

#HTTP status code 404 is given when there is no such page for the given URL.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', userName = g.userName, adminStatus = g.adminStatus), 404
    
@app.errorhandler(408)
def request_timeout(e):
    return render_template('408.html', userName = g.userName, adminStatus = g.adminStatus), 408

@app.errorhandler(410)
def gone(e):
    return render_template('410.html', userName = g.userName, adminStatus = g.adminStatus), 410

@app.errorhandler(429)
def too_many_requests(e):
    return render_template('429.html', userName = g.userName, adminStatus = g.adminStatus), 429

@app.errorhandler(431)
def request_header_fields_too_large(e):
    return render_template('431.html', userName = g.userName, adminStatus = g.adminStatus), 431

@app.errorhandler(451)
def unavailable_for_legal_reasons(e):
    return render_template('451.html', userName = g.userName, adminStatus = g.adminStatus), 451

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', userName = g.userName, adminStatus = g.adminStatus), 500

@app.errorhandler(503)
def service_unavailable(e):
    return render_template('503.html', userName = g.userName, adminStatus = g.adminStatus), 503

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html', userName = g.userName, adminStatus = g.adminStatus)

@app.route('/signout')
def signout():
    session.pop('userName', None)
    g.dbObject.disconnectDB() # Remove the connection with the database as there is no need after signing out
    return redirect(url_for('home'))

@app.route('/signup', methods =['GET', 'POST'])
def signup():
    if request.method == 'GET':
         return render_template('signup.html', userName = g.userName)
     
    if request.method == 'POST':
        userName = request.form.get('userName')
        fullName = request.form.get('fullName')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmpassword')
        email = request.form.get('email')
        phoneNumber = request.form.get('phoneNumber')
        
        encryptedPassword = generate_password_hash(password)
        
        if not userName or not fullName or not password or not confirmPassword or not email or not phoneNumber:
            msg = 'Please fill out the form!'
            flash(msg)
            return redirect(url_for('signup')) 
        elif password != confirmPassword:
            msg = 'Please confirm your password again.'
            flash(msg)
            return redirect(url_for('signup')) 
        else:
            accountExistence = g.dbObject.checkAccountExistence(userName)[0]

            # Case: There is already an account with same userName
            if accountExistence == 1:
                msg = "The account with username as " + str(userName) + " already exists!"
                flash(msg)
                return redirect(url_for('signup')) 
            # Case: the form has been filled out
            else:
                g.dbObject.addUser(fullName, userName, encryptedPassword, email, phoneNumber)
                msg = 'You have successfully registered your account!'
                flash(msg)
                session['userName'] = userName
                g.userName = userName
                g.adminStatus = 0
                return redirect(url_for('home'))

@app.route('/signin', methods =['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html', userName = g.userName)
    
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')
        encryptedPassword = generate_password_hash(password)
        accountExistence = g.dbObject.checkAccountExistence(userName)[0]
        
        # Case: No corresponding account with the userName inputed
        if accountExistence == 0:
            msg = "There is no such account created with the username - " + str(userName) + "."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            adminStatus = g.dbObject.checkAdmin(userName)[0]
            
            # Case: the corresponding account with the userName inputed is an UserAccount
            if adminStatus == 0:
                accountID, accountPassword = g.dbObject.getUserNameAndPassword(userName)
                # Case: the user has entered its password correctly
                if userName == accountID and check_password_hash(accountPassword, password):
                    session['userName'] = accountID
                    g.userName = accountID
                    g.adminStatus = 0
                    return redirect(url_for('home'))
                # Case: the user has not entered its password correctly.
                if userName == accountID and encryptedPassword != accountPassword:
                    msg = 'Incorrect password!'
                    flash(msg)
                    return redirect(url_for('signin')) 
            # Case: the corresponding account with the userName inputed is an AdminAccount    
            if adminStatus == 1:
                accountID, accountPassword = g.dbObject.getAdminIDandPassword(userName)
                # Case: the admin has entered its password correctly
                if userName == accountID and check_password_hash(accountPassword, password):
                    session['userName'] = accountID
                    g.userName = accountID
                    g.adminStatus = 1
                    return redirect(url_for('home'))
                # Case: the admin has not entered its password correctly
                if userName == accountID and encryptedPassword != accountPassword:
                    msg = 'Incorrect password!'
                    flash(msg)
                    return redirect(url_for('signin')) 

@app.route('/links', methods = ['GET'])
def links():
    if request.method == 'GET':
        return render_template('links.html')

if __name__ == '__main__':
    app.run(debug=True)