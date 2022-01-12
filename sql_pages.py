from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
from python.masterSQLAPI import DB
import re
import json
import time
import datetime

sql_pages = Blueprint("sql_pages", __name__, static_folder="static", template_folder="templates")

@sql_pages.route('/level1', methods = ['GET'])
def level1():
    if request.method == 'GET':
        return render_template('level1.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/level2', methods = ['GET'])
def level2():
    if request.method == 'GET':
        return render_template('level2.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/level3', methods = ['GET'])
def level3():
    if request.method == 'GET':
        return render_template('level3.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/level1Review', methods = ['GET'])
def level1Review():
    if request.method == 'GET':
        return render_template('level1Review.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/level2Review', methods = ['GET'])
def level2Review():
    if request.method == 'GET':
        return render_template('level2Review.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/level3Review', methods = ['GET'])
def level3Review():
    if request.method == 'GET':
        return render_template('level3Review.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/checkLevel1Answer1/<string:userQuery>', methods = ['GET'])
def checkLevel1Answer1(userQuery):
    if request.method == 'GET':
        sampleQuery = "SELECT * FROM Apple_M_Series;"
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer2/<string:userQuery>', methods = ['GET'])    
def checkLevel1Answer2(userQuery):
    if request.method == 'GET':
        sampleQuery = "SELECT COUNT(*) AS No_of_Apple_M_Series FROM Apple_M_Series;"
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer3/<string:userQuery>', methods = ['GET'])
def checkLevel1Answer3(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT modelName, chipName, SSD, price FROM MacBookPro WHERE hasNotch = 1;'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer4/<string:userQuery>', methods = ['GET'])    
def checkLevel1Answer4(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT modelName, chipName, SSD, price FROM MacBookPro WHERE NOT hasNotch = 1;'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer5/<string:userQuery>', methods = ['GET'])      
def checkLevel1Answer5(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT * FROM MacBookPro ORDER BY price DESC;'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer6/<string:userQuery>', methods = ['GET'])   
def checkLevel1Answer6(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT * FROM MacBookPro ORDER BY price ASC;'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer7/<string:userQuery>', methods = ['GET'])       
def checkLevel1Answer7(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT COUNT(*) AS "No_of_MacBook_Pro" FROM MacBookPro;'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer8/<string:userQuery>', methods = ['GET'])   
def checkLevel1Answer8(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT MAX(price) AS "maximum_price" FROM MacBookPro;'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer9/<string:userQuery>', methods = ['GET'])   
def checkLevel1Answer9(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT MIN(price) AS "minimum_price" FROM MacBookPro;'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel1Answer10/<string:userQuery>', methods = ['GET'])   
def checkLevel1Answer10(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT MIN(price) AS "minimum_price" FROM MacBookPro WHERE modelName = "MacBook Pro 16";'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer1/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer1(userQuery):
    if request.method == 'GET':
        sampleQuery = """SELECT Mathematics.StudentID, Mathematics.StudentName, Mathematics.GPA AS Math_GPA, 
                         English.GPA AS English_GPA FROM Mathematics INNER JOIN English ON 
                         Mathematics.StudentID = English.StudentID;"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer2/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer2(userQuery):
    if request.method == 'GET':
        sampleQuery = """SELECT Mathematics.StudentID, Mathematics.StudentName, Mathematics.GPA AS Math_GPA, 
                         English.GPA AS English_GPA FROM Mathematics LEFT JOIN English ON 
                         Mathematics.StudentID = English.StudentID;"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer3/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer3(userQuery):
    if request.method == 'GET':
        sampleQuery = """SELECT English.StudentID, English.StudentName, Mathematics.GPA AS Math_GPA, 
                         English.GPA AS English_GPA FROM Mathematics RIGHT JOIN English ON 
                         Mathematics.StudentID = English.StudentID;"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer4/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer4(userQuery):
    if request.method == 'GET':
        sampleQuery = """(SELECT Mathematics.StudentID, Mathematics.StudentName, Mathematics.GPA AS Math_GPA, 
                         English.GPA AS English_GPA FROM Mathematics LEFT JOIN English ON 
                         Mathematics.StudentID = English.StudentID) UNION
                         (SELECT English.StudentID, English.StudentName, Mathematics.GPA AS Math_GPA, 
                         English.GPA AS English_GPA FROM Mathematics RIGHT JOIN English ON 
                         Mathematics.StudentID = English.StudentID);"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer5/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer5(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT AVG(GPA) AS "average_gpa" FROM Mathematics WHERE StudentID IN (SELECT StudentID FROM English);'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer6/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer6(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT AVG(GPA) AS "average_gpa" FROM Mathematics WHERE StudentID NOT IN (SELECT StudentID FROM English);'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer7/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer7(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT MAX(GPA) AS "highest_gpa" FROM Mathematics WHERE StudentID IN (SELECT StudentID FROM English);'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer8/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer8(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT MIN(GPA) AS "lowest_gpa" FROM Mathematics WHERE StudentID IN (SELECT StudentID FROM English);'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer9/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer9(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT MAX(GPA) AS "highest_gpa" FROM Mathematics WHERE StudentID NOT IN (SELECT StudentID FROM English);'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel2Answer10/<string:userQuery>', methods = ['GET'])   
def checkLevel2Answer10(userQuery):
    if request.method == 'GET':
        sampleQuery = 'SELECT MIN(GPA) AS "lowest_gpa" FROM Mathematics WHERE StudentID NOT IN (SELECT StudentID FROM English);'
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel3Answer1/<string:userQuery>', methods = ['GET'])   
def checkLevel3Answer1(userQuery):
    if request.method == 'GET':
        sampleQuery = """SELECT manufacturer, COUNT(caseName) AS  Number_of_iPhone_13_Pro_Max_Cases 
                         FROM iPhone13ProMaxCase GROUP BY manufacturer;"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel3Answer2/<string:userQuery>', methods = ['GET'])   
def checkLevel3Answer2(userQuery):
    if request.method == 'GET':
        sampleQuery = "SELECT manufacturer FROM iPhone13ProMaxCase GROUP BY manufacturer HAVING COUNT(caseName) >= 2;"
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel3Answer3/<string:userQuery>', methods = ['GET'])   
def checkLevel3Answer3(userQuery):
    if request.method == 'GET':
        sampleQuery = """SELECT manufacturer FROM iPhone13ProMaxCase WHERE manufacturer <> 'Apple' GROUP BY manufacturer
                         HAVING COUNT(caseName) >= 2;"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel3Answer4/<string:userQuery>', methods = ['GET'])   
def checkLevel3Answer4(userQuery):
    if request.method == 'GET':
        sampleQuery = """SELECT manufacturer, COUNT(caseName) AS  Number_of_AirTag_Cases FROM AirTagCase 
                         WHERE AirTagCase.manufacturer IN (SELECT manufacturer FROM iPhone13ProMaxCase) 
                         GROUP BY manufacturer;"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/checkLevel3Answer5/<string:userQuery>', methods = ['GET'])   
def checkLevel3Answer5(userQuery):
    if request.method == 'GET':
        sampleQuery = """SELECT manufacturer, COUNT(caseName) AS  Number_of_AirTag_Cases FROM AirTagCase 
                         WHERE AirTagCase.manufacturer NOT IN (SELECT manufacturer FROM iPhone13ProMaxCase) 
                         GROUP BY manufacturer;"""
        return g.dbObject.checkSelectQuery(userQuery, sampleQuery)

@sql_pages.route('/submitScoreLevel1', methods = ['POST'])
def submitScoreLevel1():
    if request.method == 'POST':
        if g.userName == None:
            return json.dumps({'status': False, 'reason': 'not signed in'})
        else:
            scoresInJSON = request.get_json()
            markForEach = scoresInJSON.get('markForEach')

            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            g.dbObject.insertTest1Score(g.userName, markForEach[0], markForEach[1], markForEach[2], markForEach[3],
            markForEach[4], markForEach[5], markForEach[6], markForEach[7], markForEach[8], markForEach[9], timestamp)
            return json.dumps({'status': True, 'reason': 'score saved successfully to database'})

@sql_pages.route('/submitScoreLevel2', methods = ['POST'])
def submitScoreLevel2():
    if request.method == 'POST':
        if g.userName == None:
            return json.dumps({'status': False, 'reason': 'not signed in'})
        else:
            scoresInJSON = request.get_json()
            markForEach = scoresInJSON.get('markForEach')

            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            g.dbObject.insertTest2Score(g.userName, markForEach[0], markForEach[1], markForEach[2], markForEach[3],
            markForEach[4], markForEach[5], markForEach[6], markForEach[7], markForEach[8], markForEach[9], timestamp)
            return json.dumps({'status': True, 'reason': 'score saved successfully to database'})
            

@sql_pages.route('/submitScoreLevel3', methods = ['POST'])
def submitScoreLevel3():
    if request.method == 'POST':
        if g.userName == None:
            return json.dumps({'status': False, 'reason': 'not signed in'})
        else:
            scoresInJSON = request.get_json()
            markForEach = scoresInJSON.get('markForEach')

            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            g.dbObject.insertTest3Score(g.userName, markForEach[0], markForEach[1], markForEach[2], markForEach[3], 
            markForEach[4], timestamp)
            return json.dumps({'status': True, 'reason': 'score saved successfully to database'})

@sql_pages.route('/createTableSQL', methods = ['GET'])
def createTableSQL():
    if request.method == 'GET':
        return render_template('createTableSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/dropTableSQL', methods = ['GET'])
def dropTableSQL():
    if request.method == 'GET':
        return render_template('dropTableSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/insertDataSQL', methods = ['GET'])
def insertDataSQL():
    if request.method == 'GET':
        return render_template('insertDataSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/selectDataSQL', methods = ['GET'])
def selectDataSQL():
    if request.method == 'GET':
        return render_template('selectDataSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/updateDataSQL', methods = ['GET'])
def updateDataSQL():
    if request.method == 'GET':
        return render_template('updateDataSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/deleteDataSQL', methods = ['GET'])
def deleteDataSQL():
    if request.method == 'GET':
        return render_template('deleteDataSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/foreignKeysSQL', methods = ['GET'])
def foreignKeysSQL():
    if request.method == 'GET':
        return render_template('foreignKeysSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/joinSQL', methods = ['GET'])
def joinSQL():
    if request.method == 'GET':
        return render_template('joinSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/nestedQueriesSQL', methods = ['GET'])
def nestedQueriesSQL():
    if request.method == 'GET':
        return render_template('nestedQueriesSQL.html', userName = g.userName, adminStatus = g.adminStatus)

@sql_pages.route('/groupByHavingSQL', methods = ['GET'])
def groupByHavingSQL():
    if request.method == 'GET':
        return render_template('groupByHavingSQL.html', userName = g.userName, adminStatus = g.adminStatus)