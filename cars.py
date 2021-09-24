import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def __str__(self):
        return f'CarBase'

    __repr__ = __str__

    def get_photo_file_ext(self):
        """Получить расширение файла изображения"""
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    """Легковой автомобиль"""

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'


class Truck(CarBase):
    """Грузовой автомобиль"""

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)

        self.body_length, self.body_width, self.body_height = body_whl.split('x')
        try:
            self.body_length = float(self.body_length)
            self.body_width = float(self.body_width)
            self.body_height = float(self.body_height)
        except ValueError:
            self.body_length, self.body_width, self.body_height = 0, 0, 0

    def get_body_volume(self):
        """Возвращает объем кузова автомобиля"""
        return self.body_length*self.body_width*self.body_height


class SpecMachine(CarBase):
    """Спец техника"""

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    return car_list


def print_csv(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)

c = Truck('brand', 'photo.png', '200', '25kkx2x2')
print(c.body_length)
print(type(c.body_length))
print(c.get_body_volume())
print(c)