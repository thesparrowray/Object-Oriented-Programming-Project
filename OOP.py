from difflib import restore
from pickle import PROTO

import colorama
import Funcs
import data
import re

# from Funcs import webcam_info


class Shop:
    name = 'Cloud Store'
    def __init__(self):
        self._employees = {}
        self._branches = []
        self._contact_info = ''
        self._inventory = {}
        self._active_hours  = ''
        self._web_address = ''


# ---------------------------------------------------------
# ---------------------------------------------------------
class Person:
    def __init__(self):
        self._name = ''
        self._lastname = ''
        self._phonenumber = ''
        self._username = ''
        self._password = ''

    # name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if value.isalpha() and len(value) >= 2:
            self._name = value
        else:
            print(colorama.Fore.RED, 'Only letters, >= 2', colorama.Fore.RESET)

    # ;ast name
    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self, value):
        if value.isalpha() and len(value) >= 3:
            self._lastname = value
        else:
            print(colorama.Fore.RED, 'Only letters, >= 3', colorama.Fore.RESET)

    #phone number
    @property
    def phonenumber(self):
        return self._phonenumber
    @phonenumber.setter
    def phonenumber(self, value):
        if len(value) == 11 and value.isdigit() and value[0:2] == '09':
            self._phonenumber = value
        else:
            print(colorama.Fore.RED, 'phone number must have 11 digits and start with 09', colorama.Fore.RESET)

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        if len(value) > 3:
            self._username = value
        else:
            print(colorama.Fore.RED, 'username must be more than 3 characters', colorama.Fore.RESET)

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

# ---------------------------------------------------------
class Employee(Person):
    access = {'1': 'see personal info', '2': 'edit personal info', '3': 'calculate salary'}
    def __init__(self):
        super().__init__()
        self._empaddress = ''
        self._national_id = 'None'
        self._employment_id = 'None'
        self._salary  = 0
        self._overtime_m = 0
        self._insurance = ''
        self._offdays = []
        self._role = ''


    # #employee address
    @property
    def empaddress(self):
        return self._empaddress
    @empaddress.setter
    def empaddress(self, value):
        if len(value) > 10:
            self._empaddress = value
        else:
            print(colorama.Fore.RED, 'address too short', colorama.Fore.RESET)

    # national id
    @property
    def national_id(self):
        return self._national_id
    @national_id.setter
    def national_id(self, value):
        if len(value) == 10 and value.isdigit():
            self._national_id = int(value)
        else:
            print(colorama.Fore.RED, 'National ID must have 10 digits!', colorama.Fore.RESET)

    #employment id
    @property
    def employment_id(self):
        return self._employment_id
    @employment_id.setter
    def employment_id(self, value):
        if len(value) == 8 and value.isdigit():
            self._employment_id = value
        else:
            print(colorama.Fore.RED, 'Employment ID must have 8 digits!', colorama.Fore.RESET)

    #salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        try:
            value = int(value)
            if int(value) >= 15000000:
                self._salary = int(value)
            else:
                print(colorama.Fore.RED, 'salary cannot be less than 15,000,000', colorama.Fore.RESET)
        except ValueError:
            print(colorama.Fore.RED, 'Salary must be higher than 15 millions!', colorama.Fore.RESET)

    #overtime m
    @property
    def overtime_m(self):
        return self._overtime_m
    @overtime_m.setter
    def overtime_m(self, value):
        try:
            if int(value) >= 60:
                self._overtime_m = int(value)
            else:
                print(colorama.Fore.RED, 'Overtime must be at least 60 minutes.', colorama.Fore.RESET)
        except ValueError:
            print(colorama.Fore.RED, 'Overtime must be a number (in minutes).', colorama.Fore.RESET)

    #insurance type
    @property
    def insurance(self):
        return self._insurance
    @insurance.setter
    def insurance(self, value):
        if value.lower()== 'basic' or value.lower() == 'premium':
            self._insurance = value
        else:
            print(colorama.Fore.RED, 'invalid insurance type', colorama.Fore.RESET)

    # off days
    @property
    def offdays(self):
        return self._offdays
    @offdays.setter
    def offdays(self, value):
        if len(value) == 2 and value[0] != value[1]:
            self._offdays = value
            print(colorama.Fore.GREEN, 'adding...', colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, 'off days must be 2 different days!', colorama.Fore.RESET)

    #role
    @property
    def role(self):
        return self._role
    @role.setter
    def role(self, value):
        if len(value) >= 3:
            self._role = value
        else:
            print(colorama.Fore.RED, 'role input too short', colorama.Fore.RESET)

# ----------------------------------------------------------
class Admin(Employee):
    def __init__(self):
        super().__init__()
        self._access = []

    @property
    def access(self):
        return self._access
    @access.setter
    def access(self, value):
        if len(value) == 0:
            print(colorama.Fore.RED, 'access not defined', colorama.Fore.RESET)
        else:
            self._access = value

# ----------------------------------------------------------
class Customer(Person):
    access = {'1': 'see personal info', '2': 'edit personal info', '3': 'liked items', '4': 'shopping cart', '5': 'shop'}
    liked_items = []
    def __init__(self):
        super().__init__()
        self._address = {}
        self._postal_code = ''
        self._email = ''
        self._wallet = 0
        self._debt = 0
        self._orders = {}



    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value):
        if value:
            self._address = value
        else:
            print(colorama.Fore.RED, 'address not set', colorama.Fore.RESET)

    # postal code
    @property
    def postal_code(self):
        return self._postal_code
    @postal_code.setter
    def postal_code(self, value):
        if len(value) == 10 and value.isdigit():
            self._postal_code = value
        else:
            print(colorama.Fore.RED, 'enter 10 numbers', colorama.Fore.RESET)

    # email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value



# ----------------------------------------------------------
# ----------------------------------------------------------
class Item:
    def __init__(self):
        self._code = ''
        self._model = ''
        self._brand = ''
        self._price = 0
        self._off = 0
        self._stock = 0
        self._warranty_time = 'none'
        self._warranty_company = 'none'
        self._customer_rating = 0
        self._weight = ''
        self._size = '0x0x0'
        self._color = ''
        self._production_year = '0000'
        self._battery_life  = ''
    #code
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, value):
        if len(value) == 4:
            self._code = value
        else:
            print(colorama.Fore.RED, 'code must be 4 digits', colorama.Fore.RESET)
    #model
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, value):
        if len(value) > 5:
            self._model = value
        else:
            print(colorama.Fore.RED, 'model name must have > 5 characters', colorama.Fore.RESET)
    #brand
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, value):
        if value.lower() in data.brands and len(value) >= 2:
            self._brand = value
        else:
            print(colorama.Fore.RED, '< 2 characters or not in brands list', colorama.Fore.RESET)
    #price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value.isdigit() and int(value) > 1000000:
            self._price = int(value)
        else:
            print(colorama.Fore.RED, 'value must be a number > 1,000,000', colorama.Fore.RESET)
    #off
    @property
    def off(self):
        return self._off
    @off.setter
    def off(self, value):
        if value.isdigit() and int(value) < 100:
            self._off = int(value)
        else:
            print(colorama.Fore.RED, 'write without % sign, only number < 100', colorama.Fore.RESET)
    #stock
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, value):
        if value.isdigit() and int(value) >=0:
            self._stock = int(value)
        else:
            print(colorama.Fore.RED, 'stock must be a digit', colorama.Fore.RESET)
    #warranty_time
    @property
    def warranty_time(self):
        return self._warranty_time
    @warranty_time.setter
    def warranty_time(self, value):
        if len(value) >=2 :
            self._warranty_time = value
        else:
            print(colorama.Fore.RED, 'len input >= 2', colorama.Fore.RESET)

    # warranty_company
    @property
    def warranty_company(self):
        return self._warranty_company
    @warranty_company.setter
    def warranty_company(self, value):
        if len(value) >= 2 and value.lower() in data.warranty_companies:
            self._warranty_company = value
        else:
            print(colorama.Fore.RED, 'warranty company unknown', colorama.Fore.RESET)

    #customer_rating
    @property
    def customer_rating(self):
        return self._customer_rating
    @customer_rating.setter
    def customer_rating(self, value):
        if value.isdigit() and 1<= int(value) <= 5:
            self._customer_rating = int(value)
        else:
            print(colorama.Fore.RED, 'rating between 1 and 5', colorama.Fore.RESET)

    #weight
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        if len(value) > 1:
            self._weight = value
        else:
            print(colorama.Fore.RED, 'len value > 1', colorama.Fore.RESET)

    #size format y x y x y
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if 1 <= value.count('x') <= 2:
            self._size = value
        else:
            print(colorama.Fore.RED, 'enter size in the given format', colorama.Fore.RESET)
    #color
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        colors_list = Funcs.read_json_colors()
        match_found = any(i["name"].lower() == value.lower() for i in colors_list)
        if match_found:
            self._color = value
        else:
            print(colorama.Fore.RED, 'color not in colors.json', colorama.Fore.RESET)

    #production_year
    @property
    def production_year(self):
        return self._production_year
    @production_year.setter
    def production_year(self, value):
        if value.isdigit() and (len(value) == 2 or len(value) == 4):
            self._production_year = value
        else:
            print(colorama.Fore.RED, 'wrong production year, xxxx or xx', colorama.Fore.RESET)

    #battery_life
    @property
    def battery_life(self):
        return self._battery_life
    @battery_life.setter
    def battery_life(self, value):
        if len(value) >= 2:
            self._battery_life = value
        else:
            print(colorama.Fore.RED, 'len(input) >= 2', colorama.Fore.RESET)
# -----------------------------------------------------------
class Laptop(Item):
    def __init__(self):
        super().__init__()
        self._cpu = ''
        self._lram = ''
        self._storage = ''
        self._gpu = ''
        self._los = ''
        self._webcam = ''
        self._speaker = ''
        self._lscreensize = ''

    #cpu
    @property
    def cpu(self):
        return self._cpu
    @cpu.setter
    def cpu(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED, 'cpu info must be a string', colorama.Fore.RESET)
        if len(value.strip()) < 5:
            print(colorama.Fore.RED, 'len cpu info too short', colorama.Fore.RESET)
        if not ('amd' in value.lower() or 'intel' in value.lower() or 'apple' in value.lower()):
            print(colorama.Fore.RED, 'manufacturer not established', colorama.Fore.RESET)
        else:
            self._cpu = value

    #lram
    @property
    def lram(self):
        return self._lram
    @lram.setter
    def lram(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED, 'ram input must be a string', colorama.Fore.RESET)
        value = value.strip().upper()
        if not value.endswith('GB'):
            print(colorama.Fore.RED, 'write in the format "x GB"', colorama.Fore.RESET)
        else:
            number_part = value[:-2].strip()
            if not number_part.isdigit():
                print(colorama.Fore.RED, 'must contain a number', colorama.Fore.RESET)
            else:
                if int(number_part) <= 0:
                    print(colorama.Fore.RED, 'ram must be > 0', colorama.Fore.RESET)
                else:
                    self._lram = value

    #storage
    @property
    def storage(self):
        return self._storage
    @storage.setter
    def storage(self, value):
        if not isinstance(value.strip(), str):
            print(colorama.Fore.RED, 'storage input must be a string, e.g: 215 GB SSD', colorama.Fore.RESET)
        if not ('SSD' in value.upper() or 'HHD' in value.upper()):
            print(colorama.Fore.RED,'storage must be specified SSD or HHD', colorama.Fore.RESET)
        if not ('GB' in value.upper() or 'TB' in value.upper()):
            print(colorama.Fore.RED,'specify storage size in GB or TB', colorama.Fore.RESET)
        else:
            self._storage = value
    #gpu
    @property
    def gpu(self):
        return self._gpu
    @gpu.setter
    def gpu(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED,'input must be a string', colorama.Fore.RESET)
        if not len(value) > 5:
            print(colorama.Fore.RED,'input > 5', colorama.Fore.RESET)
        else:
            self._gpu =  value

    #los
    @property
    def los(self):
        return self._los
    @los.setter
    def los(self, value):
        if value.lower() in data.OS_laptop:
            self._los = value
        else:
            print(colorama.Fore.RED,'OS not established', colorama.Fore.RESET)

    #webcam
    @property
    def webcam(self):
        return self._webcam
    @webcam.setter
    def webcam(self, value):
        if len(value) > 7:
            self._webcam = value
        else:
            print(colorama.Fore.RED,'information incomplete', colorama.Fore.RESET)

    #speaker/ audio tech
    @property
    def speaker(self):
        return self._speaker
    @speaker.setter
    def speaker(self, value):
        if len(value) > 3:
            self._speaker = value
        else:
            print(colorama.Fore.RED,'too short', colorama.Fore.RESET)

    #lscreensize x inch
    @property
    def lscreensize(self):
        return self._lscreensize
    @lscreensize.setter
    def lscreensize(self, value):
        if len(value) >= 2:
            self._lscreensize = value
        else:
            print(colorama.Fore.RED, 'enter size in the given format', colorama.Fore.RESET)


# ----------------------------------------------------------
class Camera(Item):
    def __init__(self):
        super().__init__()
        self._memory = ''
        self._lenz = ''
        self._shutter = ''
        self._ctype = ''
        self._touchscreen = ''

    #memory
    @property
    def memory(self):
        return self._memory
    @memory.setter
    def memory(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED,'memory input must be a string, x GB', colorama.Fore.RESET)
        if not (value.lower().endswith('GB') and int(value.strip('GB')) > 0):
            print(colorama.Fore.RED,'write in the format "x GB"', colorama.Fore.RESET)
        else:
            self._memory = value
    #lenz
    @property
    def lenz(self):
        return self._lenz
    @lenz.setter
    def lenz(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED,'lenz information must be a string', colorama.Fore.RESET)
        else:
            self._lenz = value
    #shutter
    @property
    def shutter(self):
        return self._shutter
    @shutter.setter
    def shutter(self,value):
        if not isinstance(value, str):
            print(colorama.Fore.RED,'shutter information must be a string', colorama.Fore.RESET)
        else:
            self._shutter = value
    #ctype
    @property
    def ctype(self):
        return self._ctype
    @ctype.setter
    def ctype(self, value):
        if value.lower() == 'analogue' or value.lower() == 'digital':
            self._ctype = value
        else:
            print(colorama.Fore.RED,'just specify analogue or digital', colorama.Fore.RESET)

    #touchscreen
    @property
    def touchscreen(self):
        return self._touchscreen
    @touchscreen.setter
    def touchscreen(self, value):
        if value.lower() == 'yes' or value.lower() == 'no':
            self._touchscreen = value
        else:
            print(colorama.Fore.RED,'if it has, yes and if not, no', colorama.Fore.RESET)
# ----------------------------------------------------------
class Phone(Item):
    def __init__(self):
        super().__init__()
        self._storage = ''
        self._sim = '1'
        self._frontcam = ''
        self._backcam = ''
        self._pos = ''
        self._chargingport = ''
        self._pscreensize = ''

    #storage
    @property
    def storage(self):
        return self._storage
    @storage.setter
    def storage(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED,'storage input must be a string, x GB', colorama.Fore.RESET)
        if not value.lower().endswith('GB'):
            print(colorama.Fore.RED,'write in the format "x GB"', colorama.Fore.RESET)
        else:
            self._storage = value
    #sim
    @property
    def sim(self):
        return self._sim
    @sim.setter
    def sim(self, value):
        if value.isdigit() and int(value) > 0:
            self._sim = value
        else:
            print(colorama.Fore.RED,'just enter the number of sim cards ', colorama.Fore.RESET)
    #frontcam resolution
    @property
    def frontcam(self):
        return self._frontcam
    @frontcam.setter
    def frontcam(self, value):
        if value.lower().endswith("mp"):
            self._frontcam = value
        else:
            print(colorama.Fore.RED,'write front camera info in x MP', colorama.Fore.RESET)
    #backcam
    @property
    def backcam(self):
        return self._backcam
    @backcam.setter
    def backcam(self, value):
        if value.lower().endswith("mp") and value[:-2].strip().isdigit():
            self._backcam = value
        else:
            print(colorama.Fore.RED,'write back camera info in x MP', colorama.Fore.RESET)
    #pos
    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        if value.lower() in data.OS_phone:
            self._pos = value
        else:
            print(colorama.Fore.RED,'OS not established', colorama.Fore.RESET)
    #chargingport
    @property
    def chargingport(self):
        return self._chargingport
    @chargingport.setter
    def chargingport(self, value):
        if value.lower() in data.phone_port_types:
            self._chargingport = value
        else:
            print(colorama.Fore.RED,'unknown port type', colorama.Fore.RESET)
    #psscreensize
    @property
    def pscreensize(self):
        return self._pscreensize
    @pscreensize.setter
    def pscreensize(self, value):
        if len(value) > 1:
            self._pscreensize = value
        else:
            print(colorama.Fore.RED, 'enter size in the given format', colorama.Fore.RESET)
# ----------------------------------------------------------

if __name__ == '__main__':
    print('not the main file')




