from random import choice # RASTGELE IŞLEM KÜTÜPHANESI İÇİNDEN choice()
import mysql.connector # MYSQL BAĞLANTI KÜTÜPHANESİ
from lib_robin.basicCmd import *

# Veritabanı bağlantı bilgileri
vtHost = "localhost"
vtUser = "root"
vtPass = "ken"
vtData = "robin"
db = mysql.connector.connect(
    host=vtHost,
    user=vtUser,
    passwd=vtPass,
    database=vtData)

# Imleç
curs = db.cursor()

# Plan ekleme
def addPlan(gun, saat, msg, durum):
    if(gunKontrol(gun)!=-1 and saatKontrol(saat)!=0 and msg!="" and (durum!="k" or durum!="g")):
        sql  = "INSERT INTO plan (gun, saat, msg, durum) VALUES (%s, %s, %s, %s)"
        val  = (gunKontrol(gun), saatKontrol(saat), msg, durum.lower())
        curs.execute(sql, val)
        db.commit()
        return "Plan başarıyla eklendi!"
    else:
        return "Bir hata oluştu!"

# Plan silme
def delPlan(mssg):
    sql = "Delete from plan where msg='%s'"%(mssg)
    curs.execute(sql)
    db.commit()
    return 1

# Sorgu ekleme
def add_query(nq,nc,na):
    # QUERY SÜTUNU ARAMA KOLAYLIĞI İÇİN KOMPLE KÜÇÜK HARF
    nq = nq.lower()
    sql = "INSERT INTO querys (query, shell, answer) VALUES (%s, %s, %s)"
    
    val = (nq,nc,na)
    curs.execute(sql, val)
    db.commit()

def reply(query):
    query = query.lower()
    curs.execute("SELECT * FROM querys where query='"+str(query)+"'")
    # (id, query, shell, answer)
    try:
        response = choice(curs.fetchall())

        if(response[2]=="1"): #AYAR BILGISI
            pass # GEÇ
        elif(response[2]!="0"):
            # IŞLEMLER
            pass
        else:
            return [response[3], False]
    except:
        donen = "Anlamadım.\nAz önce yazdığına nasıl karşılık vermeliyim?".format(query)
        return [donen, True]

def settings(name="", author=""):
    pass