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




# region Task 8

# BaseEntity Kalıtımlı Araç sınıfı yaratalım.
# Araba sınıfında brand , model --> object attribute
# Değer ve şaşi numarası encapsule edilsin ve araba değeri sfırdan büyükse ürün yaratılsın.
# Araba statüsünü Enum ile belirtelim.

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint

class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3

class BaseEntity:
    def __init__(self):
          self.__create_date = ''
          self.__created_computer_name = ''
          self.__created_ip_address = ''
          self.__status = ''

    def set_values(self):
          self.__create_date = datetime.now()
          self.__created_computer_name = gethostname()
          self.__created_ip_address = gethostbyname(gethostname())
          self.__status = Status.Active.name

class Vehicle(BaseEntity):
      def __init__(self, model: str, brand: str):
            super().__init__()
            self.model = model
            self.brand = brand
            self.__vin = ''
            self.__price = 0

      def set_values(self, price: float):
            if price > 0:
                  self.__vin = str(uuid4())
                  self.__price = price
                  super().set_values()

            print(f'{self.__vin} Şaşi Numaralı Araç Kayıtlara Eklenmiştir.')
            print()
            pprint(self.__dict__)

v1 = Vehicle('OMODA 5', 'CHERY')
v1.set_values(1300000)

# endregion




#region Task 9

# Toplama, Üs Alma, Faktöriyel Hesaplamalarının Sonuçlarının Kaç Saniyede Hesaplandığını Bulan Dekoratör Yazalım

from math import pow, factorial
from time import sleep, time

def calculate_time_execute(funcution):
    def inner_func(*args, **kwargs):
        start_time = time()
        sleep(2)
        func = funcution(*args, **kwargs)
        end_time = time()
        print(f'Start Time : {start_time}\n'
              f'End Time : {end_time}\n'
              f'Result : {end_time - start_time}\n'
              f'====================================')

    return inner_func

@calculate_time_execute
def us_alma(a: int, b: int):
    print(f'Sonuç : {pow(a, b)}')


@calculate_time_execute
def faktoriyel_hesaplama(a: int):
    print(f'Faktöriyel : {factorial(a)}')

@calculate_time_execute
def toplam(x: int, y: int, z: int):
    print(f'Sonuç : {x + y + z}')


us_alma(1,4)
faktoriyel_hesaplama(4)
toplam(1, 2, 3)


# endregion




# region Task 10
# 2 sayının Toplamını yazan ve sonucun Loglarını tutan  Dekoratör Yazalım

from socket import gethostname, gethostbyname
from datetime import datetime

def log_decorators(funcution):
    def inner_func(*args, **kwargs):
        func = funcution(*args, **kwargs)
        with open(file='Decorators.Log.txt', mode='a', encoding='utf-8') as file:
            file.write(f'İşlem Sonucu : {func}\n'
                       f'Hesaplamayı Yapan Makine : {gethostname()}\n'
                       f'Makine Ip : {gethostbyname(gethostname())}\n'
                       f'İşlem Tarih ve Saati : {datetime.now()}\n')
        return func
    return inner_func

@log_decorators
def toplama(a: int, b: int):
    return a + b

a = int(input('1. Sayı : '))
b = int(input('2. Sayı : '))
print(toplama(a, b))

# endregion




# region Task 11
# Yetkilendirme Yapan Dekoratör Yazalım

def reguired_login(function):
    def inner_func(user):
        if user.get('role') != 'admin':
            return 'User has not authorize'

        return function(user)

    return inner_func

@reguired_login
def redirect_dashboard(user: dict):
    return f'{user.get("user name")} dashboard page has been opening..!'


print(
    redirect_dashboard({
        'user name': 'beast',
        'password': '123',
        'role': 'admin'})
)

# endregion




# region Task 12

# Karakterleri Dönüştüren Dekoratör Yazalım

def convert_character(function):
    def inner_func(*args, **kwargs):
        func = function(*args, **kwargs)
        last_version = func.replace('İ', 'I').replace('Ü', 'U')
        return last_version

    return inner_func

@convert_character
def greeting_people(name: str):
    return f'Welcome {name}'

@convert_character
def create_email(firs_name: str, last_name: str):
    return f'{firs_name}.{last_name}@hotmail.com'


print(greeting_people('İpek Üzüm'))
print(create_email('İpek', 'Üzümcü'))

# endregion




#region Task 13
# Müzik Aletleri ve Müzisyen yaratalım.

from abc import ABC, abstractmethod

class BaseMuzikAleti:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

class Gitar(BaseMuzikAleti):
    def __init__(self, brand, model, tel):
        super().__init__(brand, model)
        self.tel = tel

class Keman(BaseMuzikAleti):
    def __init__(self, brand, model, govde):
        super().__init__(brand, model)
        self.govde = govde

class Muzisyen:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
        self.caldigi_enstrumanlar = []

class BaseService(ABC):

    @abstractmethod
    def call_sound(self) -> str: pass

    def hello_word(self):
        print('Hi')
    @abstractmethod
    def harmonize(self) -> str: pass

class GitarService(BaseService):

    def harmonize(self) -> str:
        return 'Akord Edildi'

    def call_sound(self) -> str:
        return 'Gitar Sesi'

    def pena(self):
        return 'Pena değiştirildi'

class KemanService(BaseService):
    def call_sound(self) -> str:
        return 'Keman Sesi'

    def harmonize(self) -> str:
        return 'Akord Edildi'


    def hello_word(self):
        print('Beni Dinlediğiniz İçin Teşekkürler . . ')

def main():
    gitar_service = GitarService()

    gitar = Gitar('Fender', 'ESP LTD EC-1000', 'Elixir Nanoweb')
    keman = Keman('Gliga', 'Gliga Maestro', 'Abonoz')

    muzisyen = Muzisyen('Emre', 'Yücel')

    muzisyen.caldigi_enstrumanlar.append(gitar)
    muzisyen.caldigi_enstrumanlar.append(keman)

    print(f'Ad : {muzisyen.first_name}\n'
          f'Soyad: {muzisyen.last_name}\n'
          f'Brand: {muzisyen.caldigi_enstrumanlar[0].brand}\n'
          f'Model  : {muzisyen.caldigi_enstrumanlar[0].model}\n'
          f'Çıkardığı Ses :{gitar_service.call_sound()}\n'
          f'Akor Durumu : {gitar_service.harmonize()} ')

main()

# endregion




# region Task 14

# Fatura oluşturualım ve Sisteme giren kişinin fatura bilgisinin log kayıtlarını tutup ardından log kayıtlarını ekrana basalım
# Sadece log kaydını calıstır sistem log dosyasını sonrada ekrana basılsın.

import datetime
from abc import abstractmethod, ABC
from datetime import datetime
class BaseBill:
    def __init__(self, bill_name:str, value_ad_task: float, amount: float):
        self.bill_name = bill_name
        self.value_ad_task = value_ad_task
        self.amount = amount

class ElectricBill(BaseBill):
    def __init__(self,bill_name, value_ad_task, amount, kw: float):
        super().__init__(bill_name, value_ad_task, amount)
        self.kw = kw


class WaterBill(BaseBill):
    def __init__(self,bill_name, value_ad_task, amount, mill: float):
        super().__init__(bill_name, value_ad_task, amount)
        self.mill = mill


class GassBill(BaseBill):
    def __init__(self,bill_name, value_ad_task, amount, m3: float):
        super().__init__(bill_name, value_ad_task, amount)
        self.m3 = m3


class BaseService(ABC):
    @abstractmethod
    def hesaplama(self, bill: BaseBill):
        pass

    def log(self, bill: BaseBill, sonuc: float):
        with open(
            file='log.txt',
            mode='w',
            encoding='utf-8'
        ) as file:
            file.write(f'Fatura Adı : {bill.bill_name}\n'
                       f'Fatura Tutarı : {sonuc}\n'
                       f'Fatura Tarihi : {datetime.now()}\n')


class WaterBillService(BaseService):
    def hesaplama(self, bill: WaterBill):
        return bill.mill * bill.value_ad_task * bill.amount

class ElectricBillService(BaseService):
    def hesaplama(self, bill: ElectricBill):
        return bill.kw * bill.value_ad_task * bill.amount

class GassBillService(BaseService):
    def hesaplama(self, bill: GassBill):
        return bill.m3 * bill.value_ad_task * bill.amount



def main():
    e1 = ElectricBill('Elektrik Faturası', 10, 5, 4)
    w1 = WaterBill('Su Faturası', 7, 4, 6)
    g1 = GassBill('Gaz Faturası', 2 , 3, 6)

    islem = input(f'Hangi Faturayı Ödemek istediniz: ')

    match islem:
        case 'elektrik':
            pass
        case 'su':
            waterservice = WaterBillService()
            sonuc = waterservice.hesaplama(w1)
            waterservice.log(w1, sonuc)
            with open(
                    file='log.txt',
                    mode='r',
                    encoding='utf-8'
            ) as file:
                for i in file.readlines():
                    print(i)
        case 'gaz':
            pass

main()

# endregion