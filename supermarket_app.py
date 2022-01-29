from supermarket import *
import time

print("""********************************************
        SUPERMARKET ÜRÜN DÜZENLEME PROGRAMI
        1-ÜRÜNLERİ GÖSTER
        2-ÜRÜN SORGULA
        3-ÜRÜN EKLE
        4-ÜRÜN SİL
        5-ÜRÜNE ZAM YAP
        6-ÜRÜNE İNDİRİM YAP
        7-ÜRÜN ADEDİNİ DEĞİŞTİR
        Programdan çıkmak için 'q' a basınız
        **********************************************
        """)
product = DataBase()
while True:
    operation = input("İşlem seçiniz :").strip()
    if operation == "q":
        print("Program Sonlanıyor..")
        time.sleep(2)
        print("Program sonlandı!!")
        break
    elif operation == "1":
        print("Ürünler sorgulanıyor..")#ERENOMAD
        time.sleep(2)
        print("Ürünler Listeleniyor..\n")
        product.showProducts()

    elif operation == "2":
        name = input("Sorgulamak istedğiniz ürünü giriniz :").lower().strip()#ERENOMAD
        print("Ürün sorgulanıyor...")
        time.sleep(2)
        product.queryProduct(name)#ERENOMAD
    elif operation == "3":

        how_data = input("Kaç tane ürün ekleyeceksiniz ?:").strip()
        while how_data.isalpha():
            print("Lütfen rakam giriniz!!")
            how_data = input("Kaç tane ürün ekleyeceksiniz ?:").strip()
        for i in range(int(how_data)):
            name = input("İsim :").lower()
            brand = input("Mar             ka :")
            weight = input("Ağırlık(kg) :")

            while weight.isalpha():
                print("Lütfen Rakamla Giriniz!")#ERENOMAD
                weight = input("Ağırlık(kg) :")
            variety = input("Ürün çeşidi :")
            price = input("Fiyat :")
            while price.isalpha():
                print("Lütfen Rakamla Giriniz!")
                price = input("Fiyat :")

            number = input("Ürün Kaç Adet:")
            while number.isalpha():
                print("Lütfen Rakamla Giriniz!")
                number = input("Ürün Kaç Adet:")

            newProduct = Product(name, brand, weight, variety, price, number)#ERENOMAD
            print("Ürün Ekleniyor...")
            time.sleep(2)
            product.addProduct(newProduct)
            print("Ürün Eklendi!!")
    elif operation == "4":
        name = input("Silmek istediğiniz ürün adını giriniz :")
        print("Ürün aranıyor..")
        time.sleep(2)
        try:
            print(f"{name} adlı ürün siliniyor")
            time.sleep(1)
            product.deleteProduct(name)#ERENOMAD
            print(f"{name} adlı ürün başarı ile silindi!!")
        except:
            print(f"{name} adlı bir ürün bulunmamaktadır..")
    elif operation == "5":
        name = input("Zam yapacağınız ürünün adı ? :")
        print("Ürün aranıyor..")
        time.sleep(2)
        product.priceRaise(name)
    elif operation == "6":
        name = input("İndirim yapacağınız ürünün adı ? :")
        print("Ürün aranıyor..")
        time.sleep(2)
        product.priceDiscount(name)
    elif operation == "7":
        name = input("Ürün sayısını değiştirmek istediğiniz ürün adını giriniz :").lower().strip()
        print("Ürün aranıyor..")
        time.sleep(2)#ERENOMAD
        product.changeQuantity(name)
    else:
        print("Lütfen numaralı işlemlerden birini seçiniz")
