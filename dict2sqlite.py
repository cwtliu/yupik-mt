# *-* encoding: utf-8 *-*

import sys
import sqlite3

conn = sqlite3.connect(sys.argv[3])
c = conn.cursor()

c.execute('create table if not exists nouns (id integer primary key not null, yupik text, english text)')

with open(sys.argv[1], 'r') as f_ypk:
    with open(sys.argv[2], 'r') as f_en:
        lines_ypk = f_ypk.readlines()
        lines_en = f_en.readlines()

assert len(lines_ypk) == len(lines_en)
for i in range(len(lines_ypk)):
    c.execute("insert into nouns values (null, '%s', '%s')" % (lines_ypk[i].strip(), lines_en[i].strip()))


conn.commit()
conn.close()
