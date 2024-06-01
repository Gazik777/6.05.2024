from model import Footwear
import view

def add():
    f = Footwear()
    f.type = input("Тип обуви: ")
    f.color = input("Цвет обуви: ")
    f.size = input("Размер обуви: ")
    f.price = input("Цена обуви: ")
    f.manufacturer = input("Производитель обуви: ")
    view.info(f)

if __name__ == "__main__":
    add()

def info(f):
    print("Обувь: " + f.type + " " + f.color + " " + f.size + " " + f.price + " " + f.manufacturer)

class Footwear:
    def __init__(self):
        self.type = "Тип обуви: "
        self.color = "Цвет обуви: "
        self.size = "Размер обуви: "
        self.price = "Цена обуви: "
        self.manufacturer = "Производитель обуви: "