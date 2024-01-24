class Human():
    def __init__(self, full_name, data_birth, telephone, city, country, home_adress):
        self.__full_name = full_name
        self.data_birth = data_birth
        self.__telephone = telephone
        self.city = city
        self.country = country
        self.home_adress = home_adress

    def input_data(self):
        self.__full_name = input(f"Enter your full Name: ")
        self.data_birth = input(f"Enter your date of birth: ")
        self.__telephone = input(f"Enter your phone number: ")
        self.city = input(f"Enter your locality: ")
        self.country = input(f"Enter country: ")
        self.home_adress = input(f"Enter home adress: ")

    def print_info(self):
        print(f"Full Name: {self.__full_name}")
        print(f"Date of Birth: {self.data_birth}")
        print(f"Phone number: {self.__telephone}")
        print(f"Locality: {self.city} ")
        print(f"Country: {self.country}")
        print(f"Home adress: {self.home_adress}")

man = Human("Ruslan","11.06.2001","+380654421","Lviv","UA","Soborna street 12")
man.print_info()


class City():
    def __init__(self, city_name, name_region, name_country, population, postcode, telephone_code, ):
        self.__city_name = city_name
        self.__name_region = name_region
        self.__name_country = name_country
        self.populations = population
        self.postcode = postcode
        self.telephone_code = telephone_code

    def print_info(self):
        print("City: " + self.__city_name)
        print("Region: " + self.__name_region)
        print("Country: " + self.__name_country)
        print("City population: " + self.populations)
        print("City postal code: " + self.postcode)
        print("Telephone city code: " + self.telephone_code)

    def input_river(self, river):
        print(self.__city_name + " is located on the river " + river)


city1 = City("London", "England", "United Kingdom", "8,982 million", "EC2MQW", "+4420")
city1.print_info()
city1.input_river("Themse")


class Country():
    def __init__(self, name_country, continent, country_population, telephone_code_country, name_capital, names_cities):
        self.name_country = name_country
        self.__continent = continent
        self.__country_population = country_population
        self.__telephone_code_country = telephone_code_country
        self.__name_capital = name_capital
        self._names_cities = names_cities

    def input_data(self):

        self.name_country = input("Enter you country: ")
        self.__continent = input("Enter you continent: ")
        self.__country_population = input("Enter population of the country: ")
        self.__telephone_code_country = input("Enter country dialing code: ")
        self.__name_capital = input("Enter capital name: ")
        self._names_cities = input("Enter name of the cities in the country: ")

    def print_info(self):

        print(f"Country: {self.name_country}")
        print(f"Continent: {self.__continent}")
        print(f"Population: {self.__country_population}")
        print(f"Phone code: {self.__telephone_code_country}")
        print(f"Capital: {self.__name_capital}")
        print(f"Cities: {self._names_cities}")

    def __del__(self):
        print(f"Object {self.name_country} deleted")




class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def input_data(self):
        self.numerator = int(input("Введіть чисельник: "))
        self.denominator = int(input("Введіть знаменник: "))

    def display_data(self):
        print(f"{self.numerator}/{self.denominator}")

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"