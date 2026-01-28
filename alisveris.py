sepet=["elma","armut","muz","pırasa","ıspanak"]
while True:

 a=1
 b=2
 c=3
 d=4
 e=5
 f=6
 print("1-Ürün Ekle")
 print("2-Ürün Sil")
 print("3-Sepette Üründen Kaç Tane Var")
 print("4-Sepeti Göster")
 print("5-Sepette Kaç Ürün Var")
 print("6-Çıkış")

 secim=int(input("Lütfen Yapacağınız İşlemin Numarasını Girin "))

 if secim==a:
    urun=input("Eklenecek Ürünü Yazınız ")
    sepet.append(urun)
    print(sepet)

 if secim==b:
    sil = input("Silmek İstediğiniz Ürünü Yazınız: ")

    if sil in sepet:
        sepet.remove(sil)
        print("Ürün Silindi")
    else:
        print("Ürün Sepette Yok")
        print(sepet)

 if secim==c:
    say=input("Saymak İstediğiniz Ürünü Yazınız: ")
    print(sepet.count(say))

 if secim==d:
    print("Sepet Gösteriliyor")
    print(sepet)

 if secim==e:
    print("Sepet Sayılıyor")
    print(len(sepet))

 if secim==f:
    print("Uygulamadan Çıkılıyor")
    break
