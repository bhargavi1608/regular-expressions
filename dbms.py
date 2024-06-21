import sqlite3

conn =sqlite3.connect("iare") # to connect to a database
cur=conn.cursor()#function 2, to get cursor obj  
cur.execute("")#to execute queries
#cur.fetchmany()             #for particular rows(2,3....)
result=cur.fetchall()#to fetch result
print(*result,sep="\n")#print result

conn.close()#closing db connection
# SQL comands-DML,DDL,DQL
#DDL=DATA DEFINATION LANG   #CREATE TABLES,DROP=DELETE COMPLETE DATA,TABLE TRUNCATE=DEL THE DATA WHILE ENTERING THE TABLE STRUCTURE
#DML=DATA MANIPULATION LANG #INSERT UPDATE DELETE(TABLE WILL BE BUT DATA DEL)
#DQL=DATA QUERY LANG        #SELECT
