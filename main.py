import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing
import sys
from PyQt5 import QtWidgets

from TableWindow import *




def CountNtpInProg(con):
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

def GetTableNtp(con):
    with con.cursor() as cur:
        cur.execute("SELECT pg.PROG, pj.F, pj.SROK_N, pj.SROK_K, pj.isp, pj.RUK, pj.PFIN, pj.FFIN,  pj.GRNTI, pj.CODTYPE, pj.NIR FROM nir.ntp_proj pj, nir.ntp_prog pg where pj.CODPROG = pg.CODPROG;")
        table = cur.fetchall()
        return table

def main():
    with closing(pymysql.connect('localhost', 'root', 'root', 'nir', cursorclass=DictCursor)) as con:
        ntpTable = GetTableNtp(con)

    # print(ntpTable[0]["F"])
    app = QtWidgets.QApplication([])
    window = TableWidgetWindow(ntpTable)
    window.show()
    app.exec()



if __name__ == '__main__':
    main()
