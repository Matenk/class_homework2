class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Этаж номер {self.numberOfFloors}')


floors_ = House()
floors_.setNewNumberOfFloors(4)

# Создал класс House и объект floors_, затем внутри класса создал 2 метода. Первый по сути счетчик этажей изначально
# равный 0 (точнее атрибут внутри метода имеет значение 0), второй метод должен изменять значение атрибута
# первого метода на то число которое мы передаем на место параметра floors который зададим во втором методе,
# потому приравниваем self.numberOfFloors = floors, а ниже выводим Номер этажа обращаясь к атрибуту из первого метода
# (self.numberOfFloors = floors)
# в конце пишем floors_.setNewNumberOfFloors(4), как бы обращаясь к методу def setNewNumberOfFloors(self, floors): и
# подставляем аргумент 4, который встает на место параметра floors во втором методе, оттуда передается в тело функции
# и приравнивается к self.numberOfFloors, из-за чего 0 этаж становится 4ым и выводится принтом 