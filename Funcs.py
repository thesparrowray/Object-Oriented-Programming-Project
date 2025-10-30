import json
import random
from random import choice


import data
import OOP
import colorama
import re

import database

temp_cart = []
from argon2 import PasswordHasher
from argon2 import exceptions
from argon2.exceptions import VerifyMismatchError
ph = PasswordHasher

import mongodb
from tabulate import tabulate


# --------------------- product json functions -----------------------------
# laptops
def write_json_laptop_pending(data):
    with open("c:\\rafiei\\laptop_pending.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_laptop_pending():
    try:
        with open("c:\\rafiei\\laptop_pending.json", 'r') as json_file:
            laptop_pending = json.load(json_file)
        return laptop_pending
    except Exception as err:
        print(err)
        return []
# camera
def write_json_camera_pending(data):
    with open("c:\\rafiei\\camera_pending.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_camera_pending():
    try:
        with open("c:\\rafiei\\camera_pending.json", 'r') as json_file:
            camera_pending = json.load(json_file)
        return camera_pending
    except Exception as err:
        print(err)
        return []
# phone
def write_json_phone_pending(data):
    with open("c:\\rafiei\\phone_pending.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_json_phone_pending():
    try:
        with open("c:\\rafiei\\phone_pending.json", 'r') as json_file:
            phone_pending = json.load(json_file)
        return phone_pending
    except Exception as err:
        print(err)
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
# --------------------------- products in table ----------------------------
# --------------------------------add
def add_product_to_table(conn):
   while True:
       item_type = input(
           '\tL -> Laptop\n\tP -> Phone\n\tC -> Camera\n\tE -> Exit\n\tChoose product type to be added:')
       if item_type.lower() == 'l':
           add_product_laptop(conn)
       elif item_type.lower() == 'p':
          add_product_phone(conn)
       elif item_type.lower() == 'c':
           add_product_camera(conn)
       elif item_type.lower() == 'e':
           break
       else:
           print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
##############################################################
def add_product_laptop(conn):
    item = OOP.Laptop()
    while True:
        try:
            cur = conn.cursor()
            cur.execute("SELECT laptop_code FROM laptop ORDER BY laptop_code DESC LIMIT 1")
            row = cur.fetchone()
            if row:
                last_number = int(row[0][3:])
                new_number = last_number + 1
            else:
                new_number = 1001
            item.code = 'LAP'+ str(new_number)
            item.model = required_input('\tmodel: ')
            item.production_year = input('\tproduction year (xxxx): ')
            item.brand = required_input('\tbrand: ')
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
            sql = ('''
                        insert into laptop(laptop_code, l_model, l_production_year, l_brand, l_warranty_time, l_warranty_company, 
                        l_weight, l_size, l_color, l_battery_life, l_cpu, l_ram, l_storage, l_gpu, 
                        l_os, l_webcam, l_speaker, l_screensize) 
                        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ''')
            values = (item.code, item.model, item.production_year, item.brand, item.warranty_time,
                      item.warranty_company, item.weight, item.size, item.color, item.battery_life,
                      item.cpu, item.lram, item.storage, item.gpu, item.los, item.webcam,
                      item.speaker, item.lscreensize)
            cur.execute(sql, values)
            conn.commit()
            print(colorama.Fore.GREEN, "Product successfully added!", colorama.Fore.RESET)
            ask = input('do you want to create an entry for this item in the repository?')
            if ask.lower() == 'yes':
                item_code = item.code
                add_to_stock_from_item_list(conn, item_code)
            else:
                break
        except Exception as err:
            conn.rollback()
            print(print(colorama.Fore.RED, f'Error adding product: {err}', colorama.Fore.RESET))

        again = input("Add another laptop? press y: ").strip().lower()
        if again != "y":
            break

def add_product_phone(conn):
    item = OOP.Phone()
    while True:
        try:
            cur = conn.cursor()
            cur.execute("SELECT phone_code FROM phone ORDER BY phone_code DESC LIMIT 1")
            row = cur.fetchone()
            if row:
                last_number = int(row[0][3:])
                new_number = last_number + 1
            else:
                new_number = 1001
            item.code = 'PHO' + str(new_number)
            item.model = required_input('\tmodel: ')
            item.production_year = input('\tproduction year (xxxx): ')
            item.brand = required_input('\tbrand: ')
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
            sql = ('''
                        insert into phone(phone_code, p_model, p_production_year, p_brand, p_warranty_time, p_warranty_company, 
                        p_weight, p_size, p_color, p_battery_life, p_storage, p_sim,
                         p_frontcam, p_backcam, p_os, p_chargingport, p_screensize) 
                        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''')
            values = (item.code, item.model, item.production_year, item.brand, item.warranty_time,
                      item.warranty_company, item.weight, item.size, item.color, item.battery_life,
                      item.storage, item.sim, item.frontcam, item.backcam,
                      item.pos, item.chargingport, item.pscreensize)
            cur.execute(sql, values)
            conn.commit()
            print(colorama.Fore.GREEN, "Product successfully added!", colorama.Fore.RESET)

            ask = input('do you want to create an entry for this item in the repository?')
            if ask.lower() == 'yes':
                item_code = item.code
                add_to_stock_from_item_list(conn, item_code)
            else:
                break

        except Exception as err:
            conn.rollback()
            print(colorama.Fore.RED, f'Error adding product: {err}', colorama.Fore.RESET)

        again = input("Add another phone? press y: ").strip().lower()
        if again != "y":
            break

def add_product_camera(conn):
    item = OOP.Camera()
    while True:
        try:
            cur = conn.cursor()
            cur.execute("SELECT camera_code FROM camera ORDER BY camera_code DESC LIMIT 1")
            row = cur.fetchone()
            if row:
                last_number = int(row[0][3:])
                new_number = last_number + 1
            else:
                new_number = 1001
            item.code = 'CAM' + str(new_number)
            item.model = required_input('\tmodel: ')
            item.production_year = input('\tproduction year (xxxx): ')
            item.brand = required_input('\tbrand: ')
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
            item.touchscreen = input('\ttouch screen (yes/no): ')
            sql = ('''
                        insert into camera(camera_code, c_model, c_production_year, c_brand, c_warranty_time, c_warranty_company, 
                        c_weight, c_size, c_color, c_battery_life, c_memory, c_lenz,
                         c_shutter, c_type, c_touchscreen) 
                        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''')
            values = (item.code, item.model, item.production_year, item.brand, item.warranty_time,
                      item.warranty_company, item.weight, item.size, item.color, item.battery_life,
                      item.memory, item.shutter, item.lenz, item.ctype,
                      item.touchscreen)
            cur.execute(sql, values)
            conn.commit()
            print(colorama.Fore.GREEN, "Product successfully added!", colorama.Fore.RESET)

            ask = input('do you want to create an entry for this item in the repository?')
            if ask.lower() == 'yes':
                item_code = item.code
                add_to_stock_from_item_list(conn, item_code)
            else:
                break

        except Exception as err:
            conn.rollback()
            print(colorama.Fore.RED, f'Error adding product: {err}', colorama.Fore.RESET)

        again = input("Add another camera? press y: ").strip().lower()
        if again != "y":
            break
# ---------------------------------edit
def edit_item_in_item_tb(conn):
    while True:
        item_type = input(
            '\t1 -> Laptop\n\t2 -> Phone\n\t3 -> Camera\n\tE -> Exit\n\tChoose product type to be edited:')
        if item_type == '1':
            cur = conn.cursor()
            cur.execute('SELECT 1 FROM laptop LIMIT 1')
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, "No laptops in table", colorama.Fore.RESET)
                break
            else:
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\tE -> exit\n\tchoose:')
                    if ask.strip() == '1':
                        cur.execute('select * from laptop')
                        laptops = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in laptops:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                                print('='*40)
                        edit_laptop_table(conn)
                    elif ask.strip() == '2':
                        edit_laptop_table(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
        elif item_type == '2':
            cur = conn.cursor()
            cur.execute('SELECT 1 FROM phone LIMIT 1')
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, 'no phones in table', colorama.Fore.RESET)
                break
            else:
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\tE -> exit\n\tchoose: ')
                    if ask.strip() == '1':
                        cur.execute('select * from phone')
                        phones = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in phones:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        edit_phone_table(conn)
                    elif ask.strip() == '2':
                        edit_phone_table(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)

        elif item_type == '3':
            cur = conn.cursor()
            cur.execute('SELECT 1 FROM camera LIMIT 1')
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, 'no cameras in table', colorama.Fore.RESET)
                break
            else:
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\tE -> exit\n\tchoose: ')
                    if ask.strip() == '1':
                        cur.execute('select * from camera')
                        cameras = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        row_dict = dict(zip(columns, cameras))
                        for col, val in row_dict.items():
                            print(f"{col}: {val}")
                        edit_camera_table(conn)
                    elif ask.strip() == '2':
                        edit_camera_table(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
        elif item_type.lower() == 'e':
            break
        else:
            print('wrong input')

###########################################################
def edit_laptop_table(conn):
    edit_item_code = input('\tEnter item code: ')
    cur = conn.cursor()
    cur.execute('select * from laptop where laptop_code = %s', (edit_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        fields = {
            "1": "l_model",
            "2": "l_brand",
            "3": "l_warranty_time",
            "4": "l_warranty_company",
            "5": "l_weight",
            "6": "l_size",
            "7": "l_color",
            "8": "l_production_year",
            "9": "l_battery_life",
            "10": "l_cpu",
            "11": "l_ram",
            "12": "l_storage",
            "13": "l_gpu",
            "14": "l_os",
            "15": "l_webcam",
            "16": "l_speaker",
            "17": "l_screensize"
        }
        for key, val in fields.items():
            print(f"\t{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print('attribute doesnt exist')
            return
        else:
            new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
            sql = f'update laptop set {fields[edit_part_num]} = %s where laptop_code = %s'
            try:
                cur.execute(sql, (new_value, edit_item_code))
                conn.commit()
                print(colorama.Fore.GREEN, '\t\titem updated', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error updating item: {err}', colorama.Fore.RESET)
                return
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM laptop WHERE laptop_code = %s", (edit_item_code,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
        return

def edit_phone_table(conn):
    cur = conn.cursor()
    edit_item_code = input('\tEnter item code: ')
    cur.execute('select * from phone where phone_code = %s', (edit_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        fields = {
            "1": "p_model",
            "2": "p_brand",
            "3": "p_warranty_time",
            "4": "p_warranty_company",
            "5": "p_weight",
            "6": "p_size",
            "7": "p_color",
            "8": "p_production_year",
            "9": "p_battery_life",
            "10": "p_storage",
            "11": "p_sim",
            "12": "p_frontcam",
            "13": "p_backcam",
            "14": "p_os",
            "15": "p_chargingport",
            "16": "p_screensize",
        }
        for key, val in fields.items():
            print(f"\t{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print('attribute doesnt exist')
            return
        else:
            new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
            sql = f'update phone set {fields[edit_part_num]} = %s where phone_code = %s'
            try:
                cur.execute(sql, (new_value, edit_item_code))
                conn.commit()
                print(colorama.Fore.GREEN, '\t\titem updated', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error updating item: {err}', colorama.Fore.RESET)
                return
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM phone WHERE phone_code = %s", (edit_item_code,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
        return

def edit_camera_table(conn):
    cur = conn.cursor()
    edit_item_code = input('\tEnter item code: ')
    cur.execute('select * from camera where camera_code = %s', (edit_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        fields = {
            "1": "c_model",
            "2": "c_brand",
            "3": "c_warranty_time",
            "4": "c_warranty_company",
            "5": "c_weight",
            "6": "c_size",
            "7": "c_color",
            "8": "c_production_year",
            "9": "c_battery_life",
            "10": "c_memory",
            "11": "c_lenz",
            "12": "c_shutter",
            "13": "c_type",
            "14": "c_touchscreen",
        }
        for key, val in fields.items():
            print(f"\t{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print('attribute doesnt exist')
            return
        else:
            new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
            sql = f'update camera set {fields[edit_part_num]} = %s where camera_code = %s'
            try:
                cur.execute(sql, (new_value, edit_item_code))
                conn.commit()
                print(colorama.Fore.GREEN, '\t\titem updated', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error updating item: {err}', colorama.Fore.RESET)
                return
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM camera WHERE camera_code = %s", (edit_item_code,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
        return

# -------------------------------delete
def delete_item_from_table(conn):
    while True:
        item_type = input(
            '\t1 -> Laptop\n\t2 -> Phone\n\t3 -> Camera\n\tE -> Exit\n\tChoose product type to be deleted:')
        if item_type == '1':
            cur = conn.cursor()
            cur.execute('SELECT 1 FROM laptop LIMIT 1')
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, "No laptops in table", colorama.Fore.RESET)
                continue
            else:
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from laptop')
                        laptops = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in laptops:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        delete_laptop_table(conn)
                    elif ask.strip() == '2':
                        delete_laptop_table(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
        elif item_type == '2':
            cur = conn.cursor()
            cur.execute('SELECT 1 FROM phone LIMIT 1')
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, 'no phones in table', colorama.Fore.RESET)
                break
            else:
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from phone')
                        phones = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in phones:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        delete_phone_table(conn)
                    elif ask.strip() == '2':
                        delete_phone_table(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)

        elif item_type == '3':
            cur = conn.cursor()
            cur.execute('SELECT 1 FROM camera LIMIT 1')
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, 'no cameras in table', colorama.Fore.RESET)
                break
            else:
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from camera')
                        cameras = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in cameras:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        delete_camera_table(conn)
                    elif ask.strip() == '2':
                        delete_camera_table(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
        elif item_type.lower() == 'e':
            break
        else:
            print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)

#########################################################################
def delete_laptop_table(conn):
    delete_item_code = input('\tEnter item code: ')
    cur = conn.cursor()
    cur.execute('select * from laptop where laptop_code = %s', (delete_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        ask = input('\tdelete item? this  will also remove all related records on stock table. press y')
        if ask.lower() == 'y':
            try:
                cur.execute('delete from laptop where laptop_code = %s', (delete_item_code, ))
                conn.commit()
                print(colorama.Fore.GREEN, '\t\titem deleted successfully', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error deleting item: {err}', colorama.Fore.RESET)
                return
        else:
            print(colorama.Fore.YELLOW, 'delete cancelled', colorama.Fore.RESET)
            return
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)


def delete_phone_table(conn):
    delete_item_code = input('\tEnter item code: ')
    cur = conn.cursor()
    cur.execute('select * from phone where phone_code = %s', (delete_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        ask = input('\tdelete item? this  will also remove all related records on stock table. press y')
        if ask.lower() == 'y':
            try:
                cur.execute('delete from phone where phone_code = %s', (delete_item_code,))
                conn.commit()
                print(colorama.Fore.GREEN, '\t\titem deleted successfully', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error deleting item: {err}', colorama.Fore.RESET)
                return
        else:
            print(colorama.Fore.YELLOW, 'delete cancelled', colorama.Fore.RESET)
            return
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)



def delete_camera_table(conn):
    delete_item_code = input('\tEnter item code: ')
    cur = conn.cursor()
    cur.execute('select * from camera where camera_code = %s', (delete_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        ask = input('\tdelete item? this  will also remove all related records on stock table. press y')
        if ask.lower() == 'y':
            try:
                cur.execute('delete from camera where camera_code = %s', (delete_item_code,))
                conn.commit()
                print(colorama.Fore.GREEN, '\t\titem deleted successfully', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error deleting item: {err}', colorama.Fore.RESET)
                return

        else:
            print(colorama.Fore.YELLOW, 'delete cancelled', colorama.Fore.RESET)
            return
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)

# -----------------------------------------------------------------------
# --------------------------add product to stock ------------------------
# -----------------------------------------------------------------------
def add_to_stock(conn):
    cur = conn.cursor()
    item = OOP.Item()
    product_code = input('\tenter item code: ')
    if len(product_code) < 3:
        print("Invalid code")
        return
    else:
        if product_code[0:3] == 'LAP':
            cur.execute('select laptop_code from laptop where laptop_code = %s', (product_code, ))
            product = cur.fetchone()
            if product is not None:
                print(product)
                item.price = float(required_input('price: '))
                item.off = input('off (%): ')
                item.stock = int(required_input('stock number: '))
                item_seller_id = required_input('seller id: ')
                ask = input('add new item entery to repository? type yes')
                if ask.lower() == 'yes':
                    sql = 'insert into stock(laptop_code, item_type, seller_id, price, stock_off, stock) values(%s, %s, %s, %s, %s, %s)'
                    values = (product_code, 'Laptop', item_seller_id, item.price, item.off, item.stock)
                    try:
                        cur.execute(sql, values)
                        conn.commit()
                        print('item successfully added to repository')
                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
                else:
                    print(colorama.Fore.YELLOW, 'existing...', colorama.Fore.RESET)
                    return
            else:
                print(colorama.Fore.RED, 'item code invalid', colorama.Fore.RESET)

        elif product_code[0:3] == 'PHO':
            cur.execute('select phone_code from phone where phone_code = %s', (product_code, ))
            product = cur.fetchone()
            if product is not None:
                print(product)
                item.price = float(required_input('price: '))
                item.off = input('off: ')
                item.stock = int(required_input('stock number: '))
                item_seller_id = required_input('seller id: ')
                ask = input('add new item entery to repository? type yes')
                if ask.lower() == 'yes':
                    sql = 'insert into stock(phone_code, item_type, seller_id, price, stock_off, stock) values(%s, %s, %s, %s, %s, %s)'
                    values = (product_code, 'Phone', item_seller_id, item.price, item.off, item.stock)
                    try:
                        cur.execute(sql, values)
                        conn.commit()
                        print('item successfully added to repository')
                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
                else:
                    print(colorama.Fore.YELLOW, 'existing...', colorama.Fore.RESET)
                    return
            else:
                print(colorama.Fore.RED, 'item code invalid', colorama.Fore.RESET)
        elif product_code[0:3] == 'CAM':
            cur.execute('select camera_code from camera where camera_code = %s', (product_code, ))
            product = cur.fetchone()
            if product is not None:
                print(product)
                item.price = float(required_input('price: '))
                item.off = input('off: ')
                item.stock = int(required_input('stock number: '))
                item_seller_id = required_input('seller id: ')
                ask = input('add new item entery to repository? type yes ')
                if ask.lower() == 'yes':
                    sql = 'insert into stock(camera_code, item_type, seller_id, price, stock_off, stock) values(%s, %s, %s, %s, %s, %s)'
                    values = (product_code, 'Camera', item_seller_id, item.price, item.off, item.stock)
                    try:
                        cur.execute(sql, values)
                        conn.commit()
                        print('item successfully added to repository')
                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
                else:
                    print(colorama.Fore.YELLOW, 'existing...', colorama.Fore.RESET)
                    return
            else:
                print(colorama.Fore.RED, 'item code invalid', colorama.Fore.RESET)

#-----------------------------------add to stock from item list

def add_to_stock_from_item_list(conn, product_code):
    cur = conn.cursor()
    item = OOP.Item()
    if product_code[0:3] == 'LAP':
        cur.execute('select laptop_code from laptop where laptop_code = %s', (product_code, ))
        product = cur.fetchone()
        if product is not None:
            print(product)
            item.price = float(required_input('price: '))
            item.off = input('off (%): ')
            item.stock = int(required_input('stock number: '))
            item_seller_id = int(required_input('seller id: '))
            ask = input('add new item entery to repository? type yes ')
            if ask.lower() == 'yes':
                sql = 'insert into stock(laptop_code, item_type, seller_id, price, stock_off, stock) values(%s, %s, %s, %s, %s, %s)'
                values = (product_code, 'Laptop', item_seller_id, item.price, item.off, item.stock)
                try:
                    cur.execute(sql, values)
                    conn.commit()
                    print('item successfully added to repository')
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
            else:
                print(colorama.Fore.YELLOW, 'existing...', colorama.Fore.RESET)
                return
        else:
            print(colorama.Fore.RED, 'item code invalid', colorama.Fore.RESET)

    elif product_code[0:3] == 'PHO':
        cur.execute('select phone_code from phone where phone_code = %s', (product_code, ))
        product = cur.fetchone()
        if product is not None:
            print(product)
            item.price = float(required_input('\t\tprice: '))
            item.off = input('\t\toff: ')
            item.stock = int(required_input('\t\tstock number: '))
            item_seller_id = int(required_input('\t\tseller id: '))
            ask = input('\t\tadd new item entery to repository? type yes')
            if ask.lower() == 'yes':
                sql = 'insert into stock(phone_code, item_type, seller_id, price, stock_off, stock) values(%s, %s, %s, %s, %s, %s)'
                values = (product_code, 'Phone', item_seller_id, item.price, item.off, item.stock)
                try:
                    cur.execute(sql, values)
                    conn.commit()
                    print('\titem successfully added to repository')
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
            else:
                print(colorama.Fore.YELLOW, 'existing...', colorama.Fore.RESET)
                return
        else:
            print(colorama.Fore.RED, 'item code invalid', colorama.Fore.RESET)
    elif product_code[0:3] == 'CAM':
        cur.execute('select camera_code from camera where camera_code = %s', (product_code, ))
        product = cur.fetchone()
        if product is not None:
            print(product)
            item.price = float(required_input('price: '))
            item.off = input('off: ')
            item.stock = int(required_input('stock number: '))
            item_seller_id = int(required_input('seller id: '))
            ask = input('confirm adding new item entery to repository? press y')
            if ask.lower() == 'y':
                sql = 'insert into stock(camera_code, item_type, seller_id, price, stock_off, stock) values(%s, %s, %s, %s, %s, %s)'
                values = (product_code, 'Camera', item_seller_id, item.price, item.off, item.stock)
                try:
                    cur.execute(sql, values)
                    conn.commit()
                    print(colorama.Fore.GREEN, 'item successfully added to repository', colorama.Fore.RESET)
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
            else:
                print(colorama.Fore.YELLOW, 'existing...', colorama.Fore.RESET)
                return
        else:
            print(colorama.Fore.RED, 'item code invalid', colorama.Fore.RESET)
# -----------------------------edit
def edit_item_in_stock(conn):
    while True:
        cur = conn.cursor()
        cur.execute('SELECT 1 FROM stock LIMIT 1')
        row = cur.fetchone()
        if row is None:
            print(colorama.Fore.RED, 'no item in stock', colorama.Fore.RESET)
        else:
            item_type = input('''\t1 -> Laptop\n\t2 -> Phone\n\t3 -> Camera\n\tExit -> Exit
                    \n\tChoose product type to be edited:''')
            if item_type == '1':
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from stock where item_type = %s', ('Laptop', ))
                        laptops = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in laptops:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        edit_item_stock(conn)
                    elif ask.strip() == '2':
                        edit_item_stock(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
            elif item_type == '2':
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from stock where item_type = %s', ('Phone', ))
                        phones = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in phones:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        edit_item_stock(conn)
                    elif ask.strip() == '2':
                        edit_item_stock(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)

            elif item_type == '3':
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from stock where item_type = %s', ('Camera', ))
                        cameras = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in cameras:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        edit_item_stock(conn)
                    elif ask.strip() == '2':
                        edit_item_stock(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)

            elif item_type.lower() == 'exit':
                break
            else:
                print('wrong input')
################################################################3
def edit_item_stock(conn):
    edit_item_code = int(input('\tEnter item stock id: '))
    cur = conn.cursor()
    cur.execute('select * from stock where stock_id = %s', (edit_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        fields = {
            "1": "seller_id",
            "2": "price",
            "3": "stock_off",
            "4": "stock",
        }
        for key, val in fields.items():
            print(f"\t\n{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print('attribute doesnt exist')
            return
        else:
            if edit_part_num.strip() == '1':
                while True:
                    new_value = int(input(f'\t\tenter new value for {fields[edit_part_num]}: '))
                    cur.execute('select * from seller where seller_id = %s', (new_value, ))
                    seller = cur.fetchall()
                    if not seller:
                        print(colorama.Fore.RED, 'seller doesn\'t exist', colorama.Fore.RESET)
                        ask = input('\t1 -> retry \n\tE -> exit')
                        if ask.strip() == '1':
                            continue
                        else:
                            return
                    else:
                        print(seller)
                        ask = input('if this is your intended seller press Y to change the seller_id')
                        if ask.lower() == 'y':
                            sql = f'update stock set seller_id = %s where stock_id = %s'
                            try:
                                cur.execute(sql, (new_value, edit_item_code))
                                conn.commit()
                                print(colorama.Fore.GREEN, '\t\titem updated', colorama.Fore.RESET)
                            except Exception as err:
                                conn.rollback()
                                print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
                                break
                            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
                            cur.execute("SELECT * FROM stock WHERE stock_id = %s", (edit_item_code,))
                            row = cur.fetchone()
                            columns = [desc[0] for desc in cur.description]
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        else:
                            print(colorama.Fore.YELLOW, 'editing cancelled', colorama.Fore.RESET)
                            return
            elif edit_part_num in ['2', '3', '4']:
                new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
                if edit_part_num == '2':
                    new_value = float(new_value)
                else:
                    new_value = int(new_value)
                sql = f'update stock set {fields[edit_part_num]} = %s where stock_id = %s'
                try:
                    cur.execute(sql, (new_value, edit_item_code))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\titem updated', colorama.Fore.RESET)
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'Error adding to stock: {err}', colorama.Fore.RESET)
                    return
                print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
                cur.execute("SELECT * FROM stock WHERE stock_id = %s", (edit_item_code,))
                row = cur.fetchone()
                columns = [desc[0] for desc in cur.description]
                row_dict = dict(zip(columns, row))
                for col, val in row_dict.items():
                    print(f"{col}: {val}")
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
        return
#-------------------------------------------------delete
def delete_item_from_stock(conn):
    while True:
        cur = conn.cursor()
        cur.execute('SELECT 1 FROM stock LIMIT 1')
        row = cur.fetchone()
        if row is None:
            print(colorama.Fore.RED, 'no item in stock', colorama.Fore.RESET)
            break
        else:
            item_type = input('''\t1 -> Laptop\n\t2 -> Phone\n\t3 -> Camera\n\tE -> Exit
                    \n\tChoose product type to be deleted:''')
            if item_type == '1':
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from stock where item_type = %s', ('Laptop',))
                        laptops = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in laptops:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        delete_item_in_stock(conn)
                    elif ask.strip() == '2':
                        delete_item_in_stock(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)
            elif item_type == '2':
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from stock where item_type = %s', ('Phone',))
                        phones = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in phones:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        delete_item_in_stock(conn)
                    elif ask.strip() == '2':
                        delete_item_in_stock(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)

            elif item_type == '3':
                while True:
                    ask = input('\t1 -> show all items \n\t2 -> enter item code, \n\t E -> exit')
                    if ask.strip() == '1':
                        cur.execute('select * from stock where item_type = %s', ('Camera',))
                        cameras = cur.fetchall()
                        columns = [desc[0] for desc in cur.description]
                        for row in cameras:
                            row_dict = dict(zip(columns, row))
                            for col, val in row_dict.items():
                                print(f"{col}: {val}")
                        delete_item_in_stock(conn)
                    elif ask.strip() == '2':
                        delete_item_in_stock(conn)
                    elif ask.lower() == 'e':
                        break
                    else:
                        print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)

            elif item_type.lower() == 'e':
                break
            else:
                print('wrong input')

##############################################################
def delete_item_in_stock(conn):
    delete_item_code = input('\tEnter item stock id: ')
    cur = conn.cursor()
    cur.execute('select * from stock where stock_id = %s', (delete_item_code,))
    row = cur.fetchone()
    if row is not None:
        print(colorama.Fore.GREEN, 'item found', colorama.Fore.RESET)
        columns = [desc[0] for desc in cur.description]
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")

        ask = input('delete item from stock table? (this will not delete it from item specific table) press y')
        if ask.lower() == 'y':
            try:
                cur.execute('delete from stock where stock_id = %s', (delete_item_code, ))
                conn.commit()
                print(colorama.Fore.GREEN, '\t\titem deleted successfully', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error deleting item: {err}', colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED, 'item not found', colorama.Fore.RESET)
# --------------------------------------------------------
##########################################################
# ------------------------------show item--------------------------
def show_items(session, conn):
    cur = conn.cursor()
    cur.execute('SELECT 1 FROM stock LIMIT 1')
    if cur.fetchone() is None:
        print(colorama.Fore.RED, 'no item in stock', colorama.Fore.RESET)
        return

    queries = {
        "1": '''
                    select stock.stock_id, l_model, l_brand, l_warranty_time, l_warranty_company, l_weight, l_size, l_color,
                           l_production_year, l_battery_life, l_cpu, l_ram, l_storage, l_gpu, l_os, l_webcam, l_speaker,
                           l_screensize, stock.price, stock.stock_off, stock.stock, stock.rating,
                           seller.sel_store_company_name, seller.seller_address, seller.rating
                    from laptop
                    inner join stock 
                    on laptop.laptop_code = stock.laptop_code
                    inner join seller 
                    on stock.seller_id = seller.seller_id
                    where stock.state = 'approved by admin'
                ''',
        "2": '''
                    select stock.stock_id, p_model, p_brand, p_warranty_time, p_warranty_company, p_weight, p_size, p_color,
                           p_production_year, p_battery_life, p_storage, p_sim, p_frontcam, p_backcam, p_os, p_chargingport,
                           p_screensize, stock.price, stock.stock_off, stock.stock, stock.rating,
                           seller.sel_store_company_name, seller.seller_address, seller.rating
                    from phone
                    inner join stock 
                    on phone.phone_code = stock.phone_code
                    inner join seller 
                    on stock.seller_id = seller.seller_id
                    where stock.state = 'approved by admin'
                ''',
        "3": '''
                    select stock.stock_id, c_model, c_brand, c_warranty_time, c_warranty_company, c_weight, c_size, c_color,
                           c_production_year, c_battery_life, c_memory, c_lenz, c_shutter, c_type, c_touchscreen,
                           stock.price, stock.stock_off, stock.stock, stock.rating,
                           seller.sel_store_company_name, seller.seller_address, seller.rating
                    from camera
                    inner join stock 
                    on camera.camera_code = stock.camera_code
                    inner join seller 
                    on stock.seller_id = seller.seller_id
                    where stock.state = 'approved by admin'
                '''
    }

    while True:
        item_type = input(
            '\t1 -> Laptop\n\t2 -> Phone\n\t3 -> Camera\n\tE -> Exit\n\tChoose product type: '
        ).lower().strip()

        if item_type == 'e':
            break

        if item_type not in queries:
            print(colorama.Fore.RED, 'invalid option', colorama.Fore.RESET)
            continue

        cur.execute(queries[item_type])
        rows = cur.fetchall()
        if not rows:
            print(colorama.Fore.RED, 'no items of this type in stock', colorama.Fore.RESET)
            continue

        columns = [desc[0] for desc in cur.description]
        formatted_rows = []
        for row in rows:
            row_dict = dict(zip(columns, row))
            price = row_dict["price"]
            off = int(row_dict["stock_off"]) or 0
            final_price = price - (price * off / 100)
            row_dict["final_price"] = round(final_price, 2)
            formatted_rows.append(row_dict)

        columns.append("final_price")
        print(tabulate([[r[col] for col in columns] for r in formatted_rows],
                       headers=columns, tablefmt="fancy_grid"))
        item_code = input('stock id: ')
        if not item_code.isdigit():
            break
        else:
            item_code = int(item_code)

        action = input('\t1: add item to cart\n\t2: like item\n\t3: see comments\n\tE: exit\n\tchoose: ')
        if action.strip() == '1':
            customer_add_to_cart(conn, item_code, session)
        if action.strip() == '2':
            customer_like_item(conn, item_code, session)
        if action.strip() == '3':
            mongodb.item_comments(item_code)
        if action.lower() == 'e':
            break
        else:
            print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
            continue


# ----------------------------- admin --------------------------------------
def admin_check_access(conn):
    choice = input('\tto log into admin panel write "yes": ')
    if choice.lower() != 'yes':
        print(colorama.Fore.YELLOW, "\tReturning to menu.", colorama.Fore.RESET)
        return
    ph = PasswordHasher()
    while True:
        username = input('\tUsername: ')
        password = input('\tPassword: ')
        if ' ' in username or ' ' in password or not username or not password:
            print(colorama.Fore.RED, '\tusername and password cannot contain spaces or be empty.', colorama.Fore.RESET)
        else:
            cur = conn.cursor()
            cur.execute('select * from admin where ad_username = %s', (username, ))
            admin = cur.fetchone()
            if admin is None:
                print(colorama.Fore.RED, 'admin doesn\'t exist', colorama.Fore.RESET)
            else:
                try:
                    grant_access = ph.verify(admin[2], password)
                except VerifyMismatchError:
                    grant_access = False
                if grant_access:
                    cur.execute('select emp_name, emp_lname from employee where emp_id = %s', (admin[0],))
                    info_admin = cur.fetchone()
                    print(colorama.Fore.GREEN, f'welcome {info_admin[0]} {info_admin[1]}', colorama.Fore.RESET)
                    return admin
                else:
                    print(colorama.Fore.RED, 'incorrect password', colorama.Fore.RESET)

            # if not found:
            #     print(colorama.Fore.YELLOW, '\tusername/password not found', colorama.Fore.RESET)
            #     cont = input('\tdo you want to try again? yes/no: ').lower()
            #     if cont == 'yes':
            #         continue
            #     else:
            #         print(colorama.Fore.CYAN, '\tReturning to previous menu.', colorama.Fore.RESET)
            #         break

#-----------------------------------------------------------------------
def all_admin_actions(conn, identified_admin):
    while True:
        admin_access_type = identified_admin[4]
        for i in data.access_type[admin_access_type]:
            print(colorama.Fore.CYAN, f'\t{i}: {data.access_type[admin_access_type][i]}')
        print('\tE : Exit', colorama.Fore.RESET)
        ask = input('\tChoose action: ')
        if admin_access_type == 'main admin access':
            if ask.lower() == 'e':
                print('exiting...')
                break
            elif ask.strip() == '1':
                add_product_to_table(conn)
            elif ask.strip() == '2':
                edit_item_in_item_tb(conn)
            elif ask.strip() == '3':
                delete_item_from_table(conn)
            elif ask.strip() == '4':
                add_to_stock(conn)
            elif ask.strip() == '5':
                edit_item_in_stock(conn)
            elif ask.strip() == '6':
                delete_item_from_stock(conn)
            elif ask.strip() == '7':
                add_admin(conn, admin_access_type)
            elif ask.strip() == '8':
                edit_admin(conn, admin_access_type)
            elif ask.strip() == '9':
                delete_admin(conn, admin_access_type)
            elif ask.strip() == '10':
                add_employee(conn)
            elif ask.strip() == '11':
                edit_employee(conn)
            elif ask.strip() == '12':
                delete_employee(conn)
            elif ask.strip() == '13':
                see_seller_requests(conn)
            elif ask.strip() == '14':
                admin_review_pending(conn)
            elif ask.strip() == '15':
                admin_approve_stock_updates(conn, identified_admin[0])
            elif ask.strip() == '16':
                delete_seller(conn)
            elif ask.strip() == '17':
                see_admin_personal_info(conn, identified_admin[0])
            elif ask.strip() == '18':
                see_admin_personal_info(conn, identified_admin[0])
                edit_admin_personal_info(conn, identified_admin[0])
            elif ask.strip() == '19':
                ask = input('are you sure you want to delete onlineshop database? all data will be erased, press y')
                if ask.lower() == 'y':
                    cur = conn.cursor()
                    cur.execute('drop database onlineshop')
                    conn.commit()
                    print('database deleted')
            elif ask.strip() == '20':
                see_all_employees(conn)
            elif ask.strip() == '21':
                see_all_admins(conn)
            elif ask.strip() == '22':
                see_all_sellers(conn)
            elif ask.strip() == '23':
                see_all_customers(conn)
            elif ask.strip() == '24':
                see_all_orders(conn)
            else:
                print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
                break

        elif admin_access_type == 'full access':
            if ask.lower() == 'e':
                print('exiting...')
                break
            elif ask.strip() == '1':
                add_product_to_table(conn)
            elif ask.strip() == '2':
                edit_item_in_item_tb(conn)
            elif ask.strip() == '3':
                delete_item_from_table(conn)
            elif ask.strip() == '4':
                add_to_stock(conn)
            elif ask.strip() == '5':
                edit_item_in_stock(conn)
            elif ask.strip() == '6':
                delete_item_from_stock(conn)
            elif ask.strip() == '7':
                add_admin(conn, admin_access_type)
            elif ask.strip() == '8':
                edit_admin(conn, admin_access_type)
            elif ask.strip() == '9':
                delete_admin(conn, admin_access_type)
            elif ask.strip() == '10':
                add_employee(conn)
            elif ask.strip() == '11':
                edit_employee(conn)
            elif ask.strip() == '12':
                delete_employee(conn)
            elif ask.strip() == '13':
                see_seller_requests(conn)
            elif ask.strip() == '14':
                admin_review_pending(conn)
            elif ask.strip() == '15':
                admin_approve_stock_updates(conn, identified_admin[0])
            elif ask.strip() == '16':
                delete_seller(conn)
            elif ask.strip() == '17':
                see_admin_personal_info(conn, identified_admin[0])
            elif ask.strip() == '18':
                see_admin_personal_info(conn, identified_admin[0])
                edit_admin_personal_info(conn, identified_admin[0])
            else:
                print(colorama.Fore.RED, 'access not defined', colorama.Fore.RESET)


        elif admin_access_type == 'repository access':
            if ask.lower() == 'e':
                print('exiting...')
                break
            elif ask.strip() == '1':
                add_product_to_table(conn)
            elif ask.strip() == '2':
                edit_item_in_item_tb(conn)
            elif ask.strip() == '3':
                delete_item_from_table(conn)
            elif ask.strip() == '4':
                add_to_stock(conn)
            elif ask.strip() == '5':
                edit_item_in_stock(conn)
            elif ask.strip() == '6':
                delete_item_from_stock(conn)
            elif ask.strip() == '7':
                see_admin_personal_info(conn, identified_admin[0])
            elif ask.strip() == '8':
                see_admin_personal_info(conn, identified_admin[0])
                edit_admin_personal_info(conn, identified_admin[0])
            else:
                print(colorama.Fore.RED, 'access not defined', colorama.Fore.RESET)


        elif admin_access_type == 'HR access':
            if ask.lower() == 'e':
                print('exiting...')
                break
            elif ask.strip() == '1':
                add_admin(conn, admin_access_type)
            elif ask.strip() == '2':
                edit_admin(conn, admin_access_type)
            elif ask.strip() == '3':
                delete_admin(conn, admin_access_type)
            elif ask.strip() == '4':
                add_employee(conn)
            elif ask.strip() == '5':
                edit_employee(conn)
            elif ask.strip() == '6':
                delete_employee(conn)
            elif ask.strip() == '7':
                see_admin_personal_info(conn, identified_admin[0])
            elif ask.strip() == '8':
                see_admin_personal_info(conn, identified_admin[0])
                edit_admin_personal_info(conn, identified_admin[0])
            else:
                print(colorama.Fore.RED, 'access not defined', colorama.Fore.RESET)

        else:
            print(colorama.Fore.RED, 'Error! invalid access type', colorama.Fore.RESET)
            break
#########################################################################################
def add_admin(conn, admin_access_type):
    admin = OOP.Admin()
    cur = conn.cursor()
    while True:
        emp_input = input('\temployment id: ')
        if not emp_input.strip():
            print(colorama.Fore.RED, 'ID cannot be empty', colorama.Fore.RESET)
            break
        try:
            admin.employment_id = int(emp_input)
        except ValueError:
            print(colorama.Fore.RED, 'ID must be a number', colorama.Fore.RESET)
            continue
        cur.execute('select * from employee where emp_id = %s', (admin.employment_id, ))
        finding_employee = cur.fetchone()
        if finding_employee is None:
            print(colorama.Fore.RED, 'employee not found', colorama.Fore.RESET)
            continue
        else:
            cur.execute('select * from admin where emp_id = %s', (admin.employment_id, ))
            if cur.fetchone() is not None:
                print(colorama.Fore.GREEN, 'employee found!', colorama.Fore.RESET)
                print(f'employment id: {finding_employee[0]}, {finding_employee[1]} {finding_employee[2]}')
                print(colorama.Fore.YELLOW, 'employee is already an admin!, to edit info, go to edit admin', colorama.Fore.RESET)
                return
            else:
                print(colorama.Fore.GREEN, 'employee found!', colorama.Fore.RESET)
                print(f'employment id: {finding_employee[0]}, {finding_employee[1]} {finding_employee[2]}')
                while True:
                    ask = input('\tset as admin? yes/no')
                    if ask.lower() == 'yes':
                        admin.username = str(finding_employee[0])
                        admin.password = str(finding_employee[0])+ finding_employee[1]
                        admin.role = input('\t\tadmin role: ')
                        access_types = {"1": "main admin access", "2": "full access", "3": "repository access", "4": "HR access" }
                        for i in access_types:
                            print(f'\t\t{i}: {access_types[i]}')
                        admin.access = input('\t\tchoose access type: ')
                        if admin.access not in access_types:
                            print(colorama.Fore.RED, 'invalid access type')
                            continue
                        if admin.access == '1' and admin_access_type != 'main admin access':
                            print(colorama.Fore.RED, 'you cannot authorize a main admin')
                            return
                        sql = 'insert into admin(emp_id, ad_username, ad_password_hash, ad_role, ad_access_type) values(%s, %s, %s, %s, %s)'
                        values = (admin.employment_id, admin.username, admin.password, admin.role, admin.access)
                        try:
                            cur.execute(sql, values)
                            conn.commit()
                            print(colorama.Fore.GREEN, f'admin successfully added',colorama.Fore.RESET)
                            break
                        except Exception as err:
                            conn.rollback()
                            print(colorama.Fore.RED, f'Error adding admin: {err}', colorama.Fore.RESET)
                            return
                    else:
                        break


def edit_admin(conn, admin_access_type):
    cur = conn.cursor()
    while True:
        edit_admin_code = input('\tenter admin employment id you want to edit:')
        if not edit_admin_code.strip():
            print(colorama.Fore.RED, 'ID cannot be empty', colorama.Fore.RESET)
            break
        try:
            edit_admin_code = int(edit_admin_code)
        except ValueError:
            print(colorama.Fore.RED, 'ID must be a number', colorama.Fore.RESET)
            continue
        cur.execute('select * from admin where emp_id = %s', (edit_admin_code, ))
        row = cur.fetchone()
        if row is None:
            print(colorama.Fore.RED, '\t\twrong employment id or employee is not an admin', colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN, 'admin found!')
            cur.execute('''
            select employee.emp_name, employee.emp_lname, ad_role, ad_access_type
            from admin 
            inner join employee
            on admin.emp_id = employee.emp_id
            where admin.emp_id = %s
            ''', (edit_admin_code, ))
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, 'Error fetching admin info', colorama.Fore.RESET)
                continue
            else:
                columns = [desc[0] for desc in cur.description]
                row_dict = dict(zip(columns, row))
                print(colorama.Fore.GREEN, 'Admin data:', colorama.Fore.RESET)
                for col, val in row_dict.items():
                    print(f"{col}: {val}")
            fields = {
                "1": "ad_role",
                "2": "ad_access_type"
            }
            for key, val in fields.items():
                print(f"\t{key}. {val}")
            edit_part_num = input('\twhich attribute do you want to edit? (or E to exit): ')
            if edit_part_num not in fields:
                print('attribute doesnt exist')
                break
            elif edit_part_num.lower() == 'e':
                break
            else:
                new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
                if fields[edit_part_num] == 'ad_access_type' and new_value not in data.access_type:
                    print(colorama.Fore.RED, f'Invalid access type. Must be one of {data.access_type}', colorama.Fore.RESET)
                    continue
                if fields[edit_part_num] == 'ad_access_type' and new_value == 'main admin access' and admin_access_type != 'main admin access':
                    print(colorama.Fore.RED, 'You cannot authorize a main admin', colorama.Fore.RESET)
                    continue
                sql = f'update admin set {fields[edit_part_num]} = %s where emp_id = %s'
                try:
                    cur.execute(sql, (new_value, edit_admin_code))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\tadmin data updated', colorama.Fore.RESET)
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'Error updating admin: {err}', colorama.Fore.RESET)
                    continue
                print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
                cur.execute("SELECT ad_role, ad_access_type FROM admin WHERE emp_id = %s", (edit_admin_code,))
                row = cur.fetchone()
                columns = [desc[0] for desc in cur.description]
                row_dict = dict(zip(columns, row))
                for col, val in row_dict.items():
                    print(f"{col}: {val}")
                again = input('\tEdit another admin? (y/n): ')
                if again.lower() != 'y':
                    break


def delete_admin(conn, admin_access_type):
    cur = conn.cursor()
    while True:
        delete_admin_code = input('\tenter admin employment id you want to delete:')
        if not delete_admin_code.strip():
            print(colorama.Fore.RED, 'ID cannot be empty', colorama.Fore.RESET)
            break
        try:
            delete_admin_code = int(delete_admin_code)
        except ValueError:
            print(colorama.Fore.RED, 'ID must be a number', colorama.Fore.RESET)
            continue
        cur.execute('select * from admin where emp_id = %s', (delete_admin_code,))
        if cur.fetchone() is None:
            print(colorama.Fore.RED, '\t\twrong employment id or employee is not an admin', colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN, 'admin found!')
            cur.execute('''
                            select employee.emp_name, employee.emp_lname, ad_role, ad_access_type
                            from admin 
                            inner join employee
                            on admin.emp_id = employee.emp_id
                            where admin.emp_id = %s
                            ''', (delete_admin_code,))
            row = cur.fetchone()
            if row is None:
                print(colorama.Fore.RED, 'Error fetching admin info', colorama.Fore.RESET)
                continue
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
            ask = input('\t\tdelete admin? press y (this will not remove the employee)')
            if ask.lower() == 'y':
                if row[3] == 'main admin access' and admin_access_type != 'main admin access':
                    print(colorama.Fore.RED, 'error! you do not have this access', colorama.Fore.RESET)
                    continue
                else:
                    try:
                        cur.execute('delete from admin where emp_id = %s', (delete_admin_code,))
                        conn.commit()
                        print(colorama.Fore.RED, '\t\tadmin deleted successfully', colorama.Fore.RESET)
                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'Error deleting admin: {err}', colorama.Fore.RESET)
                    again = input('\tDelete another admin? (y/n): ')

                    if again.lower() != 'y':
                        break
            else:
                print(colorama.Fore.YELLOW, 'invalid input, no changes were made', colorama.Fore.RESET)
                break

def see_admin_personal_info(conn, identified_admin):
    cur = conn.cursor()
    cur.execute('''
    select admin.emp_id, employee.emp_name, employee.emp_lname, employee.emp_national_id,
    employee.emp_phone, employee.emp_address, ad_username, 
    ad_role, ad_access_type, employee.emp_salary, employee.emp_overtime, 
    employee.emp_insurance
    from admin
    inner join employee
    on admin.emp_id = employee.emp_id
    where admin.emp_id = %s
    ''', (identified_admin, ))
    row = cur.fetchone()
    columns = [desc[0] for desc in cur.description]
    if row:
        for col, val in zip(columns, row):
            print(f"{col}: {val}")
        return row
    else:
        print(colorama.Fore.RED, 'no data found', colorama.Fore.RESET)
        return None

def edit_admin_personal_info(conn, admin_data):
    cur = conn.cursor()
    while True:
        fields = {
            "1": "emp_name",
            "2": "emp_lname",
            "3": "emp_national_id",
            "4": "emp_address",
            "5": "ad_password",
            "6": "emp_overtime"
        }
        for key, val in fields.items():
            print(f"\t{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print(colorama.Fore.RED, 'attribute doesn’t exist', colorama.Fore.RESET)
            continue
        else:
            if fields[edit_part_num].startswith('emp'):
                new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
                sql = f'update employee set {fields[edit_part_num]} = %s where emp_id = %s'
                try:
                    cur.execute(sql, (new_value, admin_data))
                    conn.commit()
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'Error editing info: {err}', colorama.Fore.RESET)
                    continue
            elif fields[edit_part_num].startswith('ad'):
                if edit_part_num == '5':
                    new_value = customer_password()
                    sql = f'update admin set {fields[edit_part_num]} = %s where emp_id = %s'
                    try:
                        cur.execute(sql, (new_value, admin_data))
                        conn.commit()
                        print(colorama.Fore.GREEN, '\t\titem updated', colorama.Fore.RESET)

                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'Error editing info: {err}', colorama.Fore.RESET)
                        continue
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute('''
                select employee.emp_id, employee.emp_name, employee.emp_lname, employee.emp_national_id,
                employee.emp_phone, employee.emp_address, ad_username, 
                ad_role, ad_access_type, employee.emp_salary, employee.emp_overtime, 
                employee.emp_insurance
                from admin
                inner join employee
                on admin.emp_id = employee.emp_id
                where admin.emp_id = %s
                ''', (admin_data,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            for col, val in zip(columns, row):
                print(f"{col}: {val}")
            cont = input('\tdo you want to continue? press y: ')
            if cont.lower() == 'y':
                continue
            else:
                break
# ----------------------------- employee --------------------------------------
def add_employee(conn):
    employee = OOP.Employee()
    cur = conn.cursor()
    while True:
        employee.national_id = required_input('\tnational id: ')
        cur.execute('select * from employee where emp_national_id = %s', (employee.national_id, ))
        rows = cur.fetchone()
        if rows is not None:
            print(colorama.Fore.RED, 'person already an employee', colorama.Fore.RESET)
        else:
            employee.name = required_input('\tname: ')
            employee.lastname = required_input('\tlast name: ')
            employee.phonenumber = required_input('\tphone number: ')
            employee.empaddress = get_address()
            employee.role = input('\trole: ')
            employee.salary = input('\tdesignated salary: ')
            employee.insurance = input('\tinsurance (basic/premium): ')
            employee.username = str(employee.national_id)
            password = str(employee.national_id)[0:5] + employee.name
            ph = PasswordHasher()
            employee.password = ph.hash(password)
            employee.offdays = input('\toff day: ')
            sql = '''insert into employee(emp_national_id, emp_name, emp_lname,
             emp_phone, emp_address, emp_role, emp_salary, emp_insurance, emp_off_days)
             values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            values = (employee.national_id, employee.name, employee.lastname, employee.phonenumber, employee.empaddress, employee.role, employee.salary, employee.insurance, employee.offdays)
            try:
                cur.execute(sql, values)
                emp_id = cur.lastrowid
                sql = 'insert into employee_access(emp_id, username, password_hash) values(%s, %s, %s)'
                values = (emp_id, employee.username, employee.password)
                cur.execute(sql, values)
                conn.commit()
                print(colorama.Fore.GREEN, 'employee data added to employee table', colorama.Fore.RESET)
                print(colorama.Fore.GREEN, 'employee account data added to employee access table', colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error inserting employee: {err}', colorama.Fore.RESET)
                continue
            cur.execute('select * from employee where emp_national_id = %s', (employee.national_id, ))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            for col, val in zip(columns, row):
                print(f"{col}: {val}")

        cont = input('\tdo you want to continue? press y: ')
        if cont.lower() == 'y':
            continue
        else:
            break

def edit_employee(conn):
    cur = conn.cursor()
    while True:
        edit_employee_code = input('\tenter employee employment id you want to edit:')
        if not edit_employee_code.strip():
            print(colorama.Fore.RED, 'ID cannot be empty', colorama.Fore.RESET)
            break
        try:
            edit_employee_code = int(edit_employee_code)
        except ValueError:
            print(colorama.Fore.RED, 'ID must be a number', colorama.Fore.RESET)
            continue
        cur.execute('select * from employee where emp_id = %s', (edit_employee_code,))
        employee = cur.fetchone()
        if employee is None:
            print(colorama.Fore.RED, '\t\twrong employment id', colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN, 'employee found!', colorama.Fore.RESET)
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, employee))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
            fields = {
                "1": "emp_name",
                "2": "emp_lname",
                "3": "emp_national_id",
                "4": "emp_phone",
                "5": "emp_address",
                "6": "emp_role",
                "7": "emp_salary",
                "8": "emp_overtime",
                "9": "emp_insurance",
                "10": "emp_off_days",
            }
            for key, val in fields.items():
                print(f"\t{key}. {val}")
            edit_part_num = input('\twhich attribute do you want to edit: ')
            if edit_part_num not in fields:
                print(colorama.Fore.RED, 'attribute doesnt exist', colorama.Fore.RESET)
                continue
            else:
                if edit_part_num == '5':
                    new_value = get_address()
                    sql = 'update employee set emp_address = %s where emp_id = %s'
                    try:
                        cur.execute(sql, (new_value, edit_employee_code))
                        conn.commit()
                        print(colorama.Fore.GREEN, '\t\temployee data updated', colorama.Fore.RESET)
                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'Error editing employee: {err}', colorama.Fore.RESET)
                        continue
                else:
                    new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
                    sql = f'update employee set {fields[edit_part_num]} = %s where emp_id = %s'
                    try:
                        cur.execute(sql, (new_value, edit_employee_code))
                        conn.commit()
                        print(colorama.Fore.GREEN, '\t\temployee data updated', colorama.Fore.RESET)
                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'Error editing employee: {err}', colorama.Fore.RESET)
                        continue
                print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
                cur.execute("SELECT * FROM employee WHERE emp_id = %s", (edit_employee_code,))
                row = cur.fetchone()
                columns = [desc[0] for desc in cur.description]
                row_dict = dict(zip(columns, row))
                for col, val in row_dict.items():
                    print(f"{col}: {val}")
                ask = input('edit another employee? press y ')
                if ask.lower() != 'y':
                    break


def delete_employee(conn):
    cur = conn.cursor()
    while True:
        delete_employee_code = input('\tenter employee employment id you want to delete:')
        if not delete_employee_code.strip():
            print(colorama.Fore.RED, 'ID cannot be empty', colorama.Fore.RESET)
            break
        try:
            delete_employee_code = int(delete_employee_code)
        except ValueError:
            print(colorama.Fore.RED, 'ID must be a number', colorama.Fore.RESET)
            continue
        cur.execute('select * from employee where emp_id = %s', (delete_employee_code,))
        employee = cur.fetchone()
        if employee is None:
            print(colorama.Fore.RED, '\t\twrong employment id', colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN, 'employee found!', colorama.Fore.RESET)
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, employee))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
            ask = input('\t\tdelete employee? press y (this will also remove employee account)')
            if ask.lower() == 'y':
                try:
                    cur.execute('delete from employee_access where emp_id = %s', (delete_employee_code,))
                    cur.execute('delete from employee where emp_id = %s', (delete_employee_code,))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\temployee and employee account deleted successfully',
                          colorama.Fore.RESET)
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'Error deleting employee: {err}', colorama.Fore.RESET)
                    continue
                ask = input('delete another employee? press y ')
                if ask.lower() != 'y':
                    break
            else:
                print(colorama.Fore.YELLOW, 'invalid input, no changes were made', colorama.Fore.RESET)
                break


# ------------------------- employee functions ----------------------------
def employee_log_in(conn):
    choice = input('\tto enter employee panel write "y": ')
    if choice.lower() != 'y':
        print(colorama.Fore.YELLOW, "\tReturning to menu.", colorama.Fore.RESET)
        return
    while True:
        username = input('\tUsername: ')
        password = input('\tPassword: ')
        if ' ' in username or ' ' in password or not username or not password:
            print(colorama.Fore.RED, '\tusername and password cannot contain spaces or be empty.', colorama.Fore.RESET)
        else:
            cur = conn.cursor()
            cur.execute('select * from employee_access where username = %s', (username,))
            employee = cur.fetchone()
            if employee is None:
                print(colorama.Fore.RED, 'wrong username', colorama.Fore.RESET)
            else:
                ph = PasswordHasher()
                try:
                    grant_access = ph.verify(employee[2], password)
                except VerifyMismatchError:
                    grant_access = False
                if grant_access:
                    cur.execute('select emp_name, emp_lname from employee where emp_id = %s', (employee[0],))
                    info_employee = cur.fetchone()
                    print(colorama.Fore.GREEN, f'welcome {info_employee[0]} {info_employee[1]}', colorama.Fore.RESET)
                    return employee[0]
                else:
                    print(colorama.Fore.RED, 'incorrect password', colorama.Fore.RESET)

def all_employee_actions(conn, emp_id):
    employee_access = data.access_type['employee access']
    while True:
        for i in employee_access:
            print(colorama.Fore.BLUE, f'\t{i} -> {employee_access[i]}')
        print('\tExit', colorama.Fore.RESET)
        ask = input('\tChoose action: ')
        if ask == '1':
            employee_see_personal_info(conn, emp_id)
        elif ask == '2':
            employee_edit_personal_info(conn, emp_id)
        elif ask == '3':
            print('option unavailable')
        elif ask.lower() == 'exit':
            break
        else:
            print(colorama.Fore.RED, 'invalid input', colorama.Fore.RESET)

def employee_see_personal_info(conn, emp_id):
    cur = conn.cursor()
    cur.execute('''select employee.emp_id, emp_name, emp_lname, emp_national_id,
                emp_phone, emp_address, 
                emp_role,emp_salary, emp_overtime, 
                emp_insurance, emp_off_days, employee_access.username
                from employee
                inner join employee_access
                on employee.emp_id = employee_access.emp_id
                where employee.emp_id = %s
                ''', (emp_id, ))
    rows = cur.fetchone()
    columns = [desc[0] for desc in cur.description]
    if rows:
        for col, val in zip(columns, rows):
            print(f"{col}: {val}")
        return rows
    else:
        print(colorama.Fore.RED, 'no data found', colorama.Fore.RESET)

def employee_edit_personal_info(conn, employee):
    cur = conn.cursor()
    while True:
        fields = {
            "1": "emp_name",
            "2": "emp_lname",
            "3": "emp_phone",
            "4": "emp_address",
            "5": "emp_national_id",
            "6": "emp_overtime",
            "7": "emp_off_days",
            "8": "password_hash"
        }
        for key, val in fields.items():
            print(f"\t{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print('attribute doesnt exist')
            return
        else:
            if edit_part_num == '8':
                    new_value = customer_password()
                    sql = f'update employee_access set password_hash = %s where emp_id = %s'
                    try:
                        cur.execute(sql, (new_value, employee, ))
                        conn.commit()
                        print(colorama.Fore.GREEN, '\t\temployee account data updated', colorama.Fore.RESET)
                    except Exception as err:
                        conn.rollback()
                        print(colorama.Fore.RED, f'error editing info: {err}', colorama.Fore.RESET)
            elif edit_part_num == '4':
                new_value = get_address()
                sql = f'update employee set emp_address = %s where emp_id = %s'
                try:
                    cur.execute(sql, (new_value, employee,))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\temployee data updated', colorama.Fore.RESET)
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'error editing info: {err}', colorama.Fore.RESET)
                    continue
            else:
                new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
                sql = f'update employee set {fields[edit_part_num]} = %s where emp_id = %s'
                try:
                    cur.execute(sql, (new_value, employee))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\temployee data updated', colorama.Fore.RESET)
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f'error editing info: {err}', colorama.Fore.RESET)
                    continue

            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM employee WHERE emp_id = %s", (employee,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")


        cont = input('\tdo you want to continue? press y: ')
        if cont.lower() == 'y':
            continue
        else:
            break
# ---------------------------------------------------------------------------
#---------------------------seller functions--------------------------------
def seller_sign_up(conn):
    choice = input('\tto sign up as a seller press Y: ')
    if choice.lower() != 'y':
        print(colorama.Fore.YELLOW, "\tSignup cancelled. Returning to menu.", colorama.Fore.RESET)
        return
    else:
        seller = OOP.Seller()
        while True:
            seller.seller_work_permit_num = required_input('\twork permit number: ')
            if seller.seller_work_permit_num.isdigit():
                break
            else:
                print(colorama.Fore.RED, 'work permit should be numbers', colorama.Fore.RESET)
        cur = conn.cursor()
        cur.execute('SELECT sel_workpermit_num FROM seller WHERE sel_workpermit_num = %s', (seller.seller_work_permit_num,))
        if cur.fetchone() is None:
            seller.username = seller_username(conn, seller)
            seller.password = customer_password()
            seller.entity_name = required_input('\tcompany or store name: ')
            seller.representative_name = required_input('\trepresentative name: ')
            seller.seller_rep_pnum = required_input('\trepresentative phone number: ')
            # print('\tenter the address of all your branches')
            # addresses = []
            # x = 1
            # for i in range(100):
            #     address = get_address()
            #     addresses.append(f"{"branch {x}": {address['Province']}, {address['City']}, {address['Address']}, NO: {address['NO']}, Unit: {address['Unit']}}")
            #     add_branch = input('to add a branch press Y')
            #     if add_branch.lower() == 'y':
            #         x += 1
            #         continue
            #     else:
            #         break
            # seller.seller_address = addresses
            seller.seller_address = get_address()
            seller.other_contact_info = input('\t enter any other contact info: ')
            seller.product_exp = input('\twrite any relevant explanation related to your products or company')
            cur = conn.cursor()
            try:

                sql = 'insert into seller_account(username,password_hash) values (%s, %s)'
                value = (seller.username, seller.password)
                cur.execute(sql, value)
                seller_id = cur.lastrowid
                sql = 'insert into seller(seller_id, sel_workpermit_num, sel_store_company_name, sel_representative_name, sel_representative_num, seller_address, sel_other_contact_info, sel_product_explanation ) values (%s, %s, %s, %s, %s, %s, %s, %s)'
                value = (
                seller_id, seller.seller_work_permit_num, seller.entity_name, seller.representative_name, seller.seller_rep_pnum,
                seller.seller_address, seller.other_contact_info, seller.product_exp)
                cur.execute(sql, value)
                conn.commit()
                print(colorama.Fore.GREEN, "your data has been saved and account created successfully. \t\nyou can check your state on your account. \t\ncurrent state: waiting for administration verification ", colorama.Fore.RESET)
            except Exception as err:
                conn.rollback()
                print(colorama.Fore.RED, f'Error creating seller account: {err}', colorama.Fore.RESET)

        else:
            print(colorama.Fore.YELLOW, 'you already have an account', colorama.Fore.RESET)
            return

def see_seller_requests(conn):
    cur = conn.cursor()
    cur.execute('select * from seller where sign_up_state = %s', ('processing', ))
    requests = cur.fetchall()
    if not requests:
        print(colorama.Fore.YELLOW, 'No pending requests.', colorama.Fore.RESET)
        return
    columns = [desc[0] for desc in cur.description]
    print(colorama.Fore.CYAN, 'Pending seller requests:', colorama.Fore.RESET)
    request_ids = []
    for row in requests:
        row_dict = dict(zip(columns, row))
        request_ids.append(row_dict['request_id'])
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        print('-' * 40)
    while True:
        ask = input('do you want to make any changes? press y')
        if ask.lower() == 'y':
            request_id = int(input('\tchoose request id: '))
            if request_id not in request_ids:
                print(colorama.Fore.RED, 'wrong request id', colorama.Fore.RESET)
            else:
                cur.execute('select seller_id from seller where request_id = %s', (request_id,))
                seller_id = cur.fetchone()
                ask = input('\tU -> update request state\n\tE -> exit')
                if ask.lower() == 'u':
                    select = input('\t1: verify\n\t2: reject\n\tE -> exit')
                    if select.strip() == '1':
                        try:
                            cur.execute('update seller set sign_up_state = %s where request_id = %s',
                                    ('verified', request_id,))
                            cur.execute('update seller_account set sign_up_state = %s where seller_id = %s', ('verified', seller_id[0], ))
                            conn.commit()
                            print(colorama.Fore.GREEN, 'seller state updated to "verified".', colorama.Fore.RESET)
                            continue
                        except Exception as err:
                            conn.rollback()
                            print(colorama.Fore.RED, f'error changing seller state: {err}', colorama.Fore.RESET)
                            continue
                    elif select.strip() == '2':
                        try:
                            cur.execute('update seller set sign_up_state = %s where request_id = %s',
                                        ('denied', request_id,))
                            conn.commit()
                            print(colorama.Fore.GREEN, 'seller state updated to "denied".', colorama.Fore.RESET)
                        except Exception as err:
                            conn.rollback()
                            print(colorama.Fore.RED, f'error changing seller state: {err}', colorama.Fore.RESET)
                            continue
                        check = input('delete seller from table? press y')
                        if check.lower() == 'y':
                            try:
                                cur.execute('delete from seller where request_id = %s', (request_id, ))
                                conn.commit()
                                print(colorama.Fore.GREEN, 'seller deleted from requests.', colorama.Fore.RESET)
                                continue
                            except Exception as err:
                                conn.rollback()
                                print(colorama.Fore.RED, f'error changing seller state: {err}', colorama.Fore.RESET)
                                continue
                    elif select.lower() == 'e':
                        break
                elif ask.lower() == 'e':
                    print('exiting...')
                    break
                else:
                    print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
        else:
            break

def seller_log_in(conn):
    choice = input('\tto enter seller panel write "y": ')
    if choice.lower() != 'y':
        print(colorama.Fore.YELLOW, "\tReturning to menu.", colorama.Fore.RESET)
        return
    while True:
        username = input('\tUsername: ')
        password = input('\tPassword: ')
        if ' ' in username or ' ' in password or not username or not password:
            print(colorama.Fore.RED, '\tusername and password cannot contain spaces or be empty.', colorama.Fore.RESET)
        else:
            cur = conn.cursor()
            cur.execute('select * from seller_account where username = %s', (username,))
            seller = cur.fetchone()
            if seller is None:
                print(colorama.Fore.RED, 'wrong username', colorama.Fore.RESET)
            else:
                ph = PasswordHasher()
                try:
                    grant_access = ph.verify(seller[2], password)
                except VerifyMismatchError:
                    grant_access = False
                if grant_access:
                    cur.execute('select sel_store_company_name from seller where seller_id = %s', (seller[0],))
                    info_seller = cur.fetchone()
                    print(colorama.Fore.GREEN, f'welcome {info_seller[0]}', colorama.Fore.RESET)
                    return seller
                else:
                    print(colorama.Fore.RED, 'incorrect password', colorama.Fore.RESET)
def admin_review_pending(conn):
    cur = conn.cursor()
    while True:
        cur.execute('select * from pending_items where status = %s order by seller_id', ('processing', ))
        pending_items = cur.fetchall()
        if not pending_items:
            print(colorama.Fore.RED, 'no item to review', colorama.Fore.RESET)
            return
        else:
            for row in pending_items:
                pending_id = row[0]
                seller_id = row[1]
                item_type = row[2]
                data_json = row[3]
                item_data = json.loads(data_json)

                print(colorama.Fore.CYAN,
                      f"\nPending Item ID: {pending_id} | Seller: {seller_id} | Type: {item_type}",
                      colorama.Fore.RESET)
                for key, value in item_data.items():
                    print(f"\t{key}: {value}")

            change_state_id = input('enter pending item ID you want to approve : (or e to exit) ')
            if change_state_id.lower() == 'e':
                break
            else:
                cur.execute('SELECT * FROM pending_items WHERE id = %s', (int(change_state_id),))
                row_to_approve = cur.fetchone()
                if row_to_approve:
                    add_pending_to_table(conn, int(change_state_id))
                else:
                    print(colorama.Fore.RED, 'wrong ID', colorama.Fore.RESET)
                    continue

def add_pending_to_table(conn, change_state_id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM pending_items WHERE id = %s and status = %s', (change_state_id, 'processing', ))
    row = cur.fetchone()
    if not row:
        print(colorama.Fore.RED, 'Pending item not found', colorama.Fore.RESET)
        return
    seller_id, item_type, data_json = row[1], row[2], row[3]
    item_data = json.loads(data_json)
    if item_type == 'laptop':
        cur.execute("SELECT laptop_code FROM laptop ORDER BY laptop_code DESC LIMIT 1")
        row = cur.fetchone()
        if row:
            last_number = int(row[0][3:])
            new_number = last_number + 1
        else:
            new_number = 1001
        code = 'LAP' + str(new_number)
        try:
            cur.execute('''
                INSERT INTO laptop(laptop_code, l_model, l_brand, l_warranty_time,
                l_warranty_company, l_weight, l_size, l_color, l_production_year, l_battery_life,
                l_cpu, l_ram, l_storage, l_gpu, l_os, l_webcam, l_speaker, l_screensize)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (code, item_data["model"], item_data["brand"], item_data["warranty time"], item_data["warranty company"],
                item_data["weight"], item_data["size"], item_data["color"], item_data["production year"],item_data["battery life"],
                item_data["CPU"], item_data["RAM"], item_data["storage"], item_data["GPU"],
                item_data["OS"], item_data["webcam"], item_data["speaker"], item_data["screen size"]))
            cur.execute('''
                INSERT INTO stock (laptop_code, item_type, seller_id, price, stock_off, stock)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
            code, "Laptop", seller_id, item_data["price"], item_data["off"], item_data["stock"]))
            cur.execute('UPDATE pending_items SET status = %s WHERE id = %s', ('approved', change_state_id))
            conn.commit()
            print(colorama.Fore.GREEN, "Item added to laptop table and stock", colorama.Fore.RESET)
            print(colorama.Fore.GREEN, f"Item approved for seller {seller_id}", colorama.Fore.RESET)
        except Exception as err:
            conn.rollback()
            print(colorama.Fore.RED, f"Error adding pending item: {err}", colorama.Fore.RESET)

    elif item_type == 'phone':
        cur.execute("SELECT phone_code FROM phone ORDER BY phone_code DESC LIMIT 1")
        row = cur.fetchone()
        if row:
            last_number = int(row[0][3:])
            new_number = last_number + 1
        else:
            new_number = 1001
        code = 'PHO' + str(new_number)
        try:
            cur.execute('''
                INSERT INTO phone(phone_code, p_model, p_brand, p_warranty_time,
                p_warranty_company, p_weight, p_size, p_color, p_production_year, p_battery_life,
                p_storage, p_sim, p_frontcam, p_backcam, p_os, p_chargingport, p_screensize)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (code, item_data["model"], item_data["brand"], item_data["warranty time"], item_data["warranty company"],
                item_data["weight"], item_data["size"], item_data["color"], item_data["production year"],item_data["battery life"],
                item_data["storage"], item_data["sim"], item_data["front camera"], item_data["back camera"],
                item_data["OS"], item_data["charging port"], item_data["screen size"]))
            cur.execute('''
                INSERT INTO stock (phone_code, item_type, seller_id, price, stock_off, stock)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
            code, "Phone", seller_id, item_data["price"], item_data["off"], item_data["stock"]))
            cur.execute('UPDATE pending_items SET status = %s WHERE id = %s', ('approved', change_state_id))
            conn.commit()
            print(colorama.Fore.GREEN, "Item added to phone table and stock", colorama.Fore.RESET)
            print(colorama.Fore.GREEN, f"Item approved for seller {seller_id}", colorama.Fore.RESET)
        except Exception as err:
            conn.rollback()
            print(colorama.Fore.RED, f"Error adding pending item: {err}", colorama.Fore.RESET)

    elif item_type == 'camera':
        cur.execute("SELECT camera_code FROM camera ORDER BY camera_code DESC LIMIT 1")
        row = cur.fetchone()
        if row:
            last_number = int(row[0][3:])
            new_number = last_number + 1
        else:
            new_number = 1001
        code = 'CAM' + str(new_number)
        try:
            cur.execute('''
                INSERT INTO camera(camera_code, c_model, c_brand, c_warranty_time,
                c_warranty_company, c_weight, c_size, c_color, c_production_year, c_battery_life,
                c_memory, c_lenz, c_shutter, c_type, c_touchscreen)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (code, item_data["model"], item_data["brand"], item_data["warranty time"], item_data["warranty company"],
                item_data["weight"], item_data["size"], item_data["color"], item_data["production year"],item_data["battery life"],
                item_data["memory"], item_data["lenz"], item_data["shutter"], item_data["camera type"],
                item_data["touch screen"]))
            cur.execute('''
                INSERT INTO stock (camera_code, item_type, seller_id, price, stock_off, stock)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
            code, "Camera", seller_id, item_data["price"], item_data["off"], item_data["stock"]))
            cur.execute('UPDATE pending_items SET status = %s WHERE id = %s', ('approved', change_state_id))
            conn.commit()
            print(colorama.Fore.GREEN, "Item added to camera table and stock", colorama.Fore.RESET)
            print(colorama.Fore.GREEN, f"Item approved for seller {seller_id}", colorama.Fore.RESET)
        except Exception as err:
            conn.rollback()
            print(colorama.Fore.RED, f"Error adding pending item: {err}", colorama.Fore.RESET)

def delete_seller(conn):
    cur = conn.cursor()
    while True:
        delete_seller_code = int(input('\tenter seller id you want to delete:'))
        cur.execute('select * from seller_account where seller_id = %s', (delete_seller_code,))
        seller = cur.fetchone()
        if seller is None:
            print(colorama.Fore.RED, '\t\twrong seller id', colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN, 'seller found!', colorama.Fore.RESET)
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, seller))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
            ask = input('\t\tdelete seller? press y (this will no remove seller from seller table)')
            if ask.lower() == 'y':
                try:
                    cur.execute('delete from seller_account where seller_id = %s', (delete_seller_code,))
                    conn.commit()
                    print(colorama.Fore.RED, '\t\tseller account deleted successfully',
                          colorama.Fore.RESET)
                except Exception as err:
                    conn.rollback()
                    print(colorama.Fore.RED, f"Error deleting seller: {err}", colorama.Fore.RESET)
            else:
                print(colorama.Fore.YELLOW, 'invalid input, no changes were made', colorama.Fore.RESET)
                break

def all_seller_actions(conn, identified_seller):
    while True:
        seller_state = identified_seller[-1]
        if seller_state == 'verified':
            for i in data.access_type['seller access']:
                print(colorama.Fore.CYAN, f'{i}: {data.access_type['seller access'][i]}')
            print('\tE : Exit', colorama.Fore.RESET)
            ask = input('\tChoose action: ')
            if ask.lower() == 'e':
                print('exiting...')
                break
            elif ask.strip() == '1':
                seller_add_item(conn, identified_seller)
            elif ask.strip() == '2':
                seller_my_products(conn, identified_seller)
            elif ask.strip() == '3':
                edit_stock_info(conn, identified_seller)
            elif ask.strip() == '4':
                seller_personal_info(conn, identified_seller)
            elif ask.strip() == '5':
                seller_edit_personal_info(conn, identified_seller)
            else:
                print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
        elif seller_state == 'processing':
            print(colorama.Fore.YELLOW, 'your request is still under consideration. after verification you can access your panel', colorama.Fore.RESET)
            inp = input('\t1: see personal info\t\nE: exit')
            if inp.strip() == '1':
                seller_personal_info(conn, identified_seller)
            elif inp.lower() == 'e':
                break
            else:
                print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
                return

def seller_add_item(conn, identified_seller):
    cur = conn.cursor()
    while True:
        item_type = input(
            '\tL -> Laptop\n\tP -> Phone\n\tC -> Camera\n\tE -> Exit\n\tChoose product type to be added:')
        if item_type.lower() == 'l':
            add_laptop_pending(conn, identified_seller)
        elif item_type.lower() == 'p':
            add_phone_pending(conn, identified_seller)
        elif item_type.lower() == 'c':
            add_camera_pending(conn, identified_seller)
        elif item_type.lower() == 'e':
            break
        else:
            print('wrong input')
##############################################
def add_laptop_pending(conn, identified_seller):
    item = OOP.Laptop()
    item.model = required_input('\tmodel: ')
    item.production_year = input('\tproduction year (xxxx): ')
    item.brand = required_input('\tbrand: ')
    item.price = float(required_input('\tprice: '))
    item.off = input('\toff (without %): ')
    item.stock = int(required_input('\tstock: '))
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
    laptop_data = read_json_laptop_pending()
    laptop_data.append(temp_laptop_json)
    write_json_laptop_pending(laptop_data)
    data_json = json.dumps(temp_laptop_json)
    cur = conn.cursor()
    cur.execute('''insert into pending_items(
    seller_id, item_type, data
    ) values(%s, %s, %s)
    ''', (identified_seller[0], 'laptop', data_json, ))
    conn.commit()
    print(colorama.Fore.GREEN, "Product added to pending table. administration will review your request!", colorama.Fore.RESET)

def add_phone_pending(conn, identified_seller):
    item = OOP.Phone()
    item.model = required_input('\tmodel: ')
    item.production_year = input('\tproduction year (xxxx): ')
    item.brand = required_input('\tbrand: ')
    item.price = float(required_input('\tprice (Tooman): '))
    item.off = input('\toff (without %): ')
    item.stock = int(required_input('\tstock: '))
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
    phone_data = read_json_phone_pending()
    phone_data.append(temp_phone_json)
    write_json_phone_pending(phone_data)
    data_json = json.dumps(temp_phone_json)
    cur = conn.cursor()
    cur.execute('''insert into pending_items(
        seller_id, item_type, data
        ) values(%s, %s, %s)
        ''', (identified_seller[0], 'phone', data_json,))
    conn.commit()
    print(colorama.Fore.GREEN, "Product added to pending table. administration will review your request!",
          colorama.Fore.RESET)


def add_camera_pending(conn, identified_seller):
    item = OOP.Camera()
    item.model = required_input('\tmodel: ')
    item.production_year = input('\tproduction year (xxxx): ')
    item.brand = required_input('\tbrand: ')
    item.price = float(required_input('\tprice: '))
    item.off = input('\toff (without %): ')
    item.stock = int(required_input('\tstock: '))
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
    camera_data = read_json_camera_pending()
    camera_data.append(temp_camera_json)
    write_json_camera_pending(camera_data)
    data_json = json.dumps(temp_camera_json)
    cur = conn.cursor()
    cur.execute('''insert into pending_items(
        seller_id, item_type, data
        ) values(%s, %s, %s)
        ''', (identified_seller[0], 'camera', data_json,))
    conn.commit()
    print(colorama.Fore.GREEN, "Product added to pending table. administration will review your request!",
              colorama.Fore.RESET)
#--------------------------------------------------------------------------
def seller_my_products(conn, identified_seller):
    cur = conn.cursor()
    cur.execute('select * from pending_items where seller_id = %s', (identified_seller[0], ))
    products = cur.fetchall()
    if not products:
        print(colorama.Fore.RED, 'you have not added any products', colorama.Fore.RESET)
    else:
        for row in products:
            pending_id = row[0]
            seller_id = row[1]
            item_type = row[2]
            data_json = row[3]
            status = row[-1]
            item_data = json.loads(data_json)

            print(colorama.Fore.CYAN,
                  f"\nPending Item ID: {pending_id} | Seller: {seller_id} | Type: {item_type}, | Status: {status}",
                  colorama.Fore.RESET)
            for key, value in item_data.items():
                print(f"\t{key}: {value}")
# ----------------------------------------------------------------------------
def edit_stock_info(conn, identified_seller):
    cur = conn.cursor()
    cur.execute('select * from stock where seller_id = %s', (identified_seller[0], ))
    products = cur.fetchall()
    if not products:
        print(colorama.Fore.RED, 'you have no items in  store\'s stock', colorama.Fore.RESET)
    else:
        columns = [desc[0] for desc in cur.description]
        for i in products:
            row_dict = dict(zip(columns, i))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
        ask = input('\tenter stock id you want to edit: ')
        cur.execute('select * from stock where stock_id = %s', (ask, ))
        product = cur.fetchone()
        if product is None:
            print(colorama.Fore.RED, 'wrong id', colorama.Fore.RESET)
        else:
            fields = {
                '1': 'price',
                '2': 'off',
                '3': 'stock'
            }
            for key, val in fields.items():
                print(f"\t{key}. {val}")
            while True:
                edit_part_num = input('\twhich attribute do you want to edit: ')
                if edit_part_num not in fields:
                    print('attribute doesnt exist')
                    return
                elif edit_part_num == '1':
                    new_value = float(input('\tnew price: '))
                    sql = f'update stock set price = %s, state = %s where stock_id = %s'
                    cur.execute(sql, (new_value, 'updated by seller', ask, ))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\tstock data updated, waiting for admin approval', colorama.Fore.RESET)
                    break
                elif edit_part_num == '2':
                    new_value = input('\tnew off: ')
                    sql = f'update stock set stock_off = %s, state = %s where stock_id = %s'
                    cur.execute(sql, (new_value, 'updated by seller', ask, ))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\tstock data updated, waiting for admin approval', colorama.Fore.RESET)
                    break
                elif edit_part_num == '3':
                    new_value = int(input('\tnew stock: '))
                    sql = f'update stock set stock = %s, state = %s where stock_id = %s'
                    cur.execute(sql, (new_value, 'updated by seller', ask, ))
                    conn.commit()
                    print(colorama.Fore.GREEN, '\t\tstock data updated, waiting for admin approval', colorama.Fore.RESET)
                    break

def admin_approve_stock_updates(conn, identified_admin):
    cur = conn.cursor()
    cur.execute('select * from stock where state = %s', ('updated by seller', ))
    updates = cur.fetchall()
    if not  updates:
        print(colorama.Fore.RED, 'no updates avaiable', colorama.Fore.RESET)
    else:
        columns = [desc[0] for desc in cur.description]
        for i in updates:
            row_dict = dict(zip(columns, i))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
        ask = input('\tenter stock id: ')
        cur.execute('select * from stock where stock_id = %s', (ask,))
        product = cur.fetchone()
        if product is None:
            print(colorama.Fore.RED, 'wrong id', colorama.Fore.RESET)
        else:
            todo = input('A: approve, D: deny: ').strip().upper()
            if todo == 'A':
                cur.execute('update stock set state = %s where stock_id = %s', ('approved by admin', ask))
            elif todo == 'D':
                cur.execute('update stock set state = %s where stock_id = %s', ('denied by admin', ask))
            else:
                print('Invalid input')
                return
            conn.commit()
            print(colorama.Fore.GREEN, 'State updated', colorama.Fore.RESET)





##############################################
def seller_personal_info(conn, seller):
    cur = conn.cursor()
    cur.execute('''select seller.seller_id, sel_store_company_name, sel_representative_name, sel_representative_num,
                    sel_workpermit_num, sel_address, 
                    sel_other_contact_info, sel_product_explanation, sign_up_state, 
                    rating, seller_account.username
                    from seller
                    inner join seller_account
                    on seller.seller_id = seller_account.seller_id
                    where seller.seller_id = %s
                    ''', (seller[0],))
    rows = cur.fetchone()
    columns = [desc[0] for desc in cur.description]
    if rows:
        for col, val in zip(columns, rows):
            print(f"{col}: {val}")
        return rows
    else:
        print(colorama.Fore.RED, 'no data found', colorama.Fore.RESET)

def seller_edit_personal_info(conn, seller):
    cur = conn.cursor()
    while True:
        fields = {
            "1": "sel_store_company_name",
            "2": "sel_representative_name",
            "3": "sel_representative_num",
            "4": "seller_address",
            "5": "sel_other_contact_info",
            "6": "sel_product_explanation",
            "7": "username",
            "8": "password_hash"
        }
        for key, val in fields.items():
            print(f"\t{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print('attribute doesnt exist')
            return

        elif edit_part_num == '4':
            new_value = get_address()
            sql = f'update seller set sel_address = %s where seller_id = %s'
            cur.execute(sql, (new_value, seller[0],))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tseller data updated', colorama.Fore.RESET)
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM seller WHERE seller_id = %s", (seller[0],))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")

        elif edit_part_num == '7':
            new_value = seller_username(conn, seller)
            sql = 'update seller_account set username = %s where seller_id = %s'
            cur.execute(sql, (new_value, seller[0]))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tseller data updated', colorama.Fore.RESET)
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM seller WHERE seller_id = %s", (seller[0],))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")

        elif edit_part_num == '8':
            new_value = customer_password()
            sql = f'update seller_account set password_hash = %s where seller_id = %s'
            cur.execute(sql, (new_value, seller[0],))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tseller account data updated', colorama.Fore.RESET)

        else:
            new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
            sql = f'update seller set {fields[edit_part_num]} = %s where seller_id = %s'
            cur.execute(sql, (new_value, seller[0]))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tseller data updated', colorama.Fore.RESET)
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM seller WHERE seller_id = %s", (seller[0],))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")

        cont = input('\tdo you want to continue? press y: ')
        if cont.lower() == 'y':
            continue
        else:
            break
# ------------------------- customer functions ----------------------------
def customer_sign_up(conn, session):
    choice = input('\twrite "y" to sign up: ')
    if choice.lower() != 'y':
        print(colorama.Fore.YELLOW, "\tSignup cancelled. Returning to menu.", colorama.Fore.RESET)
        return
    else:
        customer = OOP.Customer()
        while True:
            customer.phonenumber = required_input('\tphone number: ')
            if customer.phonenumber.isdigit() and len(customer.phonenumber) == 11 and customer.phonenumber[0:2] == '09':
                break
            else:
                print(colorama.Fore.RED, 'incorrect phone number', colorama.Fore.RESET)
        cur = conn.cursor()
        cur.execute('SELECT cust_phone FROM customer WHERE cust_phone = %s', (customer.phonenumber,))
        if cur.fetchone() is None:
            customer.username = customer_username(conn)
            customer.password = customer_password()
            customer.name = required_input('\tname: ')
            customer.lastname = required_input('\tlast name: ')
            customer.address = get_address()
            while True:
                pcode = required_input('\tpostal code: ')
                if pcode.isdigit() and len(pcode) == 10:
                    customer.postal_code = pcode
                    break
                else:
                    print(colorama.Fore.RED, 'invalid postal code', colorama.Fore.RESET)
            customer.email = email_checker()
            cur = conn.cursor()
            sql = 'insert into customer_account(cust_username, cust_password_hash) values (%s, %s)'
            value = (customer.username, customer.password)
            cur.execute(sql, value)
            conn.commit()
            cust_id = cur.lastrowid
            sql = 'insert into customer(cust_id, cust_name, cust_lname, cust_phone, cust_address, cust_pcode, cust_email) values (%s, %s, %s, %s, %s, %s, %s)'
            value = (
                cust_id, customer.name, customer.lastname, customer.phonenumber, customer.address, customer.postal_code,
                customer.email)
            cur.execute(sql, value)
            conn.commit()
            print(colorama.Fore.GREEN, "account created successfully", colorama.Fore.RESET)
            session['logged_in'] = True
            session['cust_id'] = cust_id
            return cust_id
        else:
            print(colorama.Fore.YELLOW, 'you already have an account', colorama.Fore.RESET)


def customer_log_in(conn, session):
    choice = input('\tto enter customer panel write "y": ')
    if choice.lower() != 'y':
        print(colorama.Fore.YELLOW, "\tReturning to menu.", colorama.Fore.RESET)
        return
    while True:
        username = input('\tUsername: ')
        password = input('\tPassword: ')
        if ' ' in username or ' ' in password or not username or not password:
            print(colorama.Fore.RED, '\tusername and password cannot contain spaces or be empty.', colorama.Fore.RESET)
        else:
            cur = conn.cursor()
            cur.execute('select * from customer_account where cust_username = %s', (username,))
            customer = cur.fetchone()
            if customer is None:
                print(colorama.Fore.RED, 'wrong username', colorama.Fore.RESET)
            else:
                ph = PasswordHasher()
                try:
                    grant_access = ph.verify(customer[2], password)
                except VerifyMismatchError:
                    grant_access = False
                if grant_access:
                    cur.execute('select cust_name, cust_lname from customer where cust_id = %s', (customer[0],))
                    info_customer = cur.fetchone()
                    print(colorama.Fore.GREEN, f'welcome {info_customer[0]} {info_customer[1]}', colorama.Fore.RESET)
                    session['logged_in'] = True
                    session['cust_id'] = customer[0]
                    return customer[0]
                else:
                    print(colorama.Fore.RED, 'incorrect password', colorama.Fore.RESET)

def all_customer_actions(conn, customer, session):
    while True:
        for i in data.access_type['customer access']:
            print(colorama.Fore.BLUE, f'\t{i} -> {data.access_type['customer access'][i]}')
        print('\tExit', colorama.Fore.RESET)
        ask = input('\tChoose action: ')
        if ask == '1':
            customer_personal_info(conn, customer)
        elif ask == '2':
            customer_edit_info(conn, customer)
        elif ask == '3':
            customer_cart(conn, customer, session)
        elif ask == '4':
            customer_shopping_history(conn, customer)
        elif ask == '5':
            customer_liked_item_list(conn, customer)
        elif ask == '6':
            show_items(session, conn)
        elif ask == '7':
            customer_search_item(conn, session)
        elif ask.lower() == 'exit':
            break
        else:
            print(colorama.Fore.RED, 'wrnog input', colorama.Fore.RESET)

def customer_personal_info(conn, customer):
    cur = conn.cursor()
    cur.execute('''select customer_account.cust_username, cust_name, cust_lname, cust_phone,
                        cust_address, cust_pcode, cust_email
                        from customer
                        inner join customer_account
                        on customer.cust_id = customer_account.customer_id
                        where customer.cust_id = %s
                        ''', (customer,))
    row = cur.fetchone()
    columns = [desc[0] for desc in cur.description]
    if row:
        for col, val in zip(columns, row):
            print(f"{col}: {val}")
        return row
    else:
        print(colorama.Fore.RED, 'no data found', colorama.Fore.RESET)

def customer_username(conn):
    while True:
        username = required_input('\tusername: ')
        if not username:
            print(colorama.Fore.RED, 'Username cannot be empty.', colorama.Fore.RESET)
            continue
        if len(username) < 4:
            print(colorama.Fore.RED, 'username must be at least 4 characters', colorama.Fore.RESET)
            continue
        else:
            cur = conn.cursor()
            cur.execute("SELECT cust_username FROM customer_account WHERE cust_username = %s", (username,))
            if cur.fetchone() is None:
                print(colorama.Fore.GREEN, 'username available', colorama.Fore.RESET)
                return username
            else:
                print(colorama.Fore.RED, 'username already taken.', colorama.Fore.RESET)

def seller_username(conn, seller):
    while True:
        username = required_input('\tusername: ')
        if not username:
            print(colorama.Fore.RED, 'Username cannot be empty.', colorama.Fore.RESET)
            continue
        if len(username) < 4:
            print(colorama.Fore.RED, 'username must be at least 4 characters', colorama.Fore.RESET)
            continue
        else:
            cur = conn.cursor()
            cur.execute("SELECT username FROM seller_account WHERE username = %s", (username,))
            if cur.fetchone() is None:
                print(colorama.Fore.GREEN, 'username available', colorama.Fore.RESET)
                return username
            else:
                print(colorama.Fore.RED, 'username already taken.', colorama.Fore.RESET)

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
            ph = PasswordHasher()
            hpass = ph.hash(password)
            return hpass


def customer_edit_info(conn, customer):
    cur = conn.cursor()
    while True:
        fields = {
            "1": "cust_username",
            "2": "cust_password_hash",
            "3": "cust_name",
            "4": "cust_lname",
            "5": "cust_phone",
            "6": "cust_address",
            "7": "cust_pcode",
            "8": "cust_email"
        }
        for key, val in fields.items():
            print(f"\t{key}. {val}")
        edit_part_num = input('\twhich attribute do you want to edit: ')
        if edit_part_num not in fields:
            print('attribute doesnt exist')
            return
        if edit_part_num == '1':
            new_value = customer_username(conn)
            sql = f'update customer_account set cust_username = %s where customer_id = %s'
            cur.execute(sql, (new_value, customer,))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tcustomer account data updated', colorama.Fore.RESET)

        elif edit_part_num == '2':
            new_value = customer_password()
            sql = f'update customer_account set cust_password_hash = %s where customer_id = %s'
            cur.execute(sql, (new_value, customer,))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tcustomer account data updated', colorama.Fore.RESET)
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM customer WHERE cust_id = %s", (customer,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")

        elif edit_part_num == '6':
            new_value = get_address()
            sql = f'update customer set cust_address = %s where cust_id = %s'
            cur.execute(sql, (new_value, customer,))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tcustomer data updated', colorama.Fore.RESET)
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM customer WHERE cust_id = %s", (customer,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
        else:
            new_value = input(f'\t\tenter new value for {fields[edit_part_num]}: ')
            sql = f'update customer set {fields[edit_part_num]} = %s where cust_id = %s'
            cur.execute(sql, (new_value, customer))
            conn.commit()
            print(colorama.Fore.GREEN, '\t\tcustomer data updated', colorama.Fore.RESET)
            print(colorama.Fore.GREEN, "\t\tUpdated info:", colorama.Fore.RESET)
            cur.execute("SELECT * FROM customer WHERE cust_id = %s", (customer,))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            row_dict = dict(zip(columns, row))
            for col, val in row_dict.items():
                print(f"{col}: {val}")
        cont = input('\tif you want to continue press y')
        if cont.lower() == 'y':
            pass
        else:
            break

def customer_like_item(conn, item_code, session):
    cur = conn.cursor()
    if not session.get("logged_in"):
        print(colorama.Fore.RED, 'you have not logged in', colorama.Fore.RESET)
    while not session.get("logged_in"):
        ask = input('\t1: log in\n\t2: sign up\n\tE: exit\n\tchoose: ')
        if ask.strip() == '1':
            customer_log_in(conn, session)
            if session.get("logged_in"):
                break
        elif ask.strip() == '2':
            customer_sign_up(conn, session)
            if session.get("logged_in"):
                break
        elif ask.lower() == 'e':
            return
        else:
            print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)

    if session.get("logged_in"):
        customer_id = session.get("cust_id")
        cur.execute('SELECT * FROM liked_items WHERE cust_id = %s AND stock_id = %s', (customer_id, item_code))
        if cur.fetchone():
            print(colorama.Fore.YELLOW, 'Item already liked', colorama.Fore.RESET)
            return

        cur.execute('insert into liked_items(cust_id, stock_id) values(%s, %s)', (customer_id, item_code, ))
        conn.commit()
        print(colorama.Fore.GREEN, 'added to liked items', colorama.Fore.RESET)

def customer_liked_item_list(conn, customer):
    cur = conn.cursor()
    cur.execute('''SELECT stock.*
                FROM stock
                INNER JOIN liked_items
                ON stock.stock_id = liked_items.stock_id
                WHERE liked_items.cust_id = %s''', (customer, ))
    rows = cur.fetchall()
    if not rows:
        print(colorama.Fore.YELLOW, "You have not liked any items yet.", colorama.Fore.RESET)
        return
    columns = [desc[0] for desc in cur.description]
    for row in rows:
        row_dict = dict(zip(columns, row))
        for col, val in row_dict.items():
            print(f"{col}: {val}")
        print('-' * 40)


def customer_add_to_cart(conn, item_stock_code, session):
    cur = conn.cursor()

    if not session.get("logged_in"):
        session["temp_cart"].append(item_stock_code)
        print(colorama.Fore.MAGENTA, 'Item added to temporary cart. Log in or sign up to save your items.',
              colorama.Fore.RESET)

        while not session.get("logged_in"):
            ask = input('\t1: log in\n\t2: sign up\n\tE: exit\n\tchoose: ')
            if ask.strip() == '1':
                customer_log_in(conn, session)
            elif ask.strip() == '2':
                customer_sign_up(conn, session)
            elif ask.lower() == 'e':
                return
            else:
                print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)

    if session.get("logged_in"):
        customer_id = session.get("cust_id")

        cur.execute('SELECT cart_id FROM shopping_carts WHERE customer_id = %s AND status = %s',
                    (customer_id, 'processing'))
        cart = cur.fetchone()

        if cart is None:
            cur.execute('INSERT INTO shopping_carts(customer_id, status) VALUES(%s, %s)',
                        (customer_id, 'processing'))
            conn.commit()
            cur.execute('SELECT cart_id FROM shopping_carts WHERE customer_id = %s AND status = %s',
                        (customer_id, 'processing'))
            cart = cur.fetchone()
        cart_id = cart[0]

        temp_items = session.get("temp_cart", [])
        all_items_to_add = temp_items + [item_stock_code] if item_stock_code not in temp_items else temp_items

        for i in all_items_to_add:
            cur.execute('INSERT INTO cart_items_perperson(cart_id, item_stock_code) VALUES(%s, %s)',
                        (cart_id, i))
        conn.commit()
        session["temp_cart"] = []
        print(colorama.Fore.GREEN, f'{len(all_items_to_add)} item(s) added to your cart.', colorama.Fore.RESET)

        while True:
            action = input('\t1: continue shopping\n\t2: go to cart\n\tE: exit\n\tchoose: ')
            if action.strip() == '1':
                show_items(session, conn)
                return
            elif action.strip() == '2':
                customer_cart(conn, cart_id, session)
                return
            elif action.lower() == 'e':
                return
            else:
                print(colorama.Fore.RED, 'invalid choice', colorama.Fore.RESET)


def customer_cart(conn, cart_id, session):
    cur = conn.cursor()
    cur.execute('select * from shopping_carts where cart_id = %s and status = %s', (cart_id, 'processing', ))
    cart = cur.fetchone()
    if cart is None:
        print(colorama.Fore.MAGENTA, 'your cart is empty', colorama.Fore.RESET)
    else:
        cur.execute('''select item_stock_code, quantity, stock.item_type, stock.price, stock.stock_off
                        from cart_items_perperson 
                        inner join stock
                        on cart_items_perperson.item_stock_code = stock.stock_id
                        where cart_id = %s''', (cart_id, ))
        cart_items = cur.fetchall()
        if not cart_items:
            print(colorama.Fore.MAGENTA, 'Your cart is empty', colorama.Fore.RESET)
            return

        columns = [desc[0] for desc in cur.description]
        total_price = 0
        total_discount = 0
        item_codes = []
        for row in cart_items:
            row_dict = dict(zip(columns, row))
            item_code = row_dict['item_stock_code']
            item_codes.append(item_code)
            price = float(row_dict['price'])
            off = float(row_dict['stock_off'].strip('%') or 0)
            item_discount = price * (off / 100)
            total_price += price
            total_discount += item_discount

            print(f"Item: {row_dict['item_stock_code']} | Type: {row_dict['item_type']}")
            print(f"Price: {price} | Quantity: {'quantity'} | Off: {off}%")
            print(f"Item Total: {price} | Discount: {item_discount}")
            print('-' * 30)

        total_payment = total_price - total_discount
        print(colorama.Fore.GREEN, f"Total Price: {total_price}", colorama.Fore.RESET)
        print(colorama.Fore.GREEN, f"Total Discount: {total_discount}", colorama.Fore.RESET)
        print(colorama.Fore.GREEN, f"Total Payment Amount: {total_payment}", colorama.Fore.RESET)

        ask = input('\t1: pay\n\t2: continue shopping\n\tE: exit\n\tchoose: ')
        if ask.strip() == '1':
            print('connecting to bank...')
            payment_state = payment()
            if payment_state:
                from datetime import datetime
                order_date = datetime.now()
                cur.execute('''INSERT INTO orders(cart_id, status, order_date, total_price, payment_id)
                                           VALUES(%s, %s, %s, %s, %s)''',
                            (cart_id, 'processing', order_date, total_payment, payment_state))
                for i in cart_items:
                    cur.execute('update stock set stock = stock - %s where stock_id = %s', (1, i[0]))
                cur.execute('UPDATE shopping_carts SET status = %s WHERE cart_id = %s', ('paid', cart_id))

                conn.commit()
                print(colorama.Fore.GREEN, 'order complete, processing your order', colorama.Fore.RESET)
            else:
                print(colorama.Fore.RED, 'Payment failed. Please try again.', colorama.Fore.RESET)
                return
        elif ask.strip() == '2':
            show_items(session, conn)
        elif ask.lower() == 'e':
            return
        else:
            print(colorama.Fore.RED, 'invalid choice', colorama.Fore.RESET)


def payment():
    payment_id = random.randint(1000, 2000)
    return payment_id

def customer_shopping_history(conn, customer_id):
    cur = conn.cursor()
    cur.execute('''
            SELECT 
                orders.order_id, orders.order_date, orders.status,
                shopping_carts.created_at,
                cart_items_perperson.item_stock_code,
                orders.total_price, orders.payment_id,
                stock.item_type, stock.price,stock.stock_off,
                stock.laptop_code, stock.phone_code, stock.camera_code
                
            FROM orders
            INNER JOIN shopping_carts
            ON orders.cart_id = shopping_carts.cart_id
            INNER JOIN cart_items_perperson 
            ON cart_items_perperson.cart_id = shopping_carts.cart_id
            INNER JOIN stock
            ON cart_items_perperson.item_stock_code = stock.stock_id
            WHERE shopping_carts.customer_id = %s and shopping_carts.status = %s
            ORDER BY orders.order_date DESC
        ''', (customer_id, 'paid'))

    orders = cur.fetchall()
    if not orders:
        print(colorama.Fore.MAGENTA, 'No orders found.', colorama.Fore.RESET)
        return

    columns = [desc[0] for desc in cur.description]
    last_order_id = None
    for row in orders:
        row_dict = dict(zip(columns, row))
        if row_dict['order_id'] != last_order_id:
            print('-' * 60)
            print(colorama.Fore.CYAN + f"Order ID: {row_dict['order_id']}" + colorama.Fore.RESET)
            print(f"Date: {row_dict['order_date']} | Status: {row_dict['status']}")
            print(f"Total Order Price: {row_dict['total_price']} | Payment ID: {row_dict['payment_id']}")
            print('-' * 30)
            last_order_id = row_dict['order_id']

        print(f"Item: {row_dict['item_type']}")
        print(f"Price: {row_dict['price']} | Quantity: {1} | Off: {row_dict['stock_off']}")
        print('-' * 30)
        if row_dict['status'] == 'delivered':
            ask = input('\tleave a comment? press y: ')
            if ask.lower() == 'y':
                mongodb.add_comment(conn, row_dict['item_stock_code'])

def customer_search_item(conn, session):
    search_keyword = input('\tsearch: ')
    if not search_keyword:
        print(colorama.Fore.RED, 'search input is empty', colorama.Fore.RESET)
        return
    else:
        keyword_pattern = f"%{search_keyword}%"
        cur = conn.cursor()
        base_query = '''
                SELECT stock.stock_id, stock.item_type, stock.price, stock.stock_off, stock.stock, stock.rating,
                       stock.stock_date,
                       laptop.l_model AS laptop_model, laptop.l_brand AS laptop_brand,
                       phone.p_model AS phone_model, phone.p_brand AS phone_brand,
                       camera.c_model AS camera_model, camera.c_brand AS camera_brand
                FROM stock
                LEFT JOIN laptop 
                ON stock.laptop_code = laptop.laptop_code
                LEFT JOIN phone 
                ON stock.phone_code = phone.phone_code
                LEFT JOIN camera 
                ON stock.camera_code = camera.camera_code
                WHERE (laptop.l_model LIKE %s OR laptop.l_brand LIKE %s
                       OR phone.p_model LIKE %s OR phone.p_brand LIKE %s
                       OR camera.c_model LIKE %s OR camera.c_brand LIKE %s)
                  AND stock.state = 'approved by admin'
            '''

        params = (keyword_pattern, keyword_pattern,
                  keyword_pattern, keyword_pattern,
                  keyword_pattern, keyword_pattern)

        cur.execute(base_query, params)
        rows = cur.fetchall()

        if not rows:
            print(colorama.Fore.RED, "No items found matching your search.", colorama.Fore.RESET)
            return

        columns = [desc[0] for desc in cur.description]
        results = [dict(zip(columns, row)) for row in rows]
        for item in results:
            print(colorama.Fore.CYAN, f"\nStock ID: {item['stock_id']} | Type: {item['item_type']}",
                  colorama.Fore.RESET)
            if item['item_type'] == 'Laptop':
                print(f"\tModel: {item['laptop_model']}, Brand: {item['laptop_brand']}")
            elif item['item_type'] == 'Phone':
                print(f"\tModel: {item['phone_model']}, Brand: {item['phone_brand']}")
            elif item['item_type'] == 'Camera':
                print(f"\tModel: {item['camera_model']}, Brand: {item['camera_brand']}")
            print(
                f"\tPrice: {item['price']}, Stock: {item['stock']}, Discount: {item['stock_off']}, Rating: {item['rating']}")
        while True:
            options = input('\t1: add filters\t\n2: see item\t\nE: exit')
            if options.strip() == '1':
                filters = input(
                    '\t\t1: most expensive\t\t\n2: least expensive\t\t\n3: newest\t\t\n4: oldest\t\t\n5: highest rating\t\t\nchoose: ')
                order_map = {
                    '1': ' ORDER BY stock.price DESC',
                    '2': ' ORDER BY stock.price ASC',
                    '3': ' ORDER BY stock.stock_date DESC',
                    '4': ' ORDER BY stock.stock_date ASC',
                    '5': ' ORDER BY stock.rating DESC'
                }
                order_clause = order_map.get(filters.strip())
                if order_clause:
                    cur.execute(base_query + order_clause, params)
                    rows = cur.fetchall()
                    if rows:
                        print(colorama.Fore.GREEN, "\tFiltered results:", colorama.Fore.RESET)
                        columns = [desc[0] for desc in cur.description]
                        results = [dict(zip(columns, row)) for row in rows]
                        for item in results:
                            print(
                                f"Stock ID: {item['stock_id']} | {item['item_type']} | Price: {item['price']} | Rating: {item['rating']}")
                    else:
                        print(colorama.Fore.RED, "No results after filtering.", colorama.Fore.RESET)
            elif options.strip() == '2':
                stock_id = input("\tEnter the Stock ID of the item you want to see: ")
                cur.execute('select item_type from stock where stock_id = %s', (stock_id, ))
                table = (cur.fetchone())
                if table is None:
                    print(colorama.Fore.RED, "Stock ID not found.", colorama.Fore.RESET)
                    return
                reference_table = table[0].lower()
                cur.execute(f'''
                        (select stock_id, {reference_table}.*, price, stock_off, rating
                        from stock
                        inner join {reference_table}
                        on stock.{reference_table}_code = {reference_table}.{reference_table}_code
                        where stock.stock_id = %s
                        )
                        ''', (stock_id,))
                details = cur.fetchone()
                if details:
                    print("\n=== ITEM DETAILS ===")
                    for col, val in zip(columns, details):
                        print(f"{col:25}: {val}")
                else:
                    print("No record found.")

                action = input('\t\t1: like item\n\t\t2: add item to cart\n\t\tE: exit\n\t\tchoose:')
                if action.strip() == '1':
                    customer_like_item(conn, stock_id, session)
                elif action.strip() == '2':
                    customer_add_to_cart(conn, stock_id, session)
                elif action.lower() == 'e':
                    break
                else:
                    print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
                    continue
            elif options.lower() == 'e':
                return
            else:
                print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
                continue

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
    ad = address['Province'] + ',' + address['City'] + ',' + address['Address'] + ',' + address['NO'] + ',' + address['Unit']
    return ad


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
    while True:
        email_ad = input('\temail address: ').strip()
        if not email_ad:
            print(colorama.Fore.RED, 'Field empty', colorama.Fore.RESET)
            continue

        if email_ad.count('@') != 1:
            print(colorama.Fore.RED, 'Email must contain exactly one @', colorama.Fore.RESET)
            continue

        local_part, domain_part = email_ad.split('@')

        pattern_local = r'^[a-zA-Z0-9._-]+$'
        if not re.match(pattern_local, local_part):
            print(colorama.Fore.RED, 'Invalid email username', colorama.Fore.RESET)
            continue

        domain_sections = domain_part.rsplit('.', 1)
        if len(domain_sections) != 2:
            print(colorama.Fore.RED, 'Email must contain a dot in the domain', colorama.Fore.RESET)
            continue

        domain_name, domain_ext = domain_sections
        if domain_name.lower() not in data.valid_email_domains or domain_ext.lower() not in data.valid_email_endings:
            print(colorama.Fore.RED, f'Domain {domain_name} or extension {domain_ext} not valid', colorama.Fore.RESET)
            continue

        print(colorama.Fore.GREEN, 'Valid email address', colorama.Fore.RESET)
        return email_ad


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

def see_all_employees(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM employee')
    employees = cur.fetchall()
    if not employees:
        print(colorama.Fore.MAGENTA, 'No employees found.', colorama.Fore.RESET)
        return
    headers = [desc[0] for desc in cur.description]
    print(colorama.Fore.CYAN + '\n=== All Employees ===' + colorama.Fore.RESET)
    print(tabulate(employees, headers=headers, tablefmt='fancy_grid'))


def see_all_sellers(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM seller')
    sellers = cur.fetchall()
    if not sellers:
        print(colorama.Fore.MAGENTA, 'No sellers found.', colorama.Fore.RESET)
        return
    headers = [desc[0] for desc in cur.description]
    print(colorama.Fore.CYAN + '\n=== All Sellers ===' + colorama.Fore.RESET)
    print(tabulate(sellers, headers=headers, tablefmt='fancy_grid'))


def see_all_customers(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM customer')
    customers = cur.fetchall()
    if not customers:
        print(colorama.Fore.MAGENTA, 'No customers found.', colorama.Fore.RESET)
        return
    headers = [desc[0] for desc in cur.description]
    print(colorama.Fore.CYAN + '\n=== All Customers ===' + colorama.Fore.RESET)
    print(tabulate(customers, headers=headers, tablefmt='fancy_grid'))


def see_all_admins(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM admin')
    admins = cur.fetchall()
    if not admins:
        print(colorama.Fore.MAGENTA, 'No admins found.', colorama.Fore.RESET)
        return
    headers = [desc[0] for desc in cur.description]
    print(colorama.Fore.CYAN + '\n=== All Admins ===' + colorama.Fore.RESET)
    print(tabulate(admins, headers=headers, tablefmt='fancy_grid'))

def see_all_orders(conn):
    cur = conn.cursor()
    cur.execute('''
        SELECT 
            orders.order_id,
            orders.order_date,
            orders.status,
            orders.total_price,
            orders.payment_id,
            customer.cust_id,
            customer.cust_name,
            customer.cust_lname
        FROM orders 
        INNER JOIN shopping_carts 
        ON orders.cart_id = shopping_carts.cart_id
        INNER JOIN customer 
        ON shopping_carts.customer_id = customer.cust_id
        ORDER BY orders.order_date DESC
    ''')
    orders = cur.fetchall()
    if not orders:
        print(colorama.Fore.MAGENTA, 'No orders found.', colorama.Fore.RESET)
        return
    headers = [desc[0] for desc in cur.description]
    print(colorama.Fore.CYAN + '\n=== All Orders ===' + colorama.Fore.RESET)
    print(tabulate(orders, headers=headers, tablefmt='fancy_grid'))

if __name__ == '__main__':
    print('not the main file')












