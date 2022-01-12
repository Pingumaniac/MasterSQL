"""
These codes have been reused from my CSE 416 Software Engineering final project.

Here is the link for the reference code:
https://github.com/Pingumaniac/TheALLDictionaries/blob/main/error_pages.py
"""

from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
from python.masterSQLAPI import DB

error_pages = Blueprint("error_pages", __name__, static_folder="static", template_folder="templates")

@error_pages.route('/400', methods = ['GET'])
def page400():
    if request.method == 'GET':
        return render_template('400.html', userName = g.userName, adminStatus = g.adminStatus), 400

@error_pages.route('/408', methods = ['GET'])
def page408():
    if request.method == 'GET':
        return render_template('408.html', userName = g.userName, adminStatus = g.adminStatus), 408

"""
HTTP status code 410 is given when the page for the corresponding URL has been deleted from the server(?),
but the data for this page is stored in the cache of the client's computer.
"""
@error_pages.route('/410', methods = ['GET'])
def page410():
    if request.method == 'GET':
        return render_template('410.html', userName = g.userName, adminStatus = g.adminStatus), 410

@error_pages.route('/429', methods = ['GET'])
def page429():
    if request.method == 'GET':
        return render_template('429.html', userName = g.userName, adminStatus = g.adminStatus), 429

@error_pages.route('/431', methods = ['GET'])
def page431():
    if request.method == 'GET':
        return render_template('431.html', userName = g.userName, adminStatus = g.adminStatus), 431

@error_pages.route('/451', methods = ['GET'])
def page451():
    if request.method == 'GET':
        return render_template('451.html', userName = g.userName, adminStatus = g.adminStatus), 451

@error_pages.route('/500', methods = ['GET'])
def page500():
    if request.method == 'GET':
        return render_template('500.html', userName = g.userName, adminStatus = g.adminStatus), 500

@error_pages.route('/503', methods = ['GET'])
def page503():
    if request.method == 'GET':
        return render_template('503.html', userName = g.userName, adminStatus = g.adminStatus), 503