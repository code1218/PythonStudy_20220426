import os
import pymysql

con = pymysql.connect(host='127.0.0.1', port=8001, user='root', password='toor', database='python_junil')
cur = con.cursor()

sql = 'select * from user_mst'
cur.execute(sql)

result = cur.fetchall()
os.system('cls')
for user in result:
    print(user)
con.close()