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