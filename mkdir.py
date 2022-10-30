import pymysql
import sys
def mkdir():
    dir = sys.argv[1]
    l = dir.split('/')
    con = pymysql.connect(user='wtl',password='123')
    cursor = con.cursor();
    cursor.execute("USE EDFS")
    if(l.__len__() >= 2):
        child = l[-1]
        parent = l[-2]
        for i in range(l.__len__() - 1):
            print(l[i])
            cursor.execute("select count(*) from metadata where name='" + l[i] + "';")
            data = cursor.fetchone()
            print(data)
            if data[0] == 0:
                print("there exist no directory " + l[i])
                return
        cursor.execute("select count(*) from metadata;")
        data = cursor.fetchone()
        id = data[0] + 1
        cursor.execute("insert into metadata value(%d,'dir',%s,1);" % (id, "'" + l[-1] + "'"))
        cursor.execute("select id from metadata where name = %s;" % ("'" + child + "'"))
        child = cursor.fetchone()[0]
        cursor.execute("select id from metadata where name = %s;" % ("'" + parent + "'"))
        parent = cursor.fetchone()[0]
        cursor.execute("insert into directory value(%d,%d)" %(child, parent))
    else:
        cursor.execute("select count(*) from metadata where name='" + l[0] + "';")
        data = cursor.fetchall()
        if data[0][0] == 0:
            cursor.execute("select count(*) from metadata;")
            id = cursor.fetchone()[0] + 1
            print(id)
            cursor.execute("insert into metadata value(%d,'dir',%s,1);" % (id, "'"+l[0]+"'"))
        else:
            return
    con.commit()
    con.close()
# cursor.execute("insert into metadata value(1,'dir','2',1);")
# cursor.execute("insert into directory value(child,'dir','1',1);")
mkdir()