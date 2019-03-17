import sqlite3 as sql
import codecs

with codecs.open('database.db', 'a', 'utf-8-sig'):

    def insertUser(username, password):
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
        con.commit()
        con.close()


    def retrieveUsers():
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("SELECT username, password FROM users")
        users = cur.fetchall()
        con.close()
        return users


    def insertPatientDetails(patient_id,age, sex,bp,cholesterol,blood_sugar,heart_rate,exercise):
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO patient_info (patient_id,age, sex,bp,cholestrol,blood_sugar,heart_rate,exercise) VALUES (?,?,?,?,?,?,?,?)", (patient_id,age, sex,bp,cholesterol,blood_sugar,
                             heart_rate,exercise))
        con.commit()
        con.close()
