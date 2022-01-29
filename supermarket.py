import sqlite3


class Product():  # marka                   #adet
    def __init__(self, name, brand, weight, variety, price, number):
        self.name = name
        self.brand = brand
        self.weight = weight
        self.variety = variety
        self.price = price
        self.number = number                    #ERENOMAD

    def __str__(self):
        return f"Ürün ismi    :{self.name}\n" \
               f"Markası      :{self.brand}\n" \
               f"Ürün ağırlığı:{self.weight}kg\n" \
               f"Çeşidi       :{self.variety}\n" \
               f"Ürün fiyatı  :{self.price}TL\n" \
               f"Ürün adedi   :{self.number} tane\n"


class DataBase():
    def __init__(self):
        self.connection = sqlite3.connect("MarketDataBase.db")
        self.cursor = self.connection.cursor()
        self.createLink()

    def createLink(self):
        query = "CREATE TABLE IF NOT EXISTS ürünler (name TEXT,brand TEXT,weight FLOAT,kind TEXT,price FLOAT,number INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def disconnected(self):
        self.connection.close()

    def showProducts(self):
        self.cursor.execute("Select * From ürünler")
        product = self.cursor.fetchall()
        if (len(product) == 0):
            print("Markette hiç ürün bulunmamaktadır..")
        else:
            for i in product:
                product = Product(i[0], i[1], i[2], i[3], i[4], i[5])
                print(product)                      #ERENOMAD

    def queryProduct(self, name):
        self.cursor.execute("Select *From ürünler where name=?", (name,))
        products = self.cursor.fetchall()
        if len(products) == 0:
            print(f"{name} isimli bir ürün bulunmamaktadır.")
        else:
            product = Product(products[0][0], products[0][1], products[0][2], products[0][3], products[0][4],
                              products[0][5])
            print(product)

    def addProduct(self, product):
        self.cursor.execute("Insert into ürünler Values(?,?,?,?,?,?)", (
            product.name, product.brand, product.weight, product.variety, product.price, product.number))
        self.connection.commit()

    def deleteProduct(self, name):
        self.cursor.execute("Delete From ürünler where name = ?", (name,))
        self.connection.commit()

    def priceRaise(self, name):
        self.cursor.execute("Select *From ürünler where name = ?", (name,))
        product = self.cursor.fetchall()
        if len(product) == 0:#ERENOMAD
            print("() isminde bir ürün bulunmamaktadır".format(name))
        else:
            print(f"{name} isimli ürünün fiyatı", product[0][4])
            changes = float(input("Kaç lira zam yapmak istiyorsunuz ? :"))
            product[0][4] = (product[0][4] + changes)
            self.cursor.execute("Update ürünler set price = ? where name = ?", (prices, name))
            self.connection.commit()
            print(f"{name} isimli ürüne zam yapıldı!!\nYeni fiyatı: {product[0][4]}")

    def priceDiscount(self, name):
        self.cursor.execute("Select *From ürünler where name = ?", (name,))
        product = self.cursor.fetchall()
        if len(product) == 0:
            print(f"{name} isimli bir ürün bulunmamaktadır")
        else:
            print(f"{name} adlı ürünün fiyatı", product[0][4])
            changes = float(input("Kaç lira indirim yapmak istiyorsunuz ? :"))
            prices = (product[0][4] - changes)
            self.cursor.execute("Update ürünler set price = ? where name = ?", (prices, name))
            self.connection.commit()
            print(f"{name} isimli ürüne indirim yapıldı!!\nYeni fiyatı: {product[0][4]}")#ERENOMAD

    def changeQuantity(self, name):
        self.cursor.execute("Select *From ürünler where name = ?", (name,))
        product = self.cursor.fetchall()
        if len(product) == 0:
            print(f"{name} isminde bir ürün bulunmamaktadır")
        else:
            signs = input(f"{name} adlı ürünün adedini artırmak için '+' azaltmak için '-' seçiniz:").strip()
            if signs == "+":
                changes = int(input("Ürünün adedini kaç artırmak istiyorsunuz? :"))
                number = product[0][5] + changes
                self.cursor.execute("Update ürünler set number = ? where name = ?", (number, name,))
                self.connection.commit()#ERENOMAD
                print(f"{name} adlı ürünün yeni adedi:{number}")
            elif signs == "-":
                changes = int(input("Ürünün adedini kaç azaltmak istiyorsunuz? :"))
                number = product[0][5] - changes
                self.cursor.execute("Update ürünler set number = ? where name = ?", (number, name,))
                self.connection.commit()
                print(f"{name} adlı ürünün yeni adedi:{number}")
            else:
                print("Yanlış seçim yaptınız")
                return
