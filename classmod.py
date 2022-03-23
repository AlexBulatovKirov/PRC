
class Mashine():
    # Конструктор
    def __init__(self,marka,max_speed, color='black', capacity=1):
        self.marka = marka
        self.max_speed = max_speed
        self.color = color
        self.capacity = capacity

    def print_info(self):
        print('Марка автомобиля',self.marka)
        print('Максимальная скорость', self.max_speed)
        print('Цвет транспортного средства', self.color)
        print('Вместительность', self.capacity)

    def race(self,enemy):
                if self.max_speed > enemy.max_speed:
                    print('Победил', self.marka)
                else:
                    print('Победил', enemy.marka)


class Bus(Mashine):
    #Конструктор
    def __init__(self,marka,max_speed, color, capacity,price):
        Mashine.__init__(self,marka,max_speed, color, capacity)
        self.price = price

    def print_info(self):
        Mashine.print_info(self)
        print('Цена проезда', self.price)


mycar = Mashine('Kia',200,'white',5)
ourcar = Mashine('Porshe',250,'black')

bus = Bus('ПАЗ', 80,'yellow',100,26)

#mycar.print_info()
#bus.print_info()

print((mycar.max_speed + ourcar.max_speed + bus.max_speed)/3)

#mycar.race(bus)

#mycar.race(ourcar)

#ourcar.print_info()