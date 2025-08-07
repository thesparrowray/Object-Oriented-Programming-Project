import json
from operator import index
import data
import  OOP
import colorama
import re
import math
temp_cart = []



# --------------------- product json functions -----------------------------
def write_json_products(x):
    with open("c:\\rafiei\\products.json", 'w') as json_file:
        json.dump(x, json_file, indent=4)
# laptop
def write_json_laptop_stock(data):
    with open("c:\\rafiei\\laptop_stock.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_laptop_stock():
    try:
        with open("c:\\rafiei\\laptop_stock.json", 'r') as json_file:
            laptop_stock = json.load(json_file)
        return laptop_stock
    except Exception as err:
        print(err)
        return []
# camera
def write_json_camera_stock(data):
    with open("c:\\rafiei\\camera_stock.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_camera_stock():
    try:
        with open("c:\\rafiei\\camera_stock.json", 'r') as json_file:
            camera_stock = json.load(json_file)
        return camera_stock
    except Exception as err:
        print(err)
        return []
# phone
def write_json_phone_stock(data):
    with open("c:\\rafiei\\phone_stock.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_phone_stock():
    try:
        with open("c:\\rafiei\\phone_stock.json", 'r') as json_file:
            phone_stock = json.load(json_file)
        return phone_stock
    except Exception as err:
        print(err)
        return []

# ---------------------- person json functions ------------------------------
# employee
def write_json_employees(data):
    with open("c:\\rafiei\\employees.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_employees():
    try:
        with open("c:\\rafiei\\employees.json", 'r') as json_file:
            employees = json.load(json_file)
        return employees
    except Exception as err:
        print(err)
        return []
# admin
def write_json_admin(data):
    with open("c:\\rafiei\\admin.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_admin():
    try:
        with open("c:\\rafiei\\admin.json", 'r') as json_file:
            admin = json.load(json_file)
        return admin
    except Exception as err:
        print(err)
        return []

# user/customer
def write_json_customer(data):
    with open("c:\\rafiei\\customer.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_customer():
    try:
        with open("c:\\rafiei\\customer.json", 'r') as json_file:
            customer = json.load(json_file)
        return customer
    except Exception as err:
        return []

def write_json_customer_liked_items(data):
    with open("c:\\rafiei\\c_liked_items.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_customer_liked_items():
    try:
        with open("c:\\rafiei\\c_liked_items.json", 'r') as json_file:
            liked_items = json.load(json_file)
        return liked_items
    except Exception as err:
        return []

def write_json_customer_cart(data):
    with open("c:\\rafiei\\customer_cart.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_customer_cart():
    try:
        with open("c:\\rafiei\\customer_cart.json", 'r') as json_file:
            cart = json.load(json_file)
        return cart
    except Exception as err:
        return []

# ----------------------- data json functions ------------------------------
def read_json_prov_city():
    try:
        with open("c:\\rafiei\\prov_city.json", 'r') as json_file:
            prov_city = json.load(json_file)
        return prov_city
    except Exception as err:
        print(err)
        return []

def read_json_colors():
    try:
        with open("c:\\rafiei\\colors.json", 'r') as json_file:
            colors = json.load(json_file)
        return colors
    except Exception as err:
        print(err)
        return []

# ---------------------------- product -------------------------------------
def add_product_laptop():
    item = OOP.Laptop()
    while True:
        item.code = required_input('\tlaptop code (4 digits): ')
        laptop_data = read_json_laptop_stock()
        if any(i["code"] == item.code for i in laptop_data):
            print(colorama.Fore.RED, 'Error! Item already exists', colorama.Fore.RESET)
            continue
        else:
            break

    item.model = required_input('\tmodel: ')
    item.production_year = input('\tproduction year (xxxx): ')
    item.brand = required_input('\tbrand: ')
    item.price = required_input('\tprice: ')
    item.off = input('\toff (without %): ')
    item.stock = required_input('\tstock: ')
    item.warranty_time = required_input('\twarranty time (months): ')
    item.warranty_company = input('\twarranty company: ')
    item.weight = input('\tweight: ')
    item.size = input('\tsize (1x1x1): ')
    item.color = input('\tcolor: ')
    item.battery_life = input('\tbattery life: ')
    item.cpu = input('\tCPU: ')
    item.lram = input('\tRam (x GB): ')
    item.storage = input('\tstorage (x GB/TB, SSD/HHD): ')
    item.gpu = input('\tGPU: ')
    item.los = input('\tOS: ')
    item.webcam = input('\twebcam:')
    item.speaker = input('\tspeaker: ')
    item.lscreensize = input('\tscreen size (x inch): ')
    temp_laptop_json = {
        "code": item.code,
        "model": item.model,
        "production year": item.production_year,
        "brand": item.brand,
        "price": item.price,
        "off": item.off,
        "stock": item.stock,
        "warranty time": item.warranty_time,
        "warranty company": item.warranty_company,
        "weight": item.weight,
        "size": item.size,
        "color": item.color,
        "battery life": item.battery_life,
        "CPU": item.cpu,
        "RAM": item.lram,
        "storage": item.storage,
        "GPU": item.gpu,
        "OS": item.los,
        "webcam": item.webcam,
        "speaker": item.speaker,
        "screen size": item.lscreensize}
    laptop_data.append(temp_laptop_json)
    write_json_laptop_stock(laptop_data)
    print(colorama.Fore.GREEN, "Product successfully added!", colorama.Fore.RESET)

def add_product_phone():
    item = OOP.Phone()
    while True:
        item.code = required_input('\tphone code (4 digits): ')
        phone_data = read_json_phone_stock()
        if any(i["code"] == item.code for i in phone_data):
            print(colorama.Fore.RED, 'Error! Item already exists', colorama.Fore.RESET)
            continue
        else:
            break

    item.model = required_input('\tmodel: ')
    item.production_year = input('\tproduction year (xxxx): ')
    item.brand = required_input('\tbrand: ')
    item.price = required_input('\tprice (Tooman): ')
    item.off = input('\toff (without %): ')
    item.stock = required_input('\tstock: ')
    item.warranty_time = required_input('\twarranty time (in months): ')
    item.warranty_company = input('\twarranty company: ')
    item.weight = input('\tweight: ')
    item.size = input('\tsize (1x1x1): ')
    item.color = input('\tcolor: ')
    item.battery_life = input('\tbattery life: ')
    item.storage = input('\tstorage: ')
    item.sim = input('\tsim (1/2): ')
    item.frontcam = input('\tfront camera (x mp): ')
    item.backcam = input('\tback camera (x mp): ')
    item.pos = input('\tOS: ')
    item.chargingport = input('\tcharging port type: ')
    item.pscreensize = input('\tscreen size (1x1): ')
    temp_phone_json = {
        "code": item.code,
        "model": item.model,
        "production year": item.production_year,
        "brand": item.brand,
        "price": item.price,
        "off": item.off,
        "stock": item.stock,
        "warranty time": item.warranty_time,
        "warranty company": item.warranty_company,
        "weight": item.weight,
        "size": item.size,
        "color": item.color,
        "battery life": item.battery_life,
        "storage": item.storage,
        "sim": item.sim,
        "front camera": item.frontcam,
        "back camera": item.backcam,
        "OS": item.pos,
        "charging port": item.chargingport,
        "screen size": item.pscreensize}
    phone_data.append(temp_phone_json)
    write_json_phone_stock(phone_data)
    print(colorama.Fore.GREEN, "Product successfully added!", colorama.Fore.RESET)

def add_product_camera():
    item = OOP.Camera()
    while True:
        item.code = required_input('\tcamera code (4 digits): ')
        camera_data = read_json_camera_stock()
        if any(i["code"] == item.code for i in camera_data):
            print(colorama.Fore.RED, 'Error! Item already exists', colorama.Fore.RESET)
            continue
        else:
            break

    item.model = required_input('\tmodel: ')
    item.production_year = input('\tproduction year (xxxx): ')
    item.brand = required_input('\tbrand: ')
    item.price = required_input('\tprice: ')
    item.off = input('\toff (without %): ')
    item.stock = required_input('\tstock: ')
    item.warranty_time = required_input('\twarranty time (months): ')
    item.warranty_company = input('\twarranty company: ')
    item.weight = input('\tweight: ')
    item.size = input('\tsize (1x1x1): ')
    item.color = input('\tcolor: ')
    item.battery_life = input('\tbattery life: ')
    item.memory = input('\tmemory: ')
    item.shutter = input('\tshutter: ')
    item.lenz = input('\tlenz: ')
    item.ctype = input('\tcamera type (analogue/digital): ')
    item.touchsreen = input('\ttouch screen (yes/no): ')
    temp_camera_json = {
        "code": item.code,
        "model": item.model,
        "production year": item.production_year,
        "brand": item.brand,
        "price": item.price,
        "off": item.off,
        "stock": item.stock,
        "warranty time": item.warranty_time,
        "warranty company": item.warranty_company,
        "weight": item.weight,
        "size": item.size,
        "color": item.color,
        "battery life": item.battery_life,
        "memory": item.memory,
        "lenz": item.lenz,
        "shutter": item.shutter,
        "camera type": item.ctype,
        "touch screen": item.touchsreen}
    camera_data.append(temp_camera_json)
    write_json_camera_stock(camera_data)
    print(colorama.Fore.GREEN, "Product successfully added!", colorama.Fore.RESET)

def edit_item():
    while True:
        item_type = input(
            '\tL -> Laptop\n\tP -> Phone\n\tC -> Camera\n\tExit -> Exit\n\tChoose product type to be edited:')
        if item_type.lower() == 'l':
            laptop_stock = read_json_laptop_stock()
            if laptop_stock:
                for idx, item in enumerate(laptop_stock, start=1):
                    print(colorama.Fore.CYAN, f"\nLaptop #{idx}", colorama.Fore.RESET)
                    for key, value in item.items():
                        print(f"{key.capitalize():<14}: {value}")
                    print("-" * 30)
                edit_item_code = input('\tEnter item code: ')
                found = False
                for i in laptop_stock:
                    if edit_item_code == i["code"]:
                        found = True
                        print(colorama.Fore.GREEN, 'item found', i, colorama.Fore.RESET)
                        edit_part = input('\twhich attribute do you want to edit: ')
                        if edit_part in i.keys():
                            i[edit_part] = input('\tnew value: ')
                            print(colorama.Fore.GREEN, 'item updated', i, colorama.Fore.RESET)
                            write_json_laptop_stock(laptop_stock)
                        else:
                            print(colorama.Fore.RED, 'invalid key', colorama.Fore.RESET)
                        break
                if not found:
                    print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
            else:
                print('laptop stock file empty')
        elif item_type.lower() == 'p':
            phone_stock = read_json_phone_stock()
            if phone_stock:
                for idx, item in enumerate(phone_stock, start=1):
                    print(colorama.Fore.CYAN, f"\nphone #{idx}", colorama.Fore.RESET)
                    for key, value in item.items():
                        print(f"{key.capitalize():<14}: {value}")
                    print("-" * 30)
                edit_item_code = input('\tEnter item code: ')
                found = False
                for i in phone_stock:
                    if edit_item_code == i["code"]:
                        found = True
                        print(colorama.Fore.GREEN, 'item found', i, colorama.Fore.RESET)
                        edit_part = input('\twhich attribute do you want to edit: ')
                        if edit_part in i.keys():
                            i[edit_part] = input('\tnew value: ')
                            print(colorama.Fore.GREEN, 'item updated', i, colorama.Fore.RESET)
                            write_json_phone_stock(phone_stock)
                        else:
                            print(colorama.Fore.RED, 'invalid key', colorama.Fore.RESET)
                        break
                if not found:
                    print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
            else:
                print('phone stock file empty')

        elif item_type.lower() == 'c':
            camera_stock = read_json_camera_stock()
            if camera_stock:
                for idx, item in enumerate(camera_stock, start=1):
                    print(colorama.Fore.CYAN, f"\ncamera #{idx}", colorama.Fore.RESET)
                    for key, value in item.items():
                        print(f"{key.capitalize():<14}: {value}")
                    print("-" * 30)
                edit_item_code = input('\tEnter item code: ')
                found = False
                for i in camera_stock:
                    if edit_item_code == i["code"]:
                        found = True
                        print(colorama.Fore.GREEN, 'item found', i, colorama.Fore.RESET)
                        edit_part = input('\twhich attribute do you want to edit: ')
                        if edit_part in i.keys():
                            i[edit_part] = input('\tnew value: ')
                            print(colorama.Fore.GREEN, 'item updated', i, colorama.Fore.RESET)
                            write_json_camera_stock(camera_stock)
                        else:
                            print(colorama.Fore.RED, 'invalid key', colorama.Fore.RESET)
                        break
                if not found:
                    print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
            else:
                print('camera stock file empty')
        elif item_type.lower() == 'exit':
            break
        else:
            print('wrong input')

def delete_item():
    while True:
        item_type = input(
            '\tL -> Laptop\n\tP -> Phone\n\tC -> Camera\n\tExit -> Exit\n\tChoose product type to be deleted:')
        if item_type.lower() == 'l':
            laptop_stock = read_json_laptop_stock()
            if laptop_stock:
                for idx, item in enumerate(laptop_stock, start=1):
                    print(colorama.Fore.CYAN, f"\nLaptop #{idx}", colorama.Fore.RESET)
                    for key, value in item.items():
                        print(f"{key.capitalize():<14}: {value}")
                    print("-" * 30)
                delete_item_code = input('\tEnter item code: ')
                found = False
                for i in laptop_stock:
                    if delete_item_code == i["code"]:
                        found = True
                        print(colorama.Fore.GREEN, 'item found', i, colorama.Fore.RESET)
                        delete_item_confirmation = input(f'\tare you sure you want to delete item? yes/no')
                        if delete_item_confirmation.lower() == 'yes':
                            laptop_stock.remove(i)
                            print(colorama.Fore.GREEN, 'item deleted successfully', colorama.Fore.RESET)
                            write_json_laptop_stock(laptop_stock)
                        elif delete_item_confirmation.lower() == 'no':
                            print(colorama.Fore.YELLOW, 'no changes were made', colorama.Fore.RESET)
                        else:
                            print(colorama.Fore.RED, ' answer with yes/no', colorama.Fore.RESET)
                        break
                if not found:
                    print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
            else:
                print('laptop stock file empty')
        elif item_type.lower() == 'p':
            phone_stock = read_json_phone_stock()
            if phone_stock:
                for idx, item in enumerate(phone_stock, start=1):
                    print(colorama.Fore.CYAN, f"\nphone #{idx}", colorama.Fore.RESET)
                    for key, value in item.items():
                        print(f"{key.capitalize():<14}: {value}")
                    print("-" * 30)
                delete_item_code = input('\tEnter item code: ')
                found = False
                for i in phone_stock:
                    if delete_item_code == i["code"]:
                        found = True
                        print(colorama.Fore.GREEN, 'item found', i, colorama.Fore.RESET)
                        delete_item_confirmation = input(
                            f'\tare you sure you want to delete item? yes/no')
                        if delete_item_confirmation.lower() == 'yes':
                            phone_stock.remove(i)
                            print(colorama.Fore.GREEN, 'item deleted successfully', colorama.Fore.RESET)
                            write_json_phone_stock(phone_stock)
                        elif delete_item_confirmation.lower() == 'no':
                            print(colorama.Fore.YELLOW, 'no changes were made', colorama.Fore.RESET)
                        else:
                            print(colorama.Fore.RED, ' answer with yes/no', colorama.Fore.RESET)
                        break
                if not found:
                    print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
            else:
                print('phone stock file empty')

        elif item_type.lower() == 'c':
            camera_stock = read_json_camera_stock()
            if camera_stock:
                for idx, item in enumerate(camera_stock, start=1):
                    print(colorama.Fore.CYAN, f"\ncamera #{idx}", colorama.Fore.RESET)
                    for key, value in item.items():
                        print(f"{key.capitalize():<14}: {value}")
                    print("-" * 30)
                delete_item_code = input('\tEnter item code: ')
                found = False
                for i in camera_stock:
                    if delete_item_code == i["code"]:
                        found = True
                        print(colorama.Fore.GREEN, 'item found', i, colorama.Fore.RESET)
                        delete_item_confirmation = input(
                            f'\tare you sure you want to delete item? yes/no')
                        if delete_item_confirmation.lower() == 'yes':
                            camera_stock.remove(i)
                            print(colorama.Fore.GREEN, 'item deleted successfully', colorama.Fore.RESET)
                            write_json_camera_stock(camera_stock)
                        elif delete_item_confirmation.lower() == 'no':
                            print(colorama.Fore.YELLOW, 'no changes were made', colorama.Fore.RESET)
                        else:
                            print(colorama.Fore.RED, ' answer with yes/no', colorama.Fore.RESET)
                        break
                if not found:
                    print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
            else:
                print('camera stock file empty')
        elif item_type.lower() == 'exit':
            break

def show_items(session):
    while True:
        item_type = input(
            '\tL -> Laptop\n\tP -> Phone\n\tC -> Camera\n\tExit -> Exit\n\tChoose product type: ').lower().strip()
        if item_type == 'exit':
            break
        if item_type.lower() == 'l':
            items = read_json_laptop_stock()
        elif item_type.lower() == 'p':
            items = read_json_phone_stock()
        elif item_type.lower() == 'c':
            items = read_json_camera_stock()
        elif item_type.lower() == 'exit':
            return
        else:
            print(colorama.Fore.RED, 'invalid option', colorama.Fore.RESET)
            continue
        if not items:
            print(colorama.Fore.RED, 'no items available.', colorama.Fore.RESET)
            continue

        for i in items:
            print(colorama.Fore.CYAN, f'\t{i["model"]}, \n\t\tCode: {i["code"]}, \n\t\tBrand: {i["brand"]},'
                                      f' \n\t\tProduction year: {i["production year"]} \n\t\tPrice: {i["price"]}',
                  colorama.Fore.RESET)
            if int(i["off"]) > 0:
                new_price = off_calculator(i["price"], i["off"])
                print(colorama.Fore.MAGENTA, f'\t\t{i["off"]}% OFF: {new_price}', colorama.Fore.RESET)
            print(colorama.Fore.YELLOW, '\t-----------------------------------------------', colorama.Fore.RESET)
        choose_code = input('\tEnter item code to view: ')
        if not choose_code:
            break
        found = False
        for j in items:
            if choose_code.strip() == j["code"]:
                found = True
                print(j)
                options = input('\t1: add to cart\t2: like item\t3: exit\n\tchoose: ')
                if options == '1':
                    customer_add_to_cart(j, session)
                elif options == '2':
                    customer_like_item()
                elif options == '3':
                    print(colorama.Fore.YELLOW, 'exiting...', colorama.Fore.RESET)
                    return
                else:
                    print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
                    break
        if not found:
            print(print(colorama.Fore.RED, 'invalid code', colorama.Fore.RESET))
# ----------------------------- admin --------------------------------------
def admin_check_access():
    choice = input('\tto log into admin panel write "yes": ')
    if choice.lower() != 'yes':
        print(colorama.Fore.YELLOW, "\tReturning to menu.", colorama.Fore.RESET)
        return
    while True:
        username = input('\tUsername: ')
        password = input('\tPassword: ')
        temp_admin = read_json_admin()
        if not temp_admin:
            print(colorama.Fore.RED, 'admin file empty!', colorama.Fore.RESET)
            break
        elif ' ' in username or ' ' in password or not username or not password:
            print(colorama.Fore.RED, '\tusername and password cannot contain spaces or be empty.', colorama.Fore.RESET)
        else:
            ind = -1
            found = False
            for i in range(len(temp_admin)):
                if temp_admin[i]['username'] == username and temp_admin[i]['password'] == password:
                    ind = i
                    found = True
                    print(colorama.Fore.CYAN, f"\twelcome {temp_admin[ind]['name']} {temp_admin[ind]['last name']}",
                          colorama.Fore.RESET)
                    all_admin_actions(ind)
                    return


            if not found:
                print(colorama.Fore.YELLOW, '\tusername/password not found', colorama.Fore.RESET)
                cont = input('\tdo you want to try again? yes/no: ').lower()
                if cont == 'yes':
                    continue
                else:
                    print(colorama.Fore.CYAN, '\tReturning to previous menu.', colorama.Fore.RESET)
                    break


def all_admin_actions(ind):
    temp_admin = read_json_admin()
    while True:
        for j in temp_admin[ind]["access"]:
            print(colorama.Fore.BLUE, f'\t{j}')
        print('\tExit', colorama.Fore.RESET)
        ask = input('\tChoose action: ')
        if ask.lower() == 'add item':
            item_type = input('\tL -> Laptop\n\tP -> Phone\n\tC -> Camera\n\tExit -> Exit\n\tChoose product type to be added:')
            if item_type.lower() == 'l':
                add_product_laptop()
            elif item_type.lower() == 'p':
                add_product_phone()
            elif item_type.lower() == 'c':
                add_product_camera()
            elif item_type.lower() == 'exit':
                break
            else:
                print('wrong input')

        elif ask.lower() == 'edit item':
            edit_item()
        elif ask.lower() == 'delete item':
            delete_item()

        elif ask.lower() == 'add employee':
            add_employee()

        elif ask.lower() == 'add admin':
            add_admin()

        elif ask.lower() == 'delete employee':
            delete_employee()

        elif ask.lower() == 'delete admin':
            delete_admin()

        elif ask.lower() == 'edit employee':
            edit_employee()
        elif ask.lower() == 'edit admin':
            edit_admin()
        elif ask.lower() == 'edit personal info':
            edit_admin_personal_info(ind)
        elif ask.lower() == 'exit':
            break
        else:
            print(colorama.Fore.RED, 'Error! choose from the menu', colorama.Fore.RESET)

def add_admin():
    admin = OOP.Admin
    while True:
        exists = False
        found = False
        admin_data = read_json_admin()
        employee_data = read_json_employees()
        admin.employment_id = input('\temployment id: ')
        for i in admin_data:
            if admin.employment_id == i["employment id"]:
                exists = True
                print('employee is already an admin!, to edit info, go to edit admin')
                return
        if not exists:
            for i in employee_data:
                if admin.employment_id == i["employment id"]:
                    found = True
                    print(colorama.Fore.GREEN, f'employee found!, {i}', colorama.Fore.RESET)
                    while True:
                        ask = input('\tset as admin? yes/no')
                        if ask.lower() == 'yes':
                            temp_access = []
                            admin.name = i["name"]
                            admin.lastname = i["last name"]
                            admin.role = i["role"]
                            admin.username = admin.employment_id[1:5]
                            admin.password = admin.employment_id[1:5] + admin.name
                            while True:
                                for j in data.access_list:
                                    print(f'{j} -> {data.access_list[j]}')
                                give_access = input('add access: ')
                                if give_access in data.access_list:
                                    temp_access.append(data.access_list[give_access])
                                else:
                                    print(colorama.Fore.RED, "invalid action", colorama.Fore.RESET)
                                cont = input('continue adding access? yes/no')
                                if cont.lower() == 'yes':
                                    continue
                                elif cont.lower() == 'no':
                                    break
                                else:
                                    print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
                            admin.access = temp_access
                            temp_admin_data = {
                                "employment id": admin.employment_id,
                                "name": admin.name,
                                "last name": admin.lastname,
                                "role": admin.role,
                                "username": admin.username,
                                "password": admin.password,
                                "access": admin.access
                            }
                            admin_data.append(temp_admin_data)
                            write_json_admin(admin_data)
                            print(colorama.Fore.GREEN, f'admin successfully added\n{temp_admin_data}',
                                  colorama.Fore.RESET)
                            return

                        elif ask.lower() == 'no':
                            return
                        else:
                            print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
            if not found:
                print(colorama.Fore.RED, 'no employee with this code exists', colorama.Fore.RESET)
                cont = input('\tdo you want to continue? yes/no')
                if cont.lower() == 'yes':
                    continue
                else:
                    return

def edit_admin():
    admin_data = read_json_admin()
    if admin_data:
        for idx, item in enumerate(admin_data):
            for key, value in item.items():
                print(f"{key.capitalize():<12}: {value}")
            print("-" * 30)
        while True:
            found = False
            edit_admin_code = input('\tenter admin employment id you want to edit:')
            for i in admin_data:
                if edit_admin_code == i["employment id"]:
                    print('admin found!', i)
                    found = True
                    ask = input('\tenter key to edit (cannot edit "employment id"): ')

                    if ask == "employment id":
                        print(colorama.Fore.RED, '"employment id" cannot be edited.', colorama.Fore.RESET)
                        break

                    elif ask in i.keys():
                        i[ask] = input(f'\tnew value for {ask}: ')
                        print(colorama.Fore.GREEN, 'item updated', i, colorama.Fore.RESET)
                        write_json_admin(admin_data)
                        cont = input('\tdo you want to continue? yes/no: ')
                        if cont.lower() == 'yes':
                            continue
                        elif cont.lower() == 'no':
                            break
                        else:
                            print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
                    else:
                        print(colorama.Fore.RED, 'no such key exists', colorama.Fore.RESET)
                        break

            if not found:
                print(colorama.Fore.RED, 'wrong employment id', colorama.Fore.RESET)
                cont = input('\tdo you want to continue? yes/no: ')
                if cont.lower() == 'yes':
                    continue
                elif cont.lower() == 'no':
                    break
                else:
                    print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)

def delete_admin():
    admin_data = read_json_admin()
    if admin_data:
        for idx, item in enumerate(admin_data):
            for key, value in item.items():
                print(f"{key.capitalize():<12}: {value}")
            print("-" * 30)
        while True:
            found = False
            delete_admin_code = input('\tenter admin employment id you want to delete:')
            for i in admin_data:
                if delete_admin_code == i["employment id"]:
                    print('admin found!', i)
                    found = True
                    ask = input(
                        f'\t are you sure you want to delete admin {delete_admin_code}: {i["name"]} {i["last name"]}? yes/no')
                    if ask.lower() == 'yes':
                        del i
                        write_json_admin(admin_data)
                        print(colorama.Fore.RESET, 'admin deleted successfully', colorama.Fore.RESET)
                        cont = input('\tdo you want to continue? yes/no: ')
                        if cont.lower() == 'yes':
                            continue
                        elif cont.lower() == 'no':
                            break
                        else:
                            print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
                    elif ask.lower() == 'n':
                        print(colorama.Fore.YELLOW, 'no changes were made', colorama.Fore.RESET)
                    else:
                        print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)

            if not found:
                print(colorama.Fore.RED, 'wrong employment id', colorama.Fore.RESET)
                cont = input('\tdo you want to continue? yes/no: ')
                if cont.lower() == 'yes':
                    continue
                elif cont.lower() == 'no':
                    break
                else:
                    print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)

def edit_admin_personal_info(ind):
    admin_data = read_json_admin()
    print(admin_data[ind])
    while True:
        ask = input('\tenter key to edit (cannot edit "employment id"): ')
        if ask == "employment id":
            print(colorama.Fore.RED, '"employment id" cannot be edited.', colorama.Fore.RESET)
            return

        elif ask in admin_data[ind].keys():
            admin_data[ind][ask] = input(f'\tnew value for {ask}: ')
            print(colorama.Fore.GREEN, 'item updated',admin_data[ind], colorama.Fore.RESET)
            write_json_admin(admin_data)
            cont = input('\tdo you want to continue? yes/no: ')
            if cont.lower() == 'yes':
                continue
            elif cont.lower() == 'no':
                return
            else:
                print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, 'no such key exists', colorama.Fore.RESET)
            cont = input('\tdo you want to continue? yes/no: ')
            if cont.lower() == 'yes':
                continue
            elif cont.lower() == 'no':
                return
            else:
                print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
# ----------------------------- employee --------------------------------------
def add_employee():
    employee = OOP.Employee()
    while True:
        emp_id = required_input('\temployment id: ')
        if len(emp_id) != 8:
            print(colorama.Fore.RED, 'employment id must have 8 digits', colorama.Fore.RESET)

        else:
            employee_data = read_json_employees()
            if any(i["employment id"] == emp_id for i in employee_data):
                print(colorama.Fore.RED, 'Error! employee already exists', colorama.Fore.RESET)
                break
            else:
                employee.employment_id = emp_id
                employee.name = required_input('\tname: ')
                employee.lastname = required_input('\tlast name: ')
                employee.national_id = required_input('\tnational id: ')
                employee.phonenumber = required_input('\tphone number: ')
                employee.empaddress = get_address()
                employee.insurance = input('\tinsurance (basic/premium): ')
                employee.username = employee.employment_id
                employee.password = employee.employment_id[0:5] + employee.name
                temp_offdays = []
                n = 0
                while n < 2:
                    offday = input('\toff day: ')
                    if offday in temp_offdays:
                        print(colorama.Fore.RED, f'{offday} already added', colorama.Fore.RESET)
                    elif len(offday) > 3:
                        temp_offdays.append(offday)
                        n += 1
                employee.offdays = temp_offdays
                employee.overtime_m = input('\tovertime: ')
                employee.salary = input('\tsalary: ')
                employee.role = input('\trole: ')
                temp_employee_data = {
                    "name": employee.name,
                    "last name": employee.lastname,
                    "national id": employee.national_id,
                    "employment id": employee.employment_id,
                    "phone number": employee.phonenumber,
                    "address": employee.empaddress,
                    "insurance": employee.insurance,
                    "off days": employee.offdays,
                    "overtime": employee.overtime_m,
                    "salary": employee.salary,
                    "role": employee.role,
                    "access": employee.access,
                    "username": employee.username,
                    "password": employee.password
                }
                employee_data.append(temp_employee_data)
                write_json_employees(employee_data)
                print(colorama.Fore.GREEN, 'employee successfully added', colorama.Fore.RESET)
                break

def edit_employee():
    employee_data = read_json_employees()
    for idx, item in enumerate(employee_data):
        for key, value in item.items():
            print(f"{key.capitalize():<14}: {value}")
        print("-" * 30)
        edit_employee_code = input('\tenter employee employment id you want to edit:')
        for i in employee_data:
            if edit_employee_code == i["employment id"]:
                found = True
                print('employee found!', i)
                ask = input('\tenter key to edit (cannot edit "employment id"): ')

                if ask == "employment id":
                    print(colorama.Fore.RED, '"employment id" cannot be edited.', colorama.Fore.RESET)
                    break

                elif ask in i.keys():
                    i[ask] = input(f'\tnew value for {ask}: ')
                    print(colorama.Fore.GREEN, 'item updated', i, colorama.Fore.RESET)
                    write_json_employees(employee_data)
                    cont = input('\tdo you want to continue? yes/no: ')
                    if cont.lower() == 'yes':
                        continue
                    elif cont.lower() == 'no':
                        return
                    else:
                        print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
                else:
                    print(colorama.Fore.RED, 'no such key exists', colorama.Fore.RESET)
                    break

        if not found:
            print(colorama.Fore.RED, 'wrong employment id', colorama.Fore.RESET)
            cont = input('\tdo you want to continue? yes/no: ')
            if cont.lower() == 'yes':
                continue
            elif cont.lower() == 'no':
                should_continue = False
                break
            else:
                print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)

def delete_employee():
    employee_data = read_json_employees()
    for idx, item in enumerate(employee_data):
        for key, value in item.items():
            print(f"{key.capitalize():<14}: {value}")
        print("-" * 30)
    while True:
        found = False
        delete_employee_code = input('\tenter employee employment id you want to delete:')
        for i in employee_data:
            if delete_employee_code == i["employment id"]:
                print('employee found!', i)
                found = True
                ask = input(
                    f'\t are you sure you want to delete employee {delete_employee_code}: {i["name"]} {i["last name"]}? yes/no')
                if ask.lower() == 'yes':
                    del i
                    write_json_employees(employee_data)
                    print(colorama.Fore.RESET, 'employee deleted successfully', colorama.Fore.RESET)
                    cont = input('\tdo you want to continue? yes/no: ')
                    if cont.lower() == 'yes':
                        continue
                    elif cont.lower() == 'no':
                        break
                    else:
                        print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
                elif ask.lower() == 'n':
                    print(colorama.Fore.YELLOW, 'no changes were made', colorama.Fore.RESET)
                else:
                    print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)

        if not found:
            print(colorama.Fore.RED, 'wrong employment id', colorama.Fore.RESET)
            cont = input('\tdo you want to continue? yes/no: ')
            if cont.lower() == 'yes':
                continue
            elif cont.lower() == 'no':
                should_continue = False
                break
            else:
                print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)

# ------------------------- employee functions ----------------------------
def employee_log_in():
    choice = input('\tto enter employee panel write "yes": ')
    if choice.lower() != 'y':
        print(colorama.Fore.YELLOW, "\tReturning to menu.", colorama.Fore.RESET)
        return
    while True:
        username = input('\tUsername: ')
        password = input('\tPassword: ')
        temp_employee = read_json_employees()
        if not temp_employee:
            print(colorama.Fore.RED, 'employees file empty!', colorama.Fore.RESET)
            break
        elif ' ' in username or ' ' in password or not username or not password:
            print(colorama.Fore.RED, '\tusername and password cannot contain spaces or be empty.', colorama.Fore.RESET)
            break
        else:
            ind = -1
            for i in range(len(temp_employee)):
                if temp_employee[i]['username'] == username and temp_employee[i]['password'] == password:
                    ind = i
                    print(colorama.Fore.CYAN, f"\twelcome {temp_employee[ind]['name']} {temp_employee[ind]['last name']}",
                          colorama.Fore.RESET)
                    all_employee_actions(ind)
                    return
            else:
                print(colorama.Fore.YELLOW, '\tusername/password not found', colorama.Fore.RESET)
                cont = input('\tdo you want to try again? yes/no: ').lower()
                if cont == 'yes':
                    continue
                else:
                    print(colorama.Fore.CYAN, '\tReturning to previous menu.', colorama.Fore.RESET)
                    break

def all_employee_actions(ind):
    employee_data = read_json_employees()
    while True:
        for j in OOP.Employee.access:
            print(colorama.Fore.BLUE, f'\t{j} -> {OOP.Employee.access[j]}')
        print('\tExit', colorama.Fore.RESET)
        ask = input('\tChoose action: ')
        if ask == '1':
            employee_see_personal_info(ind, employee_data)
        elif ask == '2':
            employee_edit_personal_info(ind, employee_data)
        elif ask == '3':
            print('option unavailable')
        elif ask.lower() == 'exit':
            break
        else:
            print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
def employee_see_personal_info(ind, employee_data):
    print(employee_data[ind])

def employee_edit_personal_info(ind, employee_data):
    employee_see_personal_info(ind, employee_data)
    while True:
        ask = input('\tenter key to edit (cannot edit "employment id"): ')
        if ask == "employment id":
            print(colorama.Fore.RED, '"employment id" cannot be edited.', colorama.Fore.RESET)
            break
        elif ask in employee_data[ind]:
            employee_data[ind][ask] = input(f'\tnew value for {ask}: ')
            print(colorama.Fore.GREEN, 'item updated', employee_data[ind], colorama.Fore.RESET)
            write_json_employees(employee_data)
            cont = input('\tdo you want to continue? yes/no: ')
            if cont.lower() == 'yes':
                continue
            elif cont.lower() == 'no':
                break
            else:
                print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, 'no such key exists', colorama.Fore.RESET)
            break

def employee_calculate_salary():
    pass

# ------------------------- customer functions ----------------------------
def customer_sign_up():
    choice = input('\twrite "yes" to sign up: ')
    if choice.lower != 'yes':
        print(colorama.Fore.YELLOW, "\tSignup cancelled. Returning to menu.", colorama.Fore.RESET)
        return
    customer_data = read_json_customer()
    customer = OOP.Customer()
    customer.name = required_input('\tname: ')
    customer.lastname = required_input('\tlast name: ')
    customer.phonenumber = required_input('\tphone number: ')
    customer.address = get_address()
    pcode = required_input('\tpostal code: ')
    if pcode.isdigit() and len(pcode) == 10:
        customer.postal_code = pcode
    customer.email = email_checker()
    customer.username = customer_username()
    customer.password = customer_password()
    temp_customer = {
        "name": customer.name,
        "last name": customer.lastname,
        "phone number": customer.phonenumber,
        "address": customer.address,
        "postal code": customer.postal_code,
        "email": customer.email,
        "username": customer.username,
        "password": customer.password
    }
    customer_data.append(temp_customer)
    write_json_customer(customer_data)
    print(colorama.Fore.GREEN, "account created successfully", colorama.Fore.RESET)

def customer_log_in(session):
    choice = input('\tto enter customer panel write "yes": ')
    if choice.lower() != 'yes':
        print(colorama.Fore.YELLOW, "\tReturning to menu.", colorama.Fore.RESET)
        return
    while True:
        user = input('\tusername: ')
        password = input('\tpassword: ')
        if ' ' in user or ' ' in password or not user or not password:
            print(colorama.Fore.RED, '\tusername and password cannot contain spaces or be empty', colorama.Fore.RESET)
            return None
        customer_data = read_json_customer()
        if not customer_data:
            print(colorama.Fore.RED, 'customer file empty!', colorama.Fore.RESET)
            return None
        ind = -1
        for i in range(len(customer_data)):
            if customer_data[i]['username'] == user and customer_data[i]['password'] == password:
                ind = i
                print(colorama.Fore.CYAN, f"\twelcome {customer_data[ind]['name']} {customer_data[ind]['last name']}",
                      colorama.Fore.RESET)
                session['logged_in'] = True
                session['user_index'] = ind
                session['username'] = user
                return ind
        print(colorama.Fore.RED, '\tusername/password not found', colorama.Fore.RESET)
        cont = input('\tdo you want to try again? yes/no: ').lower()
        if cont == 'yes':
            continue
        else:
            print(colorama.Fore.CYAN, '\treturning to previous menu', colorama.Fore.RESET)
            return None



def all_customer_actions(ind, session):
    customer_data = read_json_customer()
    while True:
        for j in OOP.Customer.access:
            print(colorama.Fore.BLUE, f'\t{j} -> {OOP.Customer.access[j]}')
        print('\tExit', colorama.Fore.RESET)
        ask = input('\tChoose action: ')
        if ask == '1':
            print(customer_data[ind])
        elif ask == '2':
            customer_edit_info(ind, customer_data)
        elif ask == '3':
            customer_liked_item_list(ind)
        elif ask == '4':
            if "cart" in customer_data[ind]:
                print(customer_data[ind].get("cart"))
            else:
                print('cart empty')
        elif ask == '5':
            show_items(session)
        elif ask.lower() == 'exit':
            break
        else:
            print('wrnog input')


def customer_username():
    customer_data = read_json_customer()
    while True:
        username = required_input('\tusername: ')
        if not username:
            print(colorama.Fore.RED, 'Username cannot be empty.', colorama.Fore.RESET)
            continue
        elif any(i["username"] == username for i in customer_data):
            print(colorama.Fore.RED, 'Username already exists.', colorama.Fore.RESET)
        elif len(username) < 4:
            print(colorama.Fore.RED, 'username must be at least 4 characters', colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN, 'Username is valid.', colorama.Fore.RESET)
            return username


def customer_password():
    while True:
        password = required_input('\tpassword: ')
        if len(password) < 8:
            print("password must be at least 8 characters")
        elif not re.search(r"[A-Za-z]", password):
            print("must include at least one letter")
        elif not re.search(r"\d", password):
            print("must include at least one digit")
        elif not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
            print("must include at least one symbol")
        elif ' ' in password:
            print("password cannot contain spaces")
        else:
            return password


def customer_edit_info(ind, customer_data):
    print(customer_data[ind])
    while True:
        ask = input('\tenter key to edit: ')
        if ask.lower() == "username":
            customer_data[ind]["username"] = customer_username()
            write_json_customer(customer_data)
            print(colorama.Fore.GREEN, 'username successfully updated', colorama.Fore.RESET)
        elif ask.lower() == "password":
            customer_data[ind]["password"] = customer_password()
            write_json_customer(customer_data)
            print(colorama.Fore.GREEN, 'password successfully updated', colorama.Fore.RESET)
        elif ask in customer_data[ind]:
            customer_data[ind][ask] = input(f'\tnew value for {ask}: ')
            print(colorama.Fore.GREEN, 'item updated', customer_data[ind], colorama.Fore.RESET)
            write_json_customer(customer_data)
            cont = input('\tdo you want to continue? yes/no: ')
            if cont.lower() == 'yes':
                continue
            elif cont.lower() == 'no':
                break
            else:
                print(colorama.Fore.RED, 'yes/no', colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, 'no such key exists', colorama.Fore.RESET)
            break
def customer_like_item():
    print('action unavailable')
def customer_liked_item_list(ind):
    print('action unavailable')


def customer_add_to_cart(item, session):
    if not session.get("logged_in"):
        print(colorama.Fore.YELLOW, "\tPlease log in to add items to your cart.", colorama.Fore.RESET)

        if not customer_log_in(session):
            temp_cart.append(item)
            print(colorama.Fore.MAGENTA, 'Item added to temporary cart. Log in from "go to cart" to save your items.',
                  colorama.Fore.RESET)

            while True:
                action = input('\t1: continue shopping\n\t2: go to cart\n\t3: go to menu\n\tchoose: ')
                if action.strip() == '1':
                    show_items(session)
                    return
                elif action.strip() == '2':
                    print(colorama.Fore.RED, "you must log in before accessing your cart", colorama.Fore.RESET)
                elif action.strip() == '3':
                    return
                else:
                    print(colorama.Fore.RED, 'invalid choice', colorama.Fore.RESET)
            return


    ind = session["user_index"]
    customer_data = read_json_customer()

    if "cart" not in customer_data[ind]:
        customer_data[ind]["cart"] = []

    customer_cart = customer_data[ind]["cart"]
    customer_cart.append(item)
    write_json_customer(customer_data)
    print(colorama.Fore.GREEN, 'Item added to your cart!', colorama.Fore.RESET)

    while True:
        action = input('\t1: continue shopping\n\t2: go to cart\n\t3: go to menu\n\tchoose: ')
        if action.strip() == '1':
            show_items(session)
            return
        elif action.strip() == '2':
            print(colorama.Fore.GREEN, f'\nCart contents:\n\t{customer_cart}', colorama.Fore.RESET)
            calculate_customer_cart(customer_cart)

            while True:
                action_2 = input('\t1: continue shopping\n\t2: delete cart\n\t3: delete item\n\t4: user panel\n\tchoose: ')
                if action_2.strip() == '1':
                    show_items(session)
                    return
                elif action_2.strip() == '2':
                    customer_data[ind]["cart"] = []
                    write_json_customer(customer_data)
                    print(colorama.Fore.GREEN, 'Cart deleted successfully', colorama.Fore.RESET)
                elif action_2.strip() == '3':
                    print(customer_data[ind]["cart"])
                    item_delete_from_cart = input('Enter item code to delete: ')
                    for i in customer_data[ind]["cart"]:
                        if isinstance(i, dict) and item_delete_from_cart == i.get("code"):
                            customer_data[ind]["cart"].remove(i)
                            write_json_customer(customer_data)
                            print(colorama.Fore.GREEN, 'Item removed', colorama.Fore.RESET)
                            break
                    else:
                        print(colorama.Fore.RED, 'Wrong code', colorama.Fore.RESET)
                elif action_2.strip() == '4':
                    all_customer_actions(ind, session)
                    return
                else:
                    print(colorama.Fore.RED, 'Invalid choice', colorama.Fore.RESET)
                    break

        elif action.strip() == '3':
            return
        else:
            print(colorama.Fore.RED, 'Invalid choice', colorama.Fore.RESET)


# def customer_add_to_cart(item):
#     if not session.get("logged_in"):
#         print(colorama.Fore.YELLOW + "\tPlease log in to add items to your cart." + colorama.Fore.RESET)
#         if not customer_log_in(session):
#             return
#         temp_cart.append(item)
#         print(colorama.Fore.MAGENTA, 'item added to temporary cart. log in from "go to cart" to save your items', colorama.Fore.RESET)
#         while True:
#             action = input('\t1: continue shopping\n\t2: go to cart\n\t3: go to menu\n\tchoose: ')
#             if action.strip() == '1':
#                 show_items()
#             elif action.strip() == '2':
#                 ind = customer_log_in()
#                 if ind is not None:
#                     customer_data = read_json_customer()
#                     if "cart" not in customer_data[ind]:
#                         customer_data[ind]["cart"] = []
#                     customer_cart = customer_data[ind]["cart"]
#                     customer_cart.extend(temp_cart)
#                     write_json_customer_cart(customer_data)
#                     print(customer_cart)
#                     calculate_customer_cart(customer_cart)
#                     action_2 = input(
#                         '\t1: continue shopping\n\t2: delete cart\n\t3: delete item\n\t4: user panel\n\tchoose: ')
#                     if action_2.strip() == '1':
#                         show_items()
#                     elif action_2.strip() == '2':
#                         customer_data[ind]["cart"] = []
#                         write_json_customer(customer_data)
#                         print(colorama.Fore.GREEN, 'cart deleted successfully', colorama.Fore.RESET)
#                     elif action_2.strip() == '3':
#                         print(customer_data[ind]["cart"])
#                         item_delete_from_cart = input('enter item code to delete: ')
#                         for i in customer_data[ind]["cart"]:
#                             if isinstance(i, dict) and item_delete_from_cart == i.get("code"):
#                                 customer_data[ind]["cart"].remove(i)
#                                 write_json_customer(customer_data)
#                                 print(colorama.Fore.GREEN, 'item removed', colorama.Fore.RESET)
#                                 break
#                         else:
#                             print(colorama.Fore.RED, 'wrong code', colorama.Fore.RESET)
#                     elif action_2.strip() == '4':
#                         all_customer_actions(ind)
#                 else:
#                     print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)

def customer_shopping_history():
    print('unavailable')
def customer_search_item(session):
    search_input = input('\titem to search: ')
    if not search_input:
        print(colorama.Fore.RED, 'search input cannot be empty', colorama.Fore.RESET)
        return
    else:
        read_item = []
        read_item += read_json_laptop_stock()
        read_item += read_json_phone_stock()
        read_item += read_json_camera_stock()
        matches = []
        for i in read_item:
            if search_input.lower() in i["model"].lower():
                matches.append(i)
        if matches:
            for item in matches:
                print(f"Model: {item['model']}, Code: {item['code']}, Brand: {item['brand']}, Price: {item['price']}")

            ask = input('\titem code: ').strip()
            for j in matches:
                if ask == j["code"]:
                    found = True
                    print(j)
                    options = input('\t1: add to cart\t2: like item\t3: exit\n\tchoose: ')
                    if options == '1':
                        customer_add_to_cart(j, session)
                    elif options == '2':
                        customer_like_item()
                    elif options == '3':
                        print(colorama.Fore.YELLOW, 'exiting...', colorama.Fore.RESET)
                        return
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
            if not found:
                print(colorama.Fore.RED, 'wrong code', colorama.Fore.RESET)
                return
        if not matches:
            print(colorama.Fore.RED, 'no matches found', colorama.Fore.RESET)
            return


def calculate_customer_cart(shopping_cart):
    total_price = 0
    total_off = 0
    for i in shopping_cart:
        if i["off"] == 0:
            total_price += int(i["price"])
        else:
            i["new price"] = off_calculator(i["price"], i["off"])
            total_price += int(i["new price"])
            total_off += (int(i["price"]) - int(i["new price"]))
    print(colorama.Fore.MAGENTA, f'\ttotal price: {total_price}\n\ttotal off: {total_off}', colorama.Fore.RESET)

# ------------------------- general functions -----------------------------
def get_address():
    address = {'Province': '', 'City': '', 'Address': '', 'NO': '', 'Unit': ''}
    temp_data = read_json_prov_city()

    while True:
        province = required_input('\tProvince (persian keyboard): ')
        if province in temp_data:
            address['Province'] = province
            break
        else:
            print(colorama.Fore.RED, '\tinvalid province', colorama.Fore.RESET)

    while True:
        city = required_input('\tCity: ')
        if city in temp_data[address['Province']]:
            address['City'] = city
            break
        else:
            print(colorama.Fore.RED, '\tinvalid city for the selected province', colorama.Fore.RESET)

    while True:
        adres = required_input('\tAddress: ')
        if len(adres.strip()) >= 8:
            address['Address'] = adres
            break
        else:
            print(colorama.Fore.RED, '\taddress too short (< 8)', colorama.Fore.RESET)

    while True:
        NO = required_input('\tNO: ')
        if NO.isdigit() and int(NO) > 0:
            address['NO'] = NO
            break
        else:
            print(colorama.Fore.RED, '\t>0', colorama.Fore.RESET)

    while True:
        Unit = required_input('\tUnit: ')
        if Unit.isdigit() and int(Unit) > 0:
            address['Unit'] = Unit
            break
        else:
            print(colorama.Fore.RED, '\t>0.', colorama.Fore.RESET)

    return address


def employee_address():
    print(get_address())

def webcam_info():
    webcam = {'Resolution': '',
              'Frame rate': '',
              'Type': '',
              'Privacy shutter': '',
              'IR support': ''}
    for i in webcam:
        print(f'\t{i[0]} -> {i}')
    print('\tE -> Exit')
    while True:
        ask = input('Choose: ')
        if ask.lower() == 'r':
            resolution = input('Webcam resolution: ')
            if len(resolution) >= 3:
                webcam['Resolution'] = resolution
            else:
                print('resolution too short')
        elif ask.lower() == 'f':
            framerate = input('Webcam frame rate: ')
            if len(framerate) > 3 and 'fps' in framerate:
                webcam['Frame rate'] = framerate
            else:
                print('write in format "x fps"')
        elif ask.lower() == 't':
            type = input('Type (built-in or external): ')
            if len(type) > 5:
                webcam['Type'] = type
            else:
                print('input too short <=5')
        elif ask.lower() == 'p':
            privacy_shutter = input('privacy shutter: yes/no')
            if privacy_shutter.lower() == 'yes' or privacy_shutter.lower() == 'no':
                webcam['Privacy shutter'] = privacy_shutter
            else:
                print('answer yes or no')
        elif ask.lower() == 'i':
            ir_support = input('IR support: yes/no')
            if ir_support.lower() == 'yes' or ir_support.lower() == 'no':
                webcam['IR support'] = ir_support
            else:
                print('answer yes or no')
        elif ask.lower() == 'e':
            print(colorama.Fore.CYAN, 'exiting....', colorama.Fore.RESET)
            break
        else:
            print('invalid input')
    return webcam

def email_checker():
    email_ad = input('\temail address').strip()
    if not email_ad:
        print(colorama.Fore.RED, 'field empty', colorama.Fore.RESET)
    else:
        if email_ad.count('@') == 1 and '.' in email_ad.split('@')[1]:
            local_part, domain_part = email_ad.split('@')

            pattern_local = r'^[a-zA-Z0-9._-]+$'
            if not re.match(pattern_local, local_part):
                print(colorama.Fore.RED, 'Invalid email username', colorama.Fore.RESET)
            else:
                domain_sections = domain_part.rsplit('.', 1)
                if len(domain_sections) != 2:
                    print(colorama.Fore.RED, 'Email address must contain a .', colorama.Fore.RESET)
                else:
                    domain_name, domain_ext = domain_sections
                    if domain_name.lower() in data.valid_email_domains and domain_ext.lower() in data.valid_email_endings:
                        print(colorama.Fore.GREEN, 'valid email address', colorama.Fore.RESET)
                        return email_ad
                    else:
                        print(colorama.Fore.RED, f'domain {domain_name} or extension {domain_ext} not valid',
                              colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, 'Email address must contain at least one @ and .', colorama.Fore.RESET)


def required_input(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print(colorama.Fore.RED, "This field is required and cannot be empty or just spaces.", colorama.Fore.RESET)
        elif value.isspace():
            print(colorama.Fore.RED, "This field cannot contain only spaces.", colorama.Fore.RESET)
        else:
            return value

def off_calculator(n, x):
    price = n
    off = x
    price_after_off = price - ((off*price)//100)
    return price_after_off


if __name__ == '__main__':
    print('not the main file')












