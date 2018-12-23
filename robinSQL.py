import mysql.connector # MYSQL BAĞLANTI KÜTÜPHANESİ
from random import choice # RASTGELE IŞLEM KÜTÜPHANESI İÇİNDEN choice()

# Veritabanı bağlantı bilgileri
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ken",
    database="robin")

# Imleç
curs = db.cursor()

# Sorgu ekleme
def add_query(nq="",nc="",na=""):
    # PARAMETRE BOŞ GEÇERSE SOR
    if(nq=="" or nc=="" or na==""):
        nq = input("Please input the query you want to add: ")
        nc = input("Please input the Python command or command file you want to add\n(if command file doesn't exist, leave blank!)")
        na = input("Please input the answer of this function: ")
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
            return response[3]
    except:
        return "Anlayamadım!"

def settings(name="", author=""):
    pass