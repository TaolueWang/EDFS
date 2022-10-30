import pymysql
import sys
def cat():
    l = sys.argv[1].split('/')
    con = pymysql.connect(user='wtl', password='123')
    cursor = con.cursor()
    cursor.execute("USE EDFS")
    cursor.execute("select id from metadata where name=%s" % ("'" + l[-1] + "'"))