from PyQt5.QtCore import *
import pymysql
from pymysql.cursors import *
import os


# Update ntp_proj set PFIN4 = PFIN - 3*Round(PFIN/4);

class dbc():
    dbcon = None

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
        print("database '" +dbname+"' is open OK")
        dbc.dbcon = con
        return con
    except BaseException:
        print("cannot connect to database")
        return None

def countNPROJ():
    with dbc.dbcon.cursor() as cur:
        cur.execute("SELECT CODPROG, count(*) cnt FROM ntp_proj GROUP by CODPROG order by Codprog")
        ntp_prog_cnt = cur.fetchall()

        cur.execute("SET SQL_SAFE_UPDATES = 0")
        for row in ntp_prog_cnt:
            q = "UPDATE ntp_prog SET nproj = {} WHERE TRIM(codprog) = {}".format(row['cnt'], row['CODPROG'])
            cur.execute(q)
        dbc.dbcon.commit()

def SumPFinInProg():
    with dbc.dbcon.cursor() as cur:
        cur.execute("select codprog ,sum(PFIN) pfin,sum(PFIN1) pfin1,sum(PFIN2) pfin2,sum(PFIN3) pfin3,sum(PFIN4) pfin4 from nir.ntp_proj Group by ntp_proj.codprog")
        ntp_prog_pfin_sum = cur.fetchall()

        cur.execute("SET SQL_SAFE_UPDATES = 0")
        for row in ntp_prog_pfin_sum:
            q = "UPDATE ntp_prog SET pfin = {},pfin1 = {},pfin2 = {},pfin3 = {},pfin4 = {} WHERE TRIM(codprog) = {}".format(row['pfin'],row['pfin1'],row['pfin2'],row['pfin3'],row['pfin4'], row['codprog'])
            cur.execute(q)
        dbc.dbcon.commit()


def GetTableNir(sort = 0, desc = False):
    sorttuple = ('order by pj.Codprog, pj.F',
                 'order by pj.isp',
                 'order by pj.Pfin')
    descsorttuple = ('order by pj.Codprog desc, pj.F desc',
                 'order by pj.isp desc',
                 'order by pj.Pfin desc')
    if desc :
        sortexpr = descsorttuple[sort]
    else:
        sortexpr = sorttuple[sort]
    with dbc.dbcon.cursor() as cur:
        cur.execute("SELECT pg.PROG, pj.F,  pj.isp, pj.PFIN, pg.FFIN,pj.SROK_N, pj.SROK_K,pj.RUK, pj.GRNTI, pj.CODTYPE,pj.PFIN1,pj.PFIN2,pj.PFIN3,pj.PFIN4,pg.FFIN1,pg.FFIN2,pg.FFIN3,pg.FFIN4, pj.NIR FROM nir.ntp_proj pj, nir.ntp_prog pg where pj.CODPROG = pg.CODPROG "+sortexpr)
        table = cur.fetchall()
        return table

def GetProgTable():
    with dbc.dbcon.cursor() as cur:
        cur.execute("SELECT CODPROG, PROG, NPROJ, PFIN,PFIN1,PFIN2,PFIN3,PFIN4, FFIN,FFIN1,FFIN2,FFIN3,FFIN4 FROM nir.ntp_prog ")
        table = cur.fetchall()

        cur.execute(f"select codprog from nir.ntp_prog where prog = 'Экраноплан'")
        print(cur.fetchone()["codprog"])
        # cprog =
        return table

def GetVuzTable():
    with dbc.dbcon.cursor() as cur:
        cur.execute("SELECT * FROM nir.vuz ")
        table = cur.fetchall()
        return table

def GetProgTuple():
    with dbc.dbcon.cursor() as cur:
        cur.execute("SELECT PROG FROM nir.ntp_prog ")
        progtup = ((row["PROG"]) for row in cur.fetchall())
        return tuple(progtup)

def GetMaxProjInProg(prog):
    with dbc.dbcon.cursor() as cur:
        cur.execute(f"SELECT max(pj.F) F FROM nir.ntp_prog pg, nir.ntp_proj pj where pg.prog = '{prog}' and pg.codprog = pj.codprog")
        i = cur.fetchone()["F"]
        if not i:
            i = 0
        return i

def GetVuzTuple():
    with dbc.dbcon.cursor() as cur:
        cur.execute("SELECT z2 FROM nir.vuz ")
        vuztup = ((row["z2"]) for row in cur.fetchall())
        return tuple(vuztup)

def CheckProjNum(prog,num):
    with dbc.dbcon.cursor() as cur:
        cur.execute(f"SELECT pj.F FROM nir.ntp_prog pg, nir.ntp_proj pj where pg.prog = '{prog}' and pg.codprog = pj.codprog")
        nums = tuple(int(row["F"]) for row in cur.fetchall())
        return not (num in nums)

def AddRecord(prog,f,nir,isp,srn,srk,ruk,ruk2,grnti,ctype,pfin):
    with dbc.dbcon.cursor() as cur:
        cur.execute(f"select codprog from nir.ntp_prog where prog = '{prog}'")
        row  = cur.fetchone()
        cprog = row["codprog"]
        cur.execute(f"select codvuz from nir.vuz where z2 = '{isp}'")
        cisp = cur.fetchone()["codvuz"].strip()
        print(cisp)
        pfin = int(pfin)
        pfin123 = round(pfin/4)
        pfin4 = pfin - 3 * round(pfin / 4)

        cur.execute(f"""INSERT INTO nir.ntp_proj (CODPROG,F,NIR,ISP,CODISP,SROK_N,SROK_K,RUK,RUK2,GRNTI,CODTYPE,PFIN,PFIN1,PFIN2,PFIN3,PFIN4,FFIN,FFIN1,FFIN2,FFIN3,FFIN4)
VALUES('{cprog}','{str(f).rjust(4,"0")}','{nir}','{isp}','{cisp}','{srn}','{srk}','{ruk}','{ruk2}','{grnti}','{ctype}',{pfin},{pfin123},{pfin123},{pfin123},{pfin4},0,0,0,0,0)""")

        dbc.dbcon.commit()

def EditRecord(prog,f,nir,isp,srn,srk,ruk,ruk2,grnti,ctype,pfin):
    with dbc.dbcon.cursor() as cur:
        cur.execute(f"select codprog from nir.ntp_prog where prog = '{prog}'")
        row  = cur.fetchone()
        cprog = row["codprog"]
        cur.execute(f"select codvuz from nir.vuz where z2 = '{isp}'")
        cisp = cur.fetchone()["codvuz"].strip()
        print(cisp)
        pfin = int(pfin)
        print(str(pfin))
        pfin123 = round(pfin/4)
        pfin4 = pfin - 3 * round(pfin / 4)

        cur.execute(f"""Replace INTO nir.ntp_proj (CODPROG,F,NIR,ISP,CODISP,SROK_N,SROK_K,RUK,RUK2,GRNTI,CODTYPE,PFIN,PFIN1,PFIN2,PFIN3,PFIN4,FFIN,FFIN1,FFIN2,FFIN3,FFIN4)
        VALUES('{cprog}','{str(f).rjust(4, "0")}','{nir}','{isp}','{cisp}','{srn}','{srk}','{ruk}','{ruk2}','{grnti}','{ctype}',{pfin},{pfin123},{pfin123},{pfin123},{pfin4},0,0,0,0,0)""")

#         cur.execute(f"""Update nir.ntp_proj set CODPROG = '{cprog}',F = '{str(f).rjust(4,"0")}',NIR = '{nir}',ISP= '{isp}',CODISP= '{cisp}',SROK_N = '{srn}',SROK_K = '{srk}',
# RUK='{ruk}',RUK2='{ruk2}',GRNTI='{grnti}',CODTYPE='{ctype}',PFIN={pfin},PFIN1={pfin123},PFIN2={pfin123},PFIN3={pfin123},PFIN4= {pfin4}""")

        dbc.dbcon.commit()

def RemoveRecord(prog,f):
    with dbc.dbcon.cursor() as cur:
        # cur.execute(f"select codprog from nir.ntp_prog where prog = '{prog}'")
        # row  = cur.fetchone()
        # cprog = row["codprog"]
        cur.execute(f"delete from ntp_proj using ntp_proj, ntp_prog  where ntp_prog.prog = '{prog}' and ntp_prog.codprog = ntp_proj.codprog and ntp_proj.f = '{f}'")
        dbc.dbcon.commit()

def GetRecord(prog,f):
    with dbc.dbcon.cursor() as cur:
        cur.execute(f"select nj.CODPROG,nj.F,nj.NIR,nj.ISP,nj.CODISP,nj.SROK_N,nj.SROK_K,nj.RUK,nj.RUK2,nj.GRNTI,nj.CODTYPE,nj.PFIN from  nir.ntp_proj nj,nir.ntp_prog ng where ng.prog = '{prog}' and ng.codprog = nj.codprog and nj.f = '{f}'")
        return cur.fetchone()


if __name__ == '__main__':

    db = openDatabase("config.ini")

    print(db)

