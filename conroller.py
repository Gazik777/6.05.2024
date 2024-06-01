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

#второе задание одинаковое