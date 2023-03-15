class Product:
    def __init__(self, i, n, p, c):
        self.id = i
        self.name = n
        self.price = p
        self.count = c

    @staticmethod
    def add():
        code = input("enter code: ")
        name = input("enter name: ")
        price = input("enter price: ")
        count = input("enter count: ")
        new_product = Product(code, name, price, count)
        PRODUCTS.append(new_product)
        print("Add successful\n")

    def edit(self):
        pass

    @staticmethod
    def search():
        pass

    def remove(self):
        pass

    def show(self):
        pass

    @staticmethod
    def show_list():
        pass

    def buy(self):
        pass




class Database:
    def read():
        f = open("database.txt", "r")

        for line in f:
            result = line.split(",")
            my_obj = Product(result[0], result[1], result[2], result[3])
            PRODUCT.append(my_obj)

            f.close()


    def write():
        f = open("vscode/database.txt", "w")

        ...

        f.close()

PRODUCT = []
db = Database()


def show_menu():
    print("1.Add")
    print("2.Edit")
    print("3.Remove")
    print("4.Search")
    print("5.Show List")
    print("6.Buy")
    print("7.convert product to qr")
    print("8.exit")

print("Welcome to store")
print("Loading...")
db.read()
print("Data loaded")

while True:
    print("-"*50)
    show_menu()
    choice = int(input("\nenter your choice: "))

    if choice == 1:
        Product.add()
    elif choice == 2:
        id = int(input("enter product id: "))
        for product in PRODUCT:
            if product.id == id:
                product.edit()

    elif choice == 3:
        id = int(input("enter product id: "))
        for product in PRODUCT:
            if product.id == id:
                product.remove()

    elif choice == 4:
        Product.search()
    elif choice == 5:
        Product.show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        convert_qr()
    elif choice == 8:
        db.write()
        print("\nHave Nice Time")
        exit()
