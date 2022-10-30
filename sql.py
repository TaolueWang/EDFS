import pymysql
con = pymysql.connect(user='wtl',password='123')
cursor = con.cursor();
cursor.execute("USE EDFS")
cursor.execute("drop table metadata")
cursor.execute("create table if not exists metadata (id int primary key,type varchar(255),name varchar(255),partition_id int)")
# cursor.execute("insert into metadata value(1,'dir','1',1);")
# cursor.execute("insert into metadata value(2,'dir','1',1);")
# cursor.execute("insert into metadata value(1,'dir','2',1);")
# cursor.execute("drop table directory")
cursor.execute("create table if not exists directory (child int,parent int,"
               "foreign key(child) references metadata(id),"
               "foreign key(parent) references metadata(id))")
con.commit()
# cursor.execute("insert into metadata value(2,'dir','2',1)")
# cursor.execute("insert into metadata value(1,'dir','3',1)")
# cursor.execute()