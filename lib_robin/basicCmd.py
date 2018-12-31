""" Simple functions for Robin """

def gunKontrol(gun):
    gunler = ["pazar","pazartesi","salı","çarşamba","perşembe","cuma","cumartesi"]
    gun = gun.lower()
    if gun in gunler: return gunler.index(gun)
    else: return -1

def saatKontrol(saat):
    nokta=0
    ySaat = []
    while len(ySaat)<2:
        if(nokta==0):   ySaat = saat.split(".");nokta=1
        elif(nokta==1): ySaat = saat.split(":");nokta=2
        elif(nokta==2): ySaat = saat.split(",");nokta=2
    sa, dk = ySaat
    sa = int(sa)
    dk = int(dk)
    if not(sa<0 or sa>23) and not(dk<0 or dk>59):
        return "{}:{}".format(sa,dk)
    else:
        return 0

def takePicture():
    from os import system, getcwd
    from datetime import datetime
    from urllib.request import urlopen
    konum = getcwd()+"/"
    tarih = datetime.now()
    kayit = str(tarih.day)+str(tarih.month)+str(tarih.year)+"_"+str(tarih.hour)+str(tarih.minute)

    system("fswebcam -r 1280x720 --no-banner webcam/{}.jpg".format(kayit))
    url = urlopen("file://"+konum+"webcam/"+kayit+".jpg")
    return url