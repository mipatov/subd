import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing

with closing(pymysql.connect('localhost', 'root','root', 'nir',cursorclass=DictCursor)) as con:
    with con.cursor() as cur:
        pass
        # query = "SELECT CODPROG, count(*) cnt FROM ntp_proj GROUP by CODPROG order by Codprog"
    con.commit()

def CountNtpInProg(con):
    with con.cursor() as cur:
        cur.execute("SELECT CODPROG, count(*) cnt FROM ntp_proj GROUP by CODPROG order by Codprog")
        ntp_prog_cnt = cur.fetchall()

        cur.execute("SET SQL_SAFE_UPDATES = 0")
        for row in ntp_prog_cnt:
            q = "UPDATE ntp_prog SET nproj = {} WHERE TRIM(codprog) = {}".format(row['cnt'], row['CODPROG'])
            cur.execute(q)
        con.commit()