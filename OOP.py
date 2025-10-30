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
        self._name = 'Unknown'
        self._lastname = 'Unknown'
        self._phonenumber = 'Unknown'
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
            self._name = 'Unknown'

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
            self._lastname = 'Unknown'

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
            self._phonenumber = 'Unknown'

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
    def __init__(self):
        super().__init__()
        self._empaddress = 'Unknown'
        self._national_id = 'None'
        self._employment_id = 'None'
        self._salary  = 0
        self._overtime_m = 0
        self._insurance = 'Not defined'
        self._offdays = 'Not defined'
        self._role = 'Not defined'


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
            self._empaddress = 'Unknown'

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
        self._employment_id = int(value)


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
                self._overtime_m = 0
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
            self._insurance = 'basic'

    # off days
    @property
    def offdays(self):
        return self._offdays
    @offdays.setter
    def offdays(self, value):
        if len(value) >= 6:
            self._offdays = value
            print(colorama.Fore.GREEN, 'adding...', colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, 'off days must be 2 different days!', colorama.Fore.RESET)
            self._offdays = 'Unknown'
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
            self._role = 'Unknown'

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
        self._address = ['Unknown']
        self._postal_code = 'Unknown'
        self._email = 'Unknown'
        self._wallet = 0
        self._debt = 0




    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value):
        if value:
            self._address = value
        else:
            print(colorama.Fore.RED, 'address not set', colorama.Fore.RESET)
            self._address = 'Unknown'

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
            self._postal_code = 'Unknown'

    # email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value



#-----------------------------------------------------------
class Seller:
    def __init__(self):
        self._entity_name = 'Unknown'
        self._representative_name = 'Unknown'
        self._seller_rep_pnum = 'Unknown'
        self._seller_work_permit_num = 'Unknown'
        self._seller_address = ['Unknown']
        self._rating = 0
        self._other_contact_info = 'Unknown'
        self._username = 'Unknown'
        self._password = 'Unknown'
        self._product_exp = 'Unknown'

    @property
    def entity_name(self):
        return self._entity_name
    @entity_name.setter
    def entity_name(self, value):
        if value.isalnum() and len(value) >= 4:
            self._seller_address = value
        else:
            print(colorama.Fore.RED, 'seller title too short', colorama.Fore.RESET)

    @property
    def representative_name(self):
        return self._representative_name
    @representative_name.setter
    def representative_name(self, value):
        if len(value) >= 5:
            self._representative_name = value
        else:
            print(colorama.Fore.RED, 'name too  short', colorama.Fore.RESET)

    @property
    def seller_rep_pnum(self):
        return self._seller_rep_pnum
    @seller_rep_pnum.setter
    def seller_rep_pnum(self, value):
        if value.isdigit() and len(value) == 11:
            self._seller_rep_pnum = value
        else:
            print(colorama.Fore.RED, '11 digit phone number', colorama.Fore.RESET)

    @property
    def seller_work_permit_num(self):
        return self._seller_work_permit_num

    @seller_work_permit_num.setter
    def seller_work_permit_num(self, value):
        if value.isdigit():
            self._seller_work_permit_num = value
        else:
            print(colorama.Fore.RED, 'must be a number', colorama.Fore.RESET)

    @property
    def seller_address(self):
        return self._seller_address
    @seller_address.setter
    def seller_address(self, value):
        if value:
            self._seller_address = value
        else:
            print(colorama.Fore.RED, 'seller address not set', colorama.Fore.RESET)

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, value):
        if value.isdigit() and 0 <= value <= 5:
            self._rating = value
        else:
            print(colorama.Fore.RED, 'rating must be between 0 and 5', colorama.Fore.RESET)

    @property
    def other_contact_info(self):
        return self._other_contact_info
    @other_contact_info.setter
    def other_contact_info(self, value):
        self._other_contact_info = value

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

    @property
    def product_exp(self):
        return self._product_exp
    @product_exp.setter
    def product_exp(self, value):
        self._product_exp = value

# ----------------------------------------------------------
# ----------------------------------------------------------
class Item:
    def __init__(self):
        self._code = 'xxx0000'
        self._model = 'Unknown'
        self._brand = 'Unknown'
        self._price = 0
        self._off = 'None'
        self._stock = 0
        self._warranty_time = 'none'
        self._warranty_company = 'Unknown'
        self._customer_rating = 0
        self._weight = 'None'
        self._size = '0x0x0'
        self._color = 'Not defined'
        self._production_year = '0000'
        self._battery_life  = 'None'
        self._rating = 0
    #code
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, value):
        if len(value) >= 6:
            self._code = value
        else:
            print(colorama.Fore.RED, 'code must be 6 chars', colorama.Fore.RESET)
            self._code = 'xxx0000'
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
            self._model = 'Unknown'
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
            self._brand = 'Unknown'
    #price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        value = int(value)
        if value > 1000000:
            self._price = int(value)
        else:
            print(colorama.Fore.RED, 'value must be a number > 1,000,000', colorama.Fore.RESET)
            self._price = 0
    #off
    @property
    def off(self):
        return self._off
    @off.setter
    def off(self, value):
        if '%' in value:
            self._off = value.strip('%')
        else:
            self._off = value

    #stock
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, value):
        value = int(value)
        if value >= 0:
            self._stock = int(value)
        else:
            print(colorama.Fore.RED, 'stock must be a digit', colorama.Fore.RESET)
            self._stock = 0
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
            self._warranty_time = 'Unknown'

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
            self._warranty_company = 'Unknown'

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
            self._customer_rating = 0

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
            self._weight = 'Unknown'

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
            self._size = 'Unknown'
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
            self._color = 'Unknown'

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
            self._production_year = 'Unknown'

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
            self._battery_life = 'Unknown'

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, value):
        if value.isdigit() and 0 <= value <= 5:
            self._rating = value
        else:
            print(colorama.Fore.RED, 'rating must be between 0 and 5', colorama.Fore.RESET)
            self._rating = 0

# -----------------------------------------------------------
class Laptop(Item):
    def __init__(self):
        super().__init__()
        self._cpu = 'Not defined'
        self._lram = 'Not defined'
        self._storage = 'Not defined'
        self._gpu = 'Not defined'
        self._los = 'Not defined'
        self._webcam = 'Not defined'
        self._speaker = 'Not defined'
        self._lscreensize = 'Not defined'

    #cpu
    @property
    def cpu(self):
        return self._cpu
    @cpu.setter
    def cpu(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED, 'cpu info must be a string', colorama.Fore.RESET)
            self._cpu = 'Unknown'
        if len(value.strip()) < 5:
            print(colorama.Fore.RED, 'len cpu info too short', colorama.Fore.RESET)
            self._cpu = 'Unknown'
        if not ('amd' in value.lower() or 'intel' in value.lower() or 'apple' in value.lower()):
            print(colorama.Fore.RED, 'manufacturer not established', colorama.Fore.RESET)
            self._cpu = 'Unknown'
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
            self._lram = 'Unknown'
        value = value.strip().upper()
        if not value.endswith('GB'):
            print(colorama.Fore.RED, 'write in the format "x GB"', colorama.Fore.RESET)
            self._lram = 'Unknown'
        else:
            number_part = value[:-2].strip()
            if not number_part.isdigit():
                print(colorama.Fore.RED, 'must contain a number', colorama.Fore.RESET)
                self._lram = 'Unknown'
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
            self._storage = 'Unknown'
        if not ('SSD' in value.upper() or 'HHD' in value.upper()):
            print(colorama.Fore.RED,'storage must be specified SSD or HHD', colorama.Fore.RESET)
            self_storage = 'Unknown'
        if not ('GB' in value.upper() or 'TB' in value.upper()):
            print(colorama.Fore.RED,'specify storage size in GB or TB', colorama.Fore.RESET)
            self._storage = 'Unknown'
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
            self._gpu = 'Unknown'
        if not len(value) > 5:
            print(colorama.Fore.RED,'input > 5', colorama.Fore.RESET)
            self._gpu = 'Unknown'
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
            self._los = 'Unknown'

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
            self._webcam = 'Unknown'

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
            self._speaker = 'Unknown'

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
            self._lscreensize = 'Unknown'

# ----------------------------------------------------------
class Camera(Item):
    def __init__(self):
        super().__init__()
        self._memory = 'Not defined'
        self._lenz = 'Not defined'
        self._shutter = 'Not defined'
        self._ctype = 'Not defined'
        self._touchscreen = 'Not defined'

    #memory
    @property
    def memory(self):
        return self._memory
    @memory.setter
    def memory(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED,'memory input must be a string, x GB', colorama.Fore.RESET)
            self._memory = 'Unknown'
        if not (value.lower().endswith('GB') and int(value.strip('GB')) > 0):
            print(colorama.Fore.RED,'write in the format "x GB"', colorama.Fore.RESET)
            self._memory = 'Unknown'
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
            self._lenz = 'Unknown'
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
            self._shutter = 'Unknown'
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
            self._ctype = 'Unknown'

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
            self._touchscreen = 'Unknown'
# ----------------------------------------------------------
class Phone(Item):
    def __init__(self):
        super().__init__()
        self._storage = 'Not defined'
        self._sim = '1'
        self._frontcam = 'Not defined'
        self._backcam = 'Not defined'
        self._pos = 'Not defined'
        self._chargingport = 'Not defined'
        self._pscreensize = 'Not defined'

    #storage
    @property
    def storage(self):
        return self._storage
    @storage.setter
    def storage(self, value):
        if not isinstance(value, str):
            print(colorama.Fore.RED,'storage input must be a string, x GB', colorama.Fore.RESET)
            self._storage = 'Unknown'
        if not value.lower().endswith('gb'):
            print(colorama.Fore.RED,'write in the format "x GB"', colorama.Fore.RESET)
            self._storage = 'Unknown'
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
            self._sim = '1'
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
            self._frontcam = 'Unknown'
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
            self._backcam = 'Unknown'
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
            self._pos = 'Unknown'
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
            self._chargingport = 'Unknown'
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
            self._pscreensize = 'Unknown'
# ----------------------------------------------------------

if __name__ == '__main__':
    print('not the main file')




