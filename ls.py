import pymysql
import sys
def ls():
    l = sys.argv[1].split('/')
    con = pymysql.connect(user='wtl',password='123')
    cursor = con.cursor()
    cursor.execute("USE EDFS")
    # print(l[-1])
    cursor.execute("select id from metadata where name=%s" %("'"+l[-1]+"'"))
    id = cursor.fetchone()[0]
    if(id == 0):
        print("There is no directory " + l[-1])
        return
    else:
        cursor.execute("select child from directory where parent=%d" %(id))
        data = cursor.fetchall()
        for i in data:
            # print(i[0])
            cursor.execute("select name from metadata where id=%d" % (i[0]))
            name = cursor.fetchone()[0]
            print(name, end=" ")
ls()