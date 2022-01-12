"""
These codes have been reused from my CSE 416 Software Engineering final project.

Here is the link for the reference code:
https://github.com/Pingumaniac/TheALLDictionaries/blob/main/my_pages.py

Note that I have removed the functionalities for making friends as they were irrelevant to this project.
"""

from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
from python.masterSQLAPI import DB
import re

my_pages = Blueprint("my_pages", __name__, static_folder="static", template_folder="templates")

@my_pages.route('/mypage', methods = ['GET', 'POST'])
def mypage():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access My Page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            test1Table = g.dbObject.getTest1Score(g.userName)
            test2Table = g.dbObject.getTest2Score(g.userName)
            test3Table = g.dbObject.getTest3Score(g.userName)

            # Case: the client is a user
            if g.adminStatus == 0:
                accountFullName, accountName, accountPassword, accountEmail, accountPhoneNumber, accountPicture  = g.dbObject.getUserData(g.userName)       
                return render_template('mypage.html', userName = accountName, fullName = accountFullName,
                                       accountPassword = accountPassword, accountEmail = accountEmail,
                                       accountPhoneNumber = accountPhoneNumber, accountPicture = accountPicture, 
                                       adminStatus = g.adminStatus, 
                                       test1Table = test1Table, test2Table = test2Table, test3Table = test3Table)
                
            # Case: the client is an administrator    
            if g.adminStatus == 1:
                accountFullName, accountName, accountPassword, accountEmail, accountPhoneNumber, accountJobTitle, accountPicture  = g.dbObject.getAdminData(g.userName)
                
                return render_template('mypage.html', userName = accountName, fullName = accountFullName,
                                       accountPassword = accountPassword, accountEmail = accountEmail,
                                       accountPhoneNumber = accountPhoneNumber, accountJobTitle = accountJobTitle,
                                       accountPicture = accountPicture, adminStatus = g.adminStatus,
                                       test1Table = test1Table, test2Table = test2Table, test3Table = test3Table)
    if request.method == 'POST':            
        deletePicture = request.form.get('deletePicture')
        deleteDistinctTest1Score = request.form.get('deleteDistinctTest1Score')
        deleteDistinctTest2Score = request.form.get('deleteDistinctTest2Score')
        deleteDistinctTest3Score = request.form.get('deleteDistinctTest3Score')

        print(request.form)

        if isDeletePicture != None:
            # Differentiated the case as the profile picture URL is stored in different tables
            # Case: the client is a user
            if g.adminStatus == 0:
                g.dbObject.deleteUserProfilePicture(g.userName)
            # Case: the client is an administrator
            if g.adminStatus == 1:
                g.dbObject.deleteAdminProfilePicture(g.userName)
            msg = "Profile picture deleted successfully"
            flash(msg)
            return redirect(url_for('my_pages.mypage')) 

        if deleteDistinctTest1Score != None:
            g.dbObject.deleteDistinctTest1Score(g.userName, deleteDistinctTest1Score)
            return redirect(url_for('my_pages.mypage')) 

        if deleteDistinctTest2Score != None:
            g.dbObject.deleteDistinctTest2Score(g.userName, deleteDistinctTest2Score)
            return redirect(url_for('my_pages.mypage')) 

        if deleteDistinctTest3Score != None:
            g.dbObject.deleteDistinctTest3Score(g.userName, deleteDistinctTest3Score)
            return redirect(url_for('my_pages.mypage')) 

@my_pages.route('/changeProfilePicture', methods = ['GET', 'POST'])
def changeProfilePicture():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access change profile picture page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            return render_template('changeProfilePicture.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        newURL = request.form["newProfile"]
        currentPassword = request.form["currentPassword"]
        
        # Case: the client is a user
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its password correctly
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateUserProfilePictureURL(accountUserName, newURL)  
                msg = "Your profile picture has been updated successfully!" 
                flash(msg)
                return redirect(url_for('my_pages.mypage')) 
            # Case: the user has not entered its password correctly.
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changeProfilePicture')) 
        # Case: the client is an administrator        
        if g.adminStatus == 1:
            accountUserName, accountPassword = g.dbObject.getAdminUserNameAndPassword(g.userName)
            # Case: the admin has entered its password correctly.    
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateAdminProfilePictureURL(accountUserName, newURL) 
                msg = "Your profile picture has been updated successfully!" 
                flash(msg)    
                return redirect(url_for('my_pages.mypage')) 
            # Case: the admin has not entered its password correctly.
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changeProfilePicture')) 
                
@my_pages.route('/changeFullName', methods = ['GET', 'POST'])
def changeFullName():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access change full name page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            return render_template('changeFullName.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        newFullName = request.form["newFullName"]
        currentPassword = request.form["currentPassword"]
        # Case: the client is a user.
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its password correctly.
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateUserFullName(accountUserName, newFullName)  
                msg = "Your full name has been updated successfully!" 
                flash(msg)
                return redirect(url_for('my_pages.mypage'))    
            # Case: the user has not entered its password correctly.
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changeFullName'))    
        # Case: the client is an administrator        
        if g.adminStatus == 1:
            accountUserName, accountPassword = g.dbObject.getAdminUserNameAndPassword(g.userName)
            # Case: the admin has entered its password correctly.    
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateAdminFullName(accountUserName, newFullName) 
                msg = "Your full name has been updated successfully!" 
                flash(msg)
                return redirect(url_for('my_pages.mypage'))
            # Case: the admin has not entered its password correctly.
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changeFullName'))  

@my_pages.route('/changePassword', methods = ['GET', 'POST'])
def changePassword():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access change password page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            return render_template('changePassword.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        currentPassword = request.form["currentPassword"]
        newPassword = request.form["newPassword"]
        confirmPassword = request.form["confirmPassword"]
        
        if currentPassword != confirmPassword:
            msg = "Please confirm your new password correctly"
            flash(msg)
            return redirect(url_for('my_pages.changePassword')) 
        
        # Case: the client is a user
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its password correctly
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                newEncryptedPassword = generate_password_hash(newPassword)
                g.dbObject.updateUserPassword(accountUserName, newEncryptedPassword)  
                msg = "Your password has been updated successfully!" 
                flash(msg)
                return redirect(url_for('my_pages.mypage'))
            # Case: the user has not entered its password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changePassword')) 
        # Case: the client is an admin       
        if g.adminStatus == 1:
            accountUserName, accountPassword = g.dbObject.getAdminUserNameAndPassword(g.userName)
            # Case: the admin has entered its password correctly
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                newEncryptedPassword = generate_password_hash(newPassword) 
                g.dbObject.updateAdminPassword(accountUserName, newEncryptedPassword) 
                msg = "Your password has been updated successfully!" 
                flash(msg)    
                return redirect(url_for('my_pages.mypage'))
            # Case: the admin has not entered its password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changePassword')) 

@my_pages.route('/changeEmail', methods = ['GET', 'POST'])
def changeEmail():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access change email page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            return render_template('changeEmail.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        newEmail = request.form["newEmail"]
        currentPassword = request.form["currentPassword"]
        
        # Case: the client is a user
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its password correctly
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateUserEmail(accountUserName, newEmail)  
                msg = "Your email has been updated successfully!" 
                flash(msg)
                return redirect(url_for('my_pages.mypage'))
            # Case: the user has not entered its password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changeEmail')) 
        # Case: the client is an admin        
        if g.adminStatus == 1:
            accountUserName, accountPassword = g.dbObject.getAdminUserNameAndPassword(g.userName)
            # Case: the admin has entered its password correctly    
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateAdminEmail(accountUserName, newEmail) 
                msg = "Your email has been updated successfully!" 
                flash(msg)    
                return redirect(url_for('my_pages.mypage'))
            # Case: the admin has not entered its password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changeEmail')) 

@my_pages.route('/changePhone', methods = ['GET', 'POST'])
def changePhone():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access change phone number page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            return render_template('changePhone.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        newPhone = request.form["newPhone"]
        currentPassword = request.form["currentPassword"]
        # Case: the client is a user
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its password correctly
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateUserPhoneNumber(accountUserName, newPhone)  
                msg = "Your phone number has been updated successfully!" 
                flash(msg)
                return redirect(url_for('my_pages.mypage'))
            # Case: the user has not entered its password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changePhone')) 
        # Case: the admin is the client         
        if g.adminStatus == 1:
            accountUserName, accountPassword = g.dbObject.getAdminUserNameAndPassword(g.userName)
            # Case: the admin has entered its password correctly
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateAdminPhoneNumber(accountUserName, newPhone) 
                msg = "Your phone number has been updated successfully!" 
                flash(msg)    
                return redirect(url_for('my_pages.mypage'))
            # Case: the admin has not entered its password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changePhone')) 

@my_pages.route('/unsubscribe', methods = ['GET', 'POST'])
def unsubscribe():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access cancel subscription page."
            flash(msg)
            return redirect(url_for('signin')) 
        elif g.adminStatus == 1:
            msg = "Please users can access cancel subscription page."
            flash(msg)
            return redirect(url_for('search')) 
        else:
            return render_template('unsubscribe.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        currentID = request.form["currentID"]
        currentPassword = request.form["currentPassword"]
        # Case: the client is a user
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its userName and password correctly
            if currentID == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateUserSubscriptionStatus(accountUserName, 0)  
                msg = "You have unsubscribed successfully." 
                flash(msg)
                return redirect(url_for('my_pages.mypage'))
            # Case: the user has not entered its userName or password correctly
            else:
                msg = "Please enter your userName and password correctly"
                flash(msg)
                return redirect(url_for('my_pages.unsubscribe')) 

@my_pages.route('/resetSearchHistories', methods = ['GET', 'POST'])
def resetSearchHistories():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access reset search histories page."
            flash(msg)
            return redirect(url_for('signin')) 
        elif g.adminStatus == 1:
            msg = "Only users can access reset search histories page."
            flash(msg)
            return redirect(url_for('search')) 
        else:
            return render_template('resetSearchHistories.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        currentID = request.form["currentID"]
        currentPassword = request.form["currentPassword"]
        # Case: the client is a user
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its userName and password correctly
            if currentID == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.deleteAllSearchHistory(accountUserName)  
                msg = "You search histories have been all deleted." 
                flash(msg)
                return redirect(url_for('my_pages.mypage'))
            # Case: the user has not entered its userName or password correctly
            else:
                msg = "Please enter your userName and password correctly"
                flash(msg)
                return redirect(url_for('my_pages.resetSearchHistories')) 

@my_pages.route('/changeJob', methods = ['GET', 'POST'])
def changeJob():    
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access change job title page."
            flash(msg)
            return redirect(url_for('signin')) 
        if g.adminStatus != 1:
            msg = "Only administrators can access job title page."
            flash(msg)
            return redirect(url_for('search')) 
        else:
            return render_template('changeJob.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        newNickName = request.form["newJob"]
        currentPassword = request.form["currentPassword"]  
        # Case: the client is the admin        
        if g.adminStatus == 1:
            accountUserName, accountPassword = g.dbObject.getAdminUserNameAndPassword(g.userName)
            # Case: the admin has entered its password correctly    
            if g.userName == accountUserName and check_password_hash(accountPassword, currentPassword):
                g.dbObject.updateAdminJobTitle(accountUserName, newNickName) 
                msg = "Your job title has been updated successfully!" 
                flash(msg)    
                return redirect(url_for('my_pages.mypage'))
            # Case: the admin has not entered its password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.changeJob'))  

@my_pages.route('/deleteAccount', methods = ['GET', 'POST'])
def deleteAccount():    
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access delete account page."
            flash(msg)
            return redirect(url_for('search')) 
        else:
            return render_template('deleteAccount.html', userName = g.userName, adminStatus = g.adminStatus)
        
    if request.method == 'POST':
        currentID = request.form["currentID"]
        currentPassword = request.form["currentPassword"]
        confirmPassword = request.form["confirmPassword"]
        
        if currentPassword != confirmPassword:
            msg = "Please confirm your password correctly"
            flash(msg)
            return redirect(url_for('my_pages.deleteAccount')) 
        
        # Case: the client is the user
        if g.adminStatus == 0:
            accountUserName, accountPassword = g.dbObject.getUserNameAndPassword(g.userName)
            # Case: the user has entered its userName and password correctly
            if accountUserName == currentID and check_password_hash(accountPassword, currentPassword):
                g.dbObject.deleteUser(accountUserName)  
                msg = "Your account has been deleted successfully!" 
                flash(msg)
                return redirect(url_for('signout'))
            # Case: the user has not entered its userName or password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.deleteAccount'))    
        # Case: the client is the admin        
        if g.adminStatus == 1:
            accountUserName, accountPassword = g.dbObject.getAdminUserNameAndPassword(g.userName)
            # Case: the admin has entered its userName and password correctly    
            if accountUserName == currentID and check_password_hash(accountPassword, currentPassword):
                g.dbObject.deleteAdmin(accountUserName)  
                msg = "Your account has been deleted successfully!" 
                flash(msg)
                return redirect(url_for('signout'))
            # Case: the admin has not entered its userName or password correctly
            else:
                msg = "Please enter your current password correctly"
                flash(msg)
                return redirect(url_for('my_pages.deleteAccount'))  