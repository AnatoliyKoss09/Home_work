# 1
class Human():
    __id = 1
    _name = "Ivan"
    _age = 23
    nationality = "Ukrainian"

    def __init__(self, __id, _name, _age, nationality):
        Human.__id = Human.__id + 1
        self._name = _name
        self._age = _age
        self.nationality = nationality

    def __str__(self):
        return f"ID: {self.__id} Name: {self._name} Age: {self._age}, Nationality: {self.nationality}"

    def set_name(self, new_name):
        self._name = new_name

    def set_age(self, new_age):
        self._age = new_age

    def set_nationality(self, new_nationality):
        self.nationality = new_nationality

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_nationality(self):
        return self.nationality


man1 = Human(1, "Karl", 28, "German")
man1.set_name("Oleg")
man1.set_age(26)
man1.set_nationality("Ukrainian")
print(man1.__str__())


class Builder(Human):
    __id = 1
    country = "UK"
    build_company = "BAM"

    def __init__(self, __id, _name, _age, nationality, country, build_company):
        super().__init__(__id, _name, _age, nationality)
        self.country = country
        self.build_company = build_company

    def __str__(self):
        super().__str__()
        return (f"ID: {self.__id} Name:{self._name} Age:{self._age} Nationality:{self.nationality}\n"
                f" Country: {self.country},Build Company: {self.build_company}")

    def set_country(self, new_country):
        self.country = new_country

    def set_build_company(self, new_build_company):
        self.build_company = new_build_company

    def get_country(self):
        return self.country

    def get_build_company(self):
        return self.build_company


build = Builder(2, "Grisha", 39, "turk", "Ukraine", "Ukrbud")
print(build.__str__())
print(isinstance(build, Human))


class Sailor(Human):
    __id = 1
    city = "Odessa"
    sailor_company = "MSC"
    sea = "Black"
    salary = "1200$"

    def __init__(self, __id, _name, _age, nationality, city, sailor_company, sea, salary):
        super().__init__(__id, _name, _age, nationality)
        self.city = city
        self.sailor_company = sailor_company
        self.sea = sea
        self.salary = salary

    def __str__(self):
        super().__str__()
        return (f"ID: {self.__id} Name:{self._name} Age:{self._age} Nationality:{self.nationality} City: {self.city}\n "
                f"Sailor Company: {self.sailor_company},Sea: {self.sea},Salary: {self.salary}")

    def set_city(self, new_city):
        self.city = new_city

    def set_sailor_company(self, new_sailor_company):
        self.sailor_company = new_sailor_company

    def set_sea(self, new_sea):
        self.sea = new_sea

    def set_salary(self, new_salary):
        self.salary = new_salary

    def get_city(self):
        return self.city

    def get_sailor_company(self):
        return self.sailor_company

    def get_salary(self):
        return self.salary


sailor1 = Sailor(3, "Petro", 29, "greec", "Budva", "ABS", "Red", "1300$")
print(sailor1.__str__())
print(isinstance(sailor1, Human))


class Pilot(Human):
    __id = 1
    airport = "Borispol IA"
    air_company = "UA Airlines"
    salary = "11000$"

    def __init__(self, __id, _name, _age, nationality, airport, air_company, salary):
        super().__init__(__id, _name, _age, nationality)
        self.airport = airport
        self.air_company = air_company
        self.salary = salary

    def __str__(self):
        super().__str__()
        return (
            f"ID: {self.__id} Name:{self._name} Age:{self._age} Nationality:{self.nationality} Airport: {self.airport}\n "
            f"Air Company: {self.air_company} Salary: {self.salary}")

    def set_airport(self, new_airport):
        self.airport = new_airport

    def set_air_company(self, new_air_company):
        self.air_company = new_air_company

    def set_salary(self, new_salary):
        self.salary = new_salary

    def get_airport(self):
        return self.airport

    def get_air_company(self):
        return self.air_company

    def get_salary(self):
        return self.salary


pilot1 = Pilot(4, "Natasha", 56, "moldavian", "Tiraspol", "IAM", "3000$")
print(pilot1.__str__())
print(isinstance(pilot1, Human))

#2

class Passport():
    _name = "Oleg"
    _surname = "Borsh"
    sex = "Male"
    date_of_birth = "12.12.2002"
    __seria = "KM"
    __number = 5402190
    nationality = "Ukrainian"

    def __init__(self, name, surname, sex, date_of_birth, seria, number, nationality):
        self._name = name
        self._surname = surname
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.__seria = seria
        self.__number = number
        self.nationality = nationality

    def set_name(self, new_name):
        self._name = new_name

    def set_surmane(self, new_surname):
        self._surname = new_surname

    def set_sex(self, new_sex):
        self.sex = new_sex

    def set_date_of_birth(self, new_date_of_birth):
        self.sex = new_date_of_birth

    def set_nationality(self, nationality):
        self.sex = nationality

    def get_name(self):
        return self._name

    def get_surmane(self):
        return self._surname

    def get_sex(self):
        return self.sex

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_nationalit(self):
        return self.nationality

    @property
    def seria(self):
        return self.__seria

    @seria.setter
    def seria(self, newseria):
        self.__seria = newseria

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, newnumber):
        self.__number = newnumber

    def print_info(self):
        print(f"ПАСПОРТ ГРОМАДЯНИНА УКРАЇНИ\n"
              f"Прізвище: {self._surname} Ім'я: {self._name} Стать: {self.sex} Дата народження: {self.date_of_birth}\n"
              f"Національність: {self.nationality} Серія: {self.__seria} Номер: {self.__number}")


man1 = Passport("Іван", "Радченко", "M", "12.02.2002", "KM", 5467890, "Українець")
man1.seria = 1234
man1.number = 9999
man1.set_surmane("Шевченко")
man1.print_info()


class ForeignPassport(Passport):
    def __init__(self, name, surname, sex, date_of_birth, nationality, viza, number2, seria, number):
        super().__init__(name, surname, sex, date_of_birth, nationality, seria, number)
        self.viza = viza
        self.number2 = number2

    def print_info(self):
        print(f"Foreign passport of a citizen of Ukraine\n"
              f"Surname: {self._surname} Ім'я: {self._name} Sex: {self.sex} Date of birth: {self.date_of_birth}\n"
              f"National: {self.nationality} Viza: {self.viza} Number Passport: {self.number2}")


man2 = ForeignPassport("Oleg", "Ukrainets", "M", "12.09.1989", "ukrainian", "open", 356, None, None)
man2.set_name("Anatolii")
man2.set_surmane("Shevchenko")
man2.print_info()

# 3

class Animal():
    weight = 120
    live_areal = "Avstlralia"
    red_book_animalse = True

    def __init__(self, weight, live_areal, red_book_animalse):
        self.weight = weight
        self.live_areal = live_areal
        self.red_book_animalse = red_book_animalse

    def print_info(self):
        print(
            f" Weight: {self.weight}, Areal: {self.live_areal} Red Book species: {self.red_book_animalse}")


class Tiger(Animal):
    def __init__(self,class_animal, name, weight, live_areal, red_book_animalse):
        super().__init__(weight, live_areal, red_book_animalse)
        self.name = name
        self.class_animal = class_animal

    def print_info(self):
        print(f"Animal class: {self.class_animal} Animal:{self.name} Weight: {self.weight} Areal: {self.live_areal}\n"
              f"Red Book species: {self.red_book_animalse}")

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_class_animal(self, new_class_animal):
        self.name = new_class_animal

    def get_class_animal(self):
        return self.class_animal


tiger1 = Tiger("Mammals","Tiger", 190, "Asia", True)
tiger1.set_name("Amur tiger")
tiger1.print_info()
print(isinstance(tiger1, Animal))


class Crocodile(Animal):
    def __init__(self, class_animal, name, weight, live_areal, red_book_animalse):
        super().__init__(weight, live_areal, red_book_animalse)
        self.name = name
        self.class_animal = class_animal

    def print_info(self):
        print(f"Animal class: {self.class_animal} Animal:{self.name} Weight: {self.weight} Areal: {self.live_areal}\n"
              f"Red Book species: {self.red_book_animalse}")

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_class_animal(self, new_class_animal):
        self.name = new_class_animal

    def get_class_animal(self):
        return self.class_animal


crocodile1 = Crocodile("Reptile", "Crocodaile", 600, "Africa", False)
crocodile1.set_name("Aligator")
crocodile1.print_info()
print(isinstance(crocodile1, Animal))

class Kangaroo(Animal):

    def __init__(self, class_animal, name, weight, live_areal, red_book_animalse,endemic_species):
        super().__init__(weight, live_areal, red_book_animalse)
        self.name = name
        self.class_animal = class_animal
        self.__endemic_species = endemic_species

    def print_info(self):
        print(f"Animal class: {self.class_animal} Animal:{self.name} Weight: {self.weight} Areal: {self.live_areal}\n"
              f"Red Book species: {self.red_book_animalse} Endemic species: {self.__endemic_species}")

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_class_animal(self, new_class_animal):
        self.name = new_class_animal

    def get_class_animal(self):
        return self.class_animal


kangaroo1 = Kangaroo("Mammals","Kangaroo",200,"Avstrlalia",True,True)
kangaroo1.set_name("Kangaroo")
kangaroo1.print_info()
print(isinstance(kangaroo1, Animal))
