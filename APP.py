import pickle, os, time
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

j = 0
if not os.path.isfile('urunbilgisi.dat'):
    bilgi = [[0, 1]]
    bilgi[0][0] = 'Aldemir Ürün Sistemi'
    bilgi[0][1] = 'v0.02'
    dosya = open('urunbilgisi.dat', 'wb')
    pickle.dump(bilgi, dosya)
    dosya.close()
else:
    while True:
        dosya = open('urunbilgisi.dat', 'rb+')
        bilgi = pickle.load(dosya)
        dosya.close()
        for i in range(len(bilgi)- 1):
            if len(bilgi) <= 1:
                print('Ürün bulunamadı')
            elif i <= 25:
                print("\n  " + bilgi[i + 1][0], bilgi[i + 1][1])
        print("\nHangi işlemi yapmak istersiniz?")
        print("Ürün Ekleme (1)")
        print("Ürün Silme (2)")
        print("Ad Değiştirme (3)")
        print("Fiyat Değiştirme (4)")
        print("Ürün Bulma (5)")
        print("Çıkış (0)")
        cevap = input()
        if cevap.lower() == 'ürün ekleme' or cevap.lower() == '1':
            dosya = open('urunbilgisi.dat', 'rb+')
            urun_adi = input('Ürünün adını giriniz: ')
            urun_fiyati = input('Ürünün fiyatını giriniz: ')
            bilgi.append([urun_adi, urun_fiyati])
            pickle.dump(bilgi, dosya)
            dosya.close()
        elif cevap.lower() == 'ürün silme' or cevap.lower() == '2':
            dosya = open('urunbilgisi.dat', 'rb+')
            urun_adi = input('Ürünün adını giriniz: ')
            for i in range(len(bilgi)):
                if urun_adi == bilgi[i][0]:
                    bilgi.remove(bilgi[i])
            pickle.dump(bilgi, dosya)
            dosya.close()
        elif cevap.lower() == 'ad değiştirme' or cevap.lower() == '3':
            dosya = open('urunbilgisi.dat', 'rb+')
            urun_adi = input('Ürünün adını giriniz: ')
            urun_adi_2 = input('Ürünün yeni adını giriniz: ')
            for i in range(len(bilgi)):
                if urun_adi == bilgi[i][0]:
                    bilgi[i][0] = urun_adi_2 
            pickle.dump(bilgi, dosya)
            dosya.close()
        elif cevap.lower() == 'fiyat değiştirme' or cevap.lower() == '4':
            dosya = open('urunbilgisi.dat', 'rb+')
            urun_adi = input('Ürünün adını giriniz: ')
            urun_fiyati_2 = input('Ürünün yeni fiyatını giriniz: ')
            for i in range(len(bilgi)):
                if urun_adi == bilgi[i][0]:
                    bilgi[i][1] = urun_fiyati_2
            pickle.dump(bilgi, dosya)
            dosya.close()
        elif cevap.lower() == 'ürün bulma' or cevap.lower() == '5':
            dosya = open('urunbilgisi.dat', 'rb+')
            urun_adi = input('Ürünün adını giriniz :')
            for i in range(len(bilgi)):
                if bilgi[i][0] == urun_adi:
                    print(bilgi[i][0], bilgi[i][1], "lira")
                    time.sleep(5)
            dosya.close()
        elif cevap.lower() == 'çıkış' or '0':
            exit()
        clear()
        
            
            
            
            
