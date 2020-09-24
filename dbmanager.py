from PyQt5.QtCore import *
import pymysql
from pymysql.cursors import *
import os


def checkconfig(name):
    if not os.path.exists(name):
        f = open(name, 'w')
        f.write("""[DB]
Host=localhost
User=root
Pass=root
DBName=nir""")
        f.close()


def openDatabase(dbini):
    ini = QSettings(dbini, QSettings.IniFormat)
    ini.setIniCodec("utf-8")
    ini.beginGroup("DB")
    dbname = ini.value("DBName")
    dbuser = ini.value("User")
    dbpass = ini.value("Pass")
    dbhost = ini.value("Host")
    ini.endGroup()

    try:
        con = pymysql.connect(dbhost, dbuser , dbpass, dbname, cursorclass=DictCursor)
        return con
    except BaseException:
        print("cannot connect to database")
        return None

def countNPROJ(con):
    with con.cursor() as cur:
        cur.execute("SELECT CODPROG, count(*) cnt FROM ntp_proj GROUP by CODPROG order by Codprog")
        ntp_prog_cnt = cur.fetchall()

        cur.execute("SET SQL_SAFE_UPDATES = 0")
        for row in ntp_prog_cnt:
            q = "UPDATE ntp_prog SET nproj = {} WHERE TRIM(codprog) = {}".format(row['cnt'], row['CODPROG'])
            cur.execute(q)
        con.commit()

def SumPFinInProg(con):
    with con.cursor() as cur:
        cur.execute("select codprog ,sum(PFIN) pfin,sum(PFIN1) pfin1,sum(PFIN2) pfin2,sum(PFIN3) pfin3,sum(PFIN4) pfin4 from nir.ntp_proj Group by ntp_proj.codprog")
        ntp_prog_pfin_sum = cur.fetchall()

        cur.execute("SET SQL_SAFE_UPDATES = 0")
        for row in ntp_prog_pfin_sum:
            q = "UPDATE ntp_prog SET pfin = {},pfin1 = {},pfin2 = {},pfin3 = {},pfin4 = {} WHERE TRIM(codprog) = {}".format(row['pfin'],row['pfin1'],row['pfin2'],row['pfin3'],row['pfin4'], row['codprog'])
            cur.execute(q)
        con.commit()

def GetTableNir(con):
    with con.cursor() as cur:
        cur.execute("SELECT pg.PROG, pj.F,  pj.isp, pj.PFIN,pj.PFIN1,pg.PFIN2,pg.PFIN3,pg.PFIN4, pg.FFIN,pg.FFIN1,pg.FFIN2,pg.FFIN3,pg.FFIN4,pj.SROK_N, pj.SROK_K,pj.RUK, pj.GRNTI, pj.CODTYPE, pj.NIR FROM nir.ntp_proj pj, nir.ntp_prog pg where pj.CODPROG = pg.CODPROG;")
        table = cur.fetchall()
        return table

def GetProgTable(con):
    with con.cursor() as cur:
        cur.execute("SELECT CODPROG, PROG, NPROJ, PFIN,PFIN1,PFIN2,PFIN3,PFIN4, FFIN,FFIN1,FFIN2,FFIN3,FFIN4 FROM nir.ntp_prog ")
        table = cur.fetchall()
        return table

def GetVuzTable(con):
    with con.cursor() as cur:
        cur.execute("SELECT * FROM nir.vuz ")
        table = cur.fetchall()
        return table

if __name__ == '__main__':

    db = openDatabase("config.ini")

    print(db)

