import re
import sqlite3
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)

string = '项目名称 MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
cursor.execute('create table user (id int(10) primary key,name varchar(20))')
cursor.close()
conn.close()