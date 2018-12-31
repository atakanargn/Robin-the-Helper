import telepot
from telepot.loop import MessageLoop
from time import sleep
from lib_robin.robin import *
from datetime import datetime

global gunler, ogren, onceki
ogren  = False
onceki = ""
gunler = ["pazar","pazartesi","salı","çarşamba","perşembe","cuma","cumartesi"]
BOT_TOKEN = "650318838:AAEjQU1Coh_yip6J0F3J0iC9qOE_z3C5F1g"

bot = telepot.Bot(BOT_TOKEN)

def handle(msg):
        global ogren, onceki

        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
                sorgu = msg["text"]
                komutAl=False
                if(sorgu[:0-(len(sorgu)-1)]=="/"):
                    komut = sorgu.split()
                    print(komut)
                    komutAl=True
                
                if(komutAl==False):
                    if(ogren==True):
                        minnet = ["Bundan sonra böyle cevap vereceğim :)",
                                  "Yeni şeyler öğrenmek güzel.",
                                  "Bana öğrettiğin için teşekkürler!",
                                  "Bana 1 harf öğretenin, 40 yıl asistanı olurum :D"]
                        add_query(onceki,"0",sorgu)
                        bot.sendMessage(chat_id,choice(minnet))
                        ogren = False
                    else:
                        mesaj, ogren = reply(sorgu)
                        onceki = sorgu
                        bot.sendMessage(chat_id,mesaj)

                if(komutAl):
                    cmd   = komut[0]
                    print(cmd)
                    # KOMUTLAR
                    if(cmd == "/planla"):
                        if(len(komut)==5):
                            ekle = addPlan(komut[1],komut[2],komut[3],komut[4])
                            bot.sendMessage(chat_id,ekle)
                        else:
                            bot.sendMessage(chat_id,"Eksik parametre girdin.")
                    elif(cmd == "/planlar"):
                        curs.execute("SELECT * FROM plan")
                        planlar = curs.fetchall()
                        for plan in planlar:
                            bot.sendMessage(chat_id, "Plan : {}\nTarih : {} {}".format(plan[2],gunler[int(plan[0])].title(),plan[1]))
                    elif(cmd == "/ogren"):
                        if(len(komut)>=3):
                            cevaplar = komut[2:]
                            na = ""
                            for cevap in cevaplar:
                                na += (cevap + " ")
                            add_query(komut[1],"0",na)
                            bot.sendMessage(chat_id,"Yeni şeyler öğrenmek güzel :)")
                    elif(cmd == "/kamera"):
                        foto = takePicture()
                        print(foto)
                        bot.sendPhoto(chat_id,("kamera.jpg",foto))
                    else:
                        bot.sendMessage(chat_id,"Lütfen geçerli komutlar girin!")
print ('Bot başlatılıyor...')

MessageLoop(bot, handle).run_as_thread()

while True:
    zaman  = datetime.now()
    bugun  = str(zaman.isoweekday())
    dakika = zaman.minute+10
    sa = zaman.hour
    if(dakika >= 60):
        dakika -= 60
        sa   += 1

    saat = "{}:{}".format(sa,dakika)
    curs.execute("SELECT * FROM plan")
    planlar = curs.fetchall()

    for plan in planlar:
        if(bugun == plan[0] and saat == plan[1]):
            bot.sendMessage(466525678, "10 dakika sonra olan *%s* planını unutma!\n\nDetaylar;\nPlan : %s\nTarih : %s %s"%(plan[2],plan[2],gunler[int(plan[0])].title(),plan[1]))
            delPlan(plan[2])
            curs.execute("SELECT * FROM plan")
            planlar = curs.fetchall()
            break
    sleep(1)
    