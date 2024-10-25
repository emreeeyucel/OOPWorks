# OOP üzerine Yyapmış olduğum çalışmaları içerir.
# Her task ayrı bir çalışmadır.


# region Task 1
# Çevre ve Alan Hesaplaması Yapalım
# Circle adında bir sınıf yaratalım,
# pi = 3.14 --> class attribute,
# radius --> object attribute


class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_perimeter(self):
        return self.pi * self.radius ** 2

    def calculate_area(self):
        return self.pi * self.radius * 2


radius = float(input(f'Radius : '))
c1 = Circle(radius)
print(f'Perimeter : {c1.calculate_perimeter()}\n'
      f'Area : {c1.calculate_area()}')

# endregion





# region Task 2
# Hesaplanan Sonuçların  soonuçlarını, işlem zamanını, makine adını ve ıp bilgisinin Log kayıtlarını tutalım
# Circle adında bir sınıf yaratalım,
# pi = 3.14 --> class attribute,
# radius --> object attribute
# Çevre ve Alan Hesaplaması Yapalım.


from socket import gethostname, gethostbyname
from datetime import datetime
class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_perimeter(self):
        return self.pi * self.radius ** 2

    def calculate_area(self):
        return self.pi * self.radius * 2

    def log(self):
        with open(file='CircleLog.txt',
                  mode='a',
                  encoding='utf-8'
                  ) as file:
            file.write(f'Perimeter : {self.calculate_perimeter()}\n'
                       f'Area : {self.calculate_area()}\n'
                       f'İşlem Zamanı : {datetime.now()}\n'
                       f'Makine Bilgisi : {gethostname()}\n'
                       f'Ip Adres : {gethostbyname(gethostname())}')
radius = float(input('Radius : '))
c1 = Circle(radius)
print(f'Perimeter : {c1.calculate_perimeter()}\n'
      f'Area : {c1.calculate_area()}')
c1.log()

# endregion





# region Task 3
# Departman ve Çalışan Bilgisini içerir Sınıf Yaratalım.
# Department adında bir sınıf yaratalım
# Department_name, employe_count --> class attribute
# name, age --> object attribute
# Çalışanın bilgileri ve kaç çalışan olduğu Bilgisi yazılacak ekrana yazılcak
# Kaç Çalışan olduğu Bilgisi yazılacak
# Departmand sınıfından her instance alındığında çalışan sayısı 1 arttırılsın.

class Departman:
    departman_name = 'Data Analysis'
    employe_count = 0

    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name
        Departman.employe_count += 1

    def get_info(self):
        print(f'ÇALIŞAN BİLGİLERİ\n'
              f'=====================\n'
              f'Departman Adı : {self.departman_name}\n'
              f'Çalışan Sayısı : {self.employe_count}\n'
              f'İsim Soyisim : {self.name}\n'
              f'Yaş : {self.age}')

name = input('İsim Soyisim : ')
age = int(input('Yaş : '))
d1 = Departman(name, age)
d1.get_info()

name = input('İsim Soyisim : ')
age = int(input('Yaş : '))
d2 = Departman(name, age)
d2.get_info()

name = input('İsim Soyisim : ')
age = int(input('Yaş : '))
d3 = Departman(name, age)
d3.get_info()

name = input('İsim Soyisim : ')
age = int(input('Yaş : '))
d4 = Departman(name, age)
d4.get_info()

# endregion





# region Task 4
# Software_Developer sınıfı yaratın
# first_name last_name --> object attribute
# knowledge_language =  [] --> class attribute
# get_info() -> İsim soyisim, bildiği diller  ve kaç dil bildiği bilgisini içercek içekilde düzenleme yapılsın.
# languages_append() fonksiyonu olsun . Lakin bazen bir dil bazende birden fazla dil eklenebilir.
# example input -> python
# example input -> python , c# , java


class Software_Developer:
    knowledge_language = []

    def __init__(self, first_name:str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        print(f'CV BİLGİSİ\n'
              f'=============\n'
              f'İsim Soyisim : {self.first_name} {self.last_name}\n'
              f'Bildiği Diller : {self.knowledge_language}\n'
              f'Bildiği Dil Sayısı : {len(self.knowledge_language)}')
    def languages_append(self, row:str):

        languages = row.split(',')
        for item in languages:
            self.knowledge_language.append(item.strip())

        return self.knowledge_language

name = input('İsim : ')
last_name = input('Soyisim : ')

s1 = Software_Developer(name, last_name)
languages = input('Bilinen Diller : ')
s1.languages_append(languages)
s1.get_info()

# endregion





# region Task 5
# Category adında sınıf yaratalım ve category dict olarak bulunsun.
# id, name, description -->  object attribute
# id --> uuid4() ile üretilsin
# Crud operasyonu yapın

from uuid import uuid4
from pprint import pprint

categories = {}
class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.id = str(uuid4())


class CategoryService:

    def create(self, obj: Category):
        categories[obj.id] = {
            'name': obj.name,
            'description': obj.description
        }
        print(f'{obj.id} Nolu ID ile Kayıtlara Eklenmiştir.')
        pprint(categories)

    def update(self, _id: str, name: str, description: str):
        for key, value in categories.items():
            if key == _id:
                value.update({
                    'name': name,
                    'description': description
                })

        print(f'{_id} Nolu ID Güncellenmiştir.')
        pprint(categories)

    def delete(self, _id: str):
        for key in categories.keys():
            if key == _id:
                del categories[_id]
                break

    def get_by_id(self, _id: str):
        for key in categories.keys():
            if key == _id:
                print(categories[key])

    def get_all_categories(self):
        pprint(categories)


def main():
    while True:
        service = CategoryService()
        proces = input('İşlem Türü : ')

        match proces:
            case 'create':
                name = input('İsim : ')
                description = input('Tanım : ')
                obj = Category(name, description)
                service.create(obj)
            case 'update':
                _id = input('Güncellenecek ID Bilgisi : ')
                name = input('İsim : ')
                description = input('Tanım : ')
                service.update(_id, name, description)
            case 'delete':
                _id = input('Güncellenecek ID Bilgisi : ')
                service.delete(_id)
            case 'ip':
                _id = input('Güncellenecek ID Bilgisi : ')
                service.get_by_id(_id)
            case 'list':
                service.get_all_categories()

main()

# endregion




# region Task 6

# BasePhone kalıtımlı Samsung, Iphone ve Nokia Sınıfları Yaratalım.
# Telefon Bilgileri ekrana basan fonksiyon ve her telefonun Kendine özgü sesini belirten bir fonksiyon yaratalım
# IMEI uudi4() olarak yaratılsın.

from uuid import uuid4
class BasePhone:
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price
        self.id = str(uuid4())

    def get_info(self):
        print(f'Telefon Bilgisi\n'
              f'================\n'
              f'IMEI : {self.id}\n'
              f'Model : {self.model}\n'
              f'Brand : {self.brand}\n'
              f'Price : {self.price} ')

    def phone_ring_sound(self) -> str:
        return 'Genel Telefon Sesi'


class Samsung(BasePhone):
    def __init__(self, brand, model, price, operating_system: str):
        super().__init__(brand, model, price)
        self.operating_system = operating_system


    def get_info(self):
        super().get_info()
        print(f'System : {self.operating_system}')

    def phone_ring_sound(self) -> str:
        return 'Samsung Telefon Sesi'


class Iphone(BasePhone):
    def __init__(self, brand, model, price, camera: str):
        super().__init__(brand, model, price)
        self.camera = camera

    def get_info(self):
        super().get_info()
        print(f'Camera : {self.camera}')

    def phone_ring_sound(self) -> str:
        return 'Iphone Telefon Sesi'


class Nokia(BasePhone):
    def __init__(self, brand, model, price, antenna: str):
        super().__init__(brand, model, price)
        self.antenna = antenna

    def get_info(self):
        super().get_info()
        print(f'Antenna : {self.antenna}')

    def phone_ring_sound(self) -> str:
        return 'Nokia Telefon Sesi'


s1 = Samsung('Samsung', 's22', 17000, 'Android  ')
s1.get_info()
print(f'Ses Türü :{s1.phone_ring_sound()}')
print()
i1 = Iphone('Iphone', '15 Pro Max', 89000, '24 MP ')
i1.get_info()
print(f'Ses Türü : {i1.phone_ring_sound()}')
print()
n1 = Nokia('Nokia', '5110', 3000, 'Var')
n1.get_info()
print(f'Ses Türü : {n1.phone_ring_sound()}')

# endregion




# region Task 7

# Basebill kalıtımlı WaterBill, ElectrictyBill, NaturalGasBill sınıfları yaratalım.
# Ödenecek tutarları hesapladıktan sonra hem çıktısını verelim hem de log kaydı oluşturup dosyada saklayalım

from datetime import datetime

class BaseBill:
    def __init__(self, bill_name: str, value_ad_task: float, amount: float):
        self.bill_name = bill_name
        self.value_ad_task = value_ad_task
        self.amount = amount

    def calculate_bill(self) -> float:
        return self.amount * self.value_ad_task

    def create_log(self):
        with open(
            file='Create_log.txt',
            mode='a',
            encoding='utf-8'
        ) as file:
            file.write(f'Fatura Bilgisi : {self.bill_name}\n'
                       f'Ödenecek Tutar : {self.calculate_bill()}\n'
                       f'Tarih : {datetime.now()}\n')

class WaterBill(BaseBill):
    def __init__(self, mill: int, bill_name, value_ad_task, amount):
        super().__init__(bill_name, value_ad_task, amount)
        self.mill = mill

    def calculate_bill(self):
        return super().calculate_bill() * self.mill


class ElectrictyBill(BaseBill):
    def __init__(self, kw: int, bill_name, value_ad_task, amount):
        super().__init__(bill_name, value_ad_task, amount)
        self.kw = kw

    def calculate_bill(self):
        return self.amount * self.value_ad_task * self.kw


class NaturalGasBill(BaseBill):
    def __init__(self, m3: int, bill_name, value_ad_task, amount):
        super().__init__(bill_name, value_ad_task, amount)
        self.m3 = m3

    def calculate_bill(self):
        return self.amount * self.value_ad_task * self.m3


while True:
    proces = input('Fatura Bilgisi : ')

    match proces:
        case 'Su Faturası':
            w1 = WaterBill(3, 'Su Faturası', 2, 10)
            print(w1.calculate_bill())
            w1.create_log()
        case 'Elektrik Faturası':
            e1 = ElectrictyBill(4, 'Elektrik Faturası', 2, 10)
            print(e1.calculate_bill())
            e1.create_log()
        case 'Doğalgaz Faturası':
            g1 = NaturalGasBill(5, 'Gaz Faturası', 2, 10)
            print(g1.calculate_bill())
            g1.create_log()
        case _:
            print(f'Sadece Su Faturası, Elektrik Faturası ve Doğalgaz Faturası sonucuna ulaşabilirsiniz. ')
            with open(file='System.txt', mode='a', encoding='utf-8') as file:
                file.write(f'Müşterimiz Yanlış Fatura Bilgisi Girişi Yaptı . . ')

# endregion