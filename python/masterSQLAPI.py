import pymysql
import json
class DB():
    def __init__(self):
        self.conn = pymysql.connect(
                    host =  'database-2.cpvwrnt4qvgc.ap-northeast-2.rds.amazonaws.com',
                    port = 3306,
                    user = 'admin',
                    password = 'bushmoon18',
                    database = 'sys',
                    )
        self.cursor = self.conn.cursor()
        
    def connectDB(self):
        if self.conn.open != True:
            self.conn = pymysql.connect(
                host =  'database-2.cpvwrnt4qvgc.ap-northeast-2.rds.amazonaws.com',
                port = 3306,
                user = 'admin',
                password = 'bushmoon18',
                database = 'sys',
                )
            self.cursor = self.conn.cursor()
    
    def disconnectDB(self):
        self.conn.close()
    
    def getUserName(self, userName):    
        query = "SELECT userName FROM Account WHERE id = %s"
        self.cursor.execute(query, (userName, ))
        returnValue = self.cursor.fetchone()
        
        return returnValue[0] if returnValue else None
    
    def addUser(self, fullName, userName, password, email, phoneNumber):
        query1 = 'INSERT INTO Account VALUES (%s, %s)'
        query2 = 'INSERT INTO UserAccount VALUES (%s, %s, %s, %s, %s, NULL)'
        
        isAdmin = False
            
        self.cursor.execute(query1, (userName, isAdmin, )) 
        self.cursor.execute(query2, (fullName, userName, password, email, phoneNumber, )) 
        self.conn.commit()
    
    def addAdmin(self, fullName, userName, password, email, phoneNumber, jobTitle):
        query1 = 'INSERT INTO Account VALUES (%s, %s)'
        query2 = 'INSERT INTO AdminAccount VALUES (%s, %s, %s, %s, %s, NULL, %s)'
    
        isAdmin = True
            
        self.cursor.execute(query1, (userName, isAdmin, )) 
        self.cursor.execute(query2, (fullName, userName, password, email, phoneNumber, jobTitle, )) 
        self.conn.commit()

    def checkAccountExistence(self, userName):
        query1 = 'SELECT COUNT(userName) FROM Account where userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        accountExistence = self.cursor.fetchone()
        return accountExistence

    def checkUserAccountExistence(self, userName):
        query1 = 'SELECT COUNT(userName) FROM UserAccount where userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        accountExistence = self.cursor.fetchone()
        return accountExistence

    def checkAdmin(self, userName):
        query1 = 'SELECT isAdmin FROM Account where userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        adminStatus = self.cursor.fetchone()
        return adminStatus

    def deleteUser(self, userName):
        query1 = 'DELETE FROM Test1Scores WHERE userName = (%s)'
        query2 = 'DELETE FROM Test2Scores WHERE userName = (%s)'
        query3 = 'DELETE FROM Test3Scores WHERE userName = (%s)'
        query4 = 'DELETE FROM UserAccount WHERE userName = (%s)'
        query5 = 'DELETE FROM Account WHERE userName = (%s)'
    
        self.cursor.execute(query1, (userName, ))
        self.cursor.execute(query2, (userName, ))
        self.cursor.execute(query3, (userName, ))
        self.cursor.execute(query4, (userName, ))
        self.cursor.execute(query5, (userName, ))
        self.conn.commit()
    
    def deleteAdmin(self, userName):
        query1 = 'DELETE FROM Test1Scores WHERE userName = (%s)'
        query2 = 'DELETE FROM Test2Scores WHERE userName = (%s)'
        query3 = 'DELETE FROM Test3Scores WHERE userName = (%s)'
        query4 = 'DELETE FROM AdminAccount WHERE userName = (%s)'
        query5 = 'DELETE FROM Account WHERE userName = (%s)'

        self.cursor.execute(query1, (userName, ))
        self.cursor.execute(query2, (userName, ))
        self.cursor.execute(query3, (userName, ))
        self.cursor.execute(query4, (userName, ))
        self.cursor.execute(query5, (userName, ))
        self.conn.commit()
    
    def getUserData(self, userName):
        query1 = 'SELECT * FROM UserAccount WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userDataTable = self.cursor.fetchone()
        return userDataTable

    def getUserNameAndPassword(self, userName):
        query1 = 'SELECT userName, password FROM UserAccount WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userDataTable = self.cursor.fetchone()
        return userDataTable
    
    def getUserFullName(self, userName):
        query1 = 'SELECT fullName FROM UserAccount WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userDataTable = self.cursor.fetchone()
        return userDataTable

    def getUserNickName(self, userName):
        query1 = 'SELECT nickName FROM UserAccount WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userDataTable = self.cursor.fetchone()
        return userDataTable

    def getUserProfilePicture(self, userName):
        query1 = 'SELECT profilePictureURL FROM UserAccount WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        userDataTable = self.cursor.fetchone()
        return userDataTable

    def getAdminData(self, userName):
        query1 = 'SELECT * FROM AdminAccount WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        adminDataTable = self.cursor.fetchone()
        return adminDataTable

    def getAdminUserNameAndPassword(self, userName):
        query1 = 'SELECT userName, password FROM AdminAccount WHERE userName = (%s)'
        self.cursor.execute(query1, (userName, ))
        adminDataTable = self.cursor.fetchone()
        return adminDataTable

    def updateUserProfilePictureURL(self, userName, newURL):
        query = 'UPDATE UserAccount SET profilePictureURL = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newURL, userName, ))
        self.conn.commit()
    
    def updateAdminProfilePictureURL(self, userName, newURL):
        query = 'UPDATE AdminAccount SET profilePictureURL = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newURL, userName, ))
        self.conn.commit()
    
    def deleteUserProfilePicture(self, userName):
        query = 'UPDATE UserAccount SET profilePictureURL = NULL WHERE userName = (%s)'
        self.cursor.execute(query, (userName, ))
        self.conn.commit()
        
    def deleteAdminProfilePicture(self, userName):
        query = 'UPDATE AdminAccount SET profilePictureURL = NULL WHERE userName = (%s)'
        self.cursor.execute(query, (userName, ))
        self.conn.commit()
    
    def updateUserFullName(self, userName, newFullName):
        query = 'UPDATE UserAccount SET fullName = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newFullName, userName, ))
        self.conn.commit()
    
    def updateAdminFullName(self, userName, newFullName):
        query = 'UPDATE AdminAccount SET fullName = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newFullName, userName, ))
        self.conn.commit()
    
    def updateUserNickName(self, userName, newNickName):
        query = 'UPDATE UserAccount SET nickName = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newNickName, userName, ))
        self.conn.commit()
    
    def updateAdminNickName(self, userName, newNickName):
        query = 'UPDATE AdminAccount SET nickName = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newNickName, userName, ))
        self.conn.commit()
    
    def updateUserPassword(self, userName, newPassword):
        query = 'UPDATE UserAccount SET password = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newPassword, userName, ))
        self.conn.commit()
    
    def updateAdminPassword(self, userName, newPassword):
        query = 'UPDATE AdminAccount SET password = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newPassword, userName, ))
        self.conn.commit()
    
    def updateUserEmail(self, userName, newEmail):
        query = 'UPDATE UserAccount SET email = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newEmail, userName, ))
        self.conn.commit()
    
    def updateAdminEmail(self, userName, newEmail):
        query = 'UPDATE AdminAccount SET email = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newEmail, userName, ))
        self.conn.commit()
    
    def updateUserPhoneNumber(self, userName, newPhoneNumber):
        query = 'UPDATE UserAccount SET phoneNumber = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newPhoneNumber, userName, ))
        self.conn.commit()
    
    def updateAdminPhoneNumber(self, userName, newPhoneNumber):
        query = 'UPDATE AdminAccount SET phoneNumber = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newPhoneNumber, userName, ))
        self.conn.commit()
    
    def updateAdminJobTitle(self, userName, newJobTitle):
        query = 'UPDATE AdminAccount SET jobTitle = (%s) WHERE userName = (%s)'
        self.cursor.execute(query, (newJobTitle, userName, ))
        self.conn.commit()
    
    def checkSelectQuery(self, userQuery, sampleQuery):
        self.cursor.execute(sampleQuery)
        sampleTableColumns = [value[0] for value in self.cursor.description]
        sampleAnswer = self.cursor.fetchall()
        try:
            self.cursor.execute(userQuery)
            userTableColumns = [value[0] for value in self.cursor.description]
            userAnswer = self.cursor.fetchall()
        except:
            userAnswer = 'Error'
            userTableColumns = None
        
        isIdentical = True
        if set(userTableColumns) != set(sampleTableColumns):
            isIdentical = False
        elif len(userTableColumns) != len(sampleTableColumns):
            isIdentical = False
        else:
            for i in range(0, len(userTableColumns)):
                if set(userTableColumns[i]) != set(sampleTableColumns[i]):
                    isIdentical = False
        
        return json.dumps({'userTable' : userAnswer, 'userTableColumns' : userTableColumns, 
                           'sampleTable' : sampleAnswer, 'sampleTableColumns' : sampleTableColumns,
                           'isIdentical' : isIdentical})

    def insertTest1Score(self, userName, q1Status, q2Status, q3Status, q4Status, q5Status, q6Status, q7Status, q8Status, q9Status, q10Status, dateAndTime):
        query = "INSERT INTO Test1Scores VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (userName, q1Status, q2Status, q3Status, q4Status, q5Status, q6Status, q7Status, q8Status, q9Status, q10Status, dateAndTime))
        self.conn.commit()

    def insertTest2Score(self, userName, q1Status, q2Status, q3Status, q4Status, q5Status, q6Status, q7Status, q8Status, q9Status, q10Status, dateAndTime):
        query = "INSERT INTO Test2Scores VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (userName, q1Status, q2Status, q3Status, q4Status, q5Status, q6Status, q7Status, q8Status, q9Status, q10Status, dateAndTime))
        self.conn.commit()

    def insertTest3Score(self, userName, q1Status, q2Status, q3Status, q4Status, q5Status, dateAndTime):
        query = "INSERT INTO Test3Scores VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (userName, q1Status, q2Status, q3Status, q4Status, q5Status, dateAndTime))
        self.conn.commit()
    
    def getTest1Score(self, userName):
        query = """SELECT q1Status + q2Status + q3Status + q4Status + q5Status + q6Status 
                   + q7Status + q8Status +  q9Status + q10Status AS totalScore,
                   q1Status, q2Status, q3Status, q4Status, q5Status, q6Status, q7Status, q8Status, 
                   q9Status, q10Status, dateAndTime FROM Test1Scores WHERE userName = (%s) ORDER BY dateAndTime DESC"""
        self.cursor.execute(query, (userName, ))
        test1History = self.cursor.fetchall()
        return test1History
    
    def getTest2Score(self, userName):
        query = """SELECT q1Status + q2Status + q3Status + q4Status + q5Status + q6Status 
                   + q7Status + q8Status +  q9Status + q10Status AS totalScore,
                   q1Status, q2Status, q3Status, q4Status, q5Status, q6Status, q7Status, q8Status, 
                   q9Status, q10Status, dateAndTime FROM Test2Scores WHERE userName = (%s) ORDER BY dateAndTime DESC"""
        self.cursor.execute(query, (userName, ))
        test2History = self.cursor.fetchall()
        return test2History
    
    def getTest3Score(self, userName):
        query = """SELECT q1Status + q2Status + q3Status + q4Status + q5Status AS totalScore,
                   q1Status, q2Status, q3Status, q4Status, q5Status, dateAndTime FROM Test3Scores WHERE userName = (%s) 
                   ORDER BY dateAndTime DESC"""
        self.cursor.execute(query, (userName, ))
        test3History = self.cursor.fetchall()
        return test3History
    
    def deleteDistinctTest1Score(self, userName, dateAndTime):
        query = "DELETE FROM Test1Scores WHERE userName = (%s) AND dateAndTime = (%s)"
        self.cursor.execute(query, (userName, dateAndTime))
        self.conn.commit()
    
    def deleteDistinctTest2Score(self, userName, dateAndTime):
        query = "DELETE FROM Test2Scores WHERE userName = (%s) AND dateAndTime = (%s)"
        self.cursor.execute(query, (userName, dateAndTime))
        self.conn.commit()
    
    def deleteDistinctTest3Score(self, userName, dateAndTime):
        query = "DELETE FROM Test3Scores WHERE userName = (%s) AND dateAndTime = (%s)"
        self.cursor.execute(query, (userName, dateAndTime))
        self.conn.commit()