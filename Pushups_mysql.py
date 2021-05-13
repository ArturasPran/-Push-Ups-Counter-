""" Arturas Pranskunas
    This is the second part of "Push-Ups Counter"  project
    The project can be found at https://ehelper.tk/
  
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
"""

import mysql.connector
class postdata:
    def __init__(self, mhost, muser, mpassword):
        self.mydb = mysql.connector.connect(host=mhost, 
        user=muser, 
        password=mpassword, 
        database="PushUpsData")
        
    def resetCounter(self):
        sql = "UPDATE current_state SET Num = 0 WHERE ID = 1"
        mycursor2 = self.mydb.cursor()
        mycursor2.execute(sql)
        self.mydb.commit()
        #print("Counter Reset")

    def updateRecord(self, record):
        
        if(record == 0):
            self.resetCounter()
            return

        sql= "UPDATE current_state SET Num = Num + 1 WHERE ID = 1"
        mycursor2 = self.mydb.cursor()
        mycursor2.execute(sql)
        self.mydb.commit()
        print("Record updated")
        
    def updateProgress(self, number):
        #sql2= "INSERT INTO records (number) VALUES(0)"
        sql= """INSERT INTO records (number) VALUES(%s)"""
        val =number
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, (val,))
        self.mydb.commit()
        print("Exercise recorded. Total push ups registered: " + str(number))
        
    def updateTotalThisWeek(self):
        sqlTotal= """UPDATE personal_best SET total_this_week = (SELECT SUM(number)
        AS totalThisWeek FROM records WHERE yearweek(DATE(date), 1) = yearweek(curdate(), 1))"""
        mycursor = self.mydb.cursor()
        mycursor.execute(sqlTotal)
        self.mydb.commit()


    def updatePersonalBest(self, number):
        sqlMax= "SELECT MAX(number) FROM records"
        mycursor = self.mydb.cursor()
        mycursor.execute(sqlMax)
        myresult = mycursor.fetchall()
        pbest = myresult[0][0]
        if(pbest < number):
            sql= "UPDATE personal_best  SET personal_best="+ str(number) +" WHERE id = 1"
            mycursor = self.mydb.cursor()
            mycursor.execute(sql)
            self.mydb.commit()
            print("Previous record: " + str(pbest) + " New record: " + str(number))
        self.updateTotalThisWeek()
        self.resetCounter()

