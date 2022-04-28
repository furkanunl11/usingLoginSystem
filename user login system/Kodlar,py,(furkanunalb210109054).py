buyukHarfler = "ABCDEFGHIİJKLMNOÖPRSŞTUÜVYZ"
kucukHarfler = "abcdefghıijklmnoöprsştuüvyz"
rakamlar = "0123456789"
ozelKarakterler = "?.%&_-"
print("""
------------KULLANICI GIRIS OTOMASYONU-------------
------------------FURKAN ÜNAL----------------------
------------------B210109054-----------------------
------------------20.04.2022------------------------
""")
kontrol = False
kontrol2 = False

while not kontrol:
    
    kullaniciAdi = input("---Kullanici adinizi giriniz.---\n= ")
    karakterSayisi = len(kullaniciAdi)

    if karakterSayisi < 17:
        x = 0
        for a in kullaniciAdi:
            if a in buyukHarfler:
                    x = x + 1
        if x > 0: ##1 den fazla büyük karakter olmasi için.
            print("Kullanici adi Buyuk karakter bakimindan uygun.\n")
            
        else:
            print("!!!Lutfen Kullanici adinizda buyuk karakter kullaniniz!!!\n")
    
            

        y = 0

        for b in kullaniciAdi:
            if b in kucukHarfler:
                y =  y + 1
        if y > 0:
            print("Kullanici adi Kucuk karakter bakimindan uygun.\n")
            
            
        else:
            print("!!!Lutfen Kullanici adinizda kucuk karakter kullaniniz.!!!\n")
            
        
        z = 0
        for c in kullaniciAdi:
            if c in rakamlar:
                z =  z + 1
        if z > 0:
            print("Kullanici adi Rakam bakimindan uygun.\n")
            
            
        else:
            print("!!!Lutfen Kullanici adinizda rakam kullaniniz.!!!\n")
        
        if x > 0 and y > 0 and z > 0:
            kontrol = True
        else:
            pass
        
        
                

    else:
        print("Kullanici adi 16 karakterden fazla olamaz.")
        
        
        

    
while not kontrol2:
    password = input("---Sifre giriniz---\n= ")
    karakterSayisi2 = len(password)


    if karakterSayisi2 < 25 and karakterSayisi2 > 8:
        t = 0
        for d in password:
            if d in buyukHarfler:
                t = t + 1
        if t >0:
            print("Sifre buyuk karakter bakimindan uygun.")
            
        else:
            print("!!!Lutfen sifrenizde buyuk karakter kullaniniz.")

        u = 0
        for e in password:
            if e in kucukHarfler:
                u = u + 1
        if u > 0:
            print("Sifre kucuk karakter bakimindan uygun.")
            
        else:
            print("!!!Lutfen sifrenizde kucuk karakter kullaniniz.")
        
        p = 0

        for w in password:
            if w in rakamlar:
                p = p +1
        if p > 0:
            print("Sifre rakam bakimindan uygun.")
            
        else:
            print("!!!Lutfen sifrenizde rakam kullaniniz.!!!")

        l = 0

        for q in password:
            if q in ozelKarakterler:
                l = l + 1
        if l > 0:
            print("Sifre ozel karakter bakimindan uygun.\n")
            
        else:
            print("!!!Lutfen sifrenizde ozel karakter kullaniniz.!!!")

        if t > 0 and u > 0 and p > 0 and l > 0:
            kontrol2 = True
        else:
            pass

    else:
        print("Lutfen sifrenizi en az 8 en fazla 24 karakter olacak bicimde giriniz.")


kontrol3 = False
kontrol4 = False
kontrol5 = False

while not kontrol3:
    girisK = input("Lutfen giris yapmak icin kullanici adinizi giriniz.\n")

    if girisK == kullaniciAdi:
        print("Kullanici adi dogru.\n")
        kontrol3 = True
    else:
        print("Kullanici adi yanlis. Tekrar deneyiniz.")

while not kontrol4:

    girisP = input("Lutfen giris yapmak icin sifrenizi giriniz.\n")

    if girisP == password:
        print("\nTEBRİKLER! kullanici adi ve sifre dogru.\nBaşarıyla giriş yaptınız...")
        print("Birazdan Hesap makinesi aktarılıyor...\n")
        kontrol4 = True
    else:
        print("sifre yanlis. Tekrar deneyiniz.")

while not kontrol5:
    girdi=input("Lütfen sonucunu bulmak istediğiniz matematiksel işlemi yazın. + - * / matematiksel işaretlerini kullanabilirsiniz.\n")

    sonuc=eval(girdi)

    print("Verdiğiniz matematiksel işlemin sonucu:", sonuc)
    

    secim = input("Hesaplama islemlerine devam etmek istiyor musunuz? (e/h)\n")


    if secim == 'h':
        print("Cikis yapiliyor...")
        kontrol5 = True
        
        




    












    
        





    







    

    
        
    
        








