import Funcs
import colorama
import database
import data
from Funcs import admin_check_access
from database import create_main_admin_account
import mongodb
session = {
    "logged_in": False,
    "cust_id": None,
    "temp_cart": []
}

run = database.connect_mysql()
if not run:
    print(colorama.Fore.RED, 'could not connect to MySQL', colorama.Fore.RESET)
else:
    database_check = database.check_database_onlineshop(run)
    if not database_check:
        database.create_database_onlineshop(run)
    conn = database.connect_onlineshop()
    tables_check = database.check_database_tables(conn)
    if not tables_check:
        print(colorama.Fore.RED, 'tables missing, creating database again')
        database.create_database_tables(conn)
    print(colorama.Fore.GREEN, 'connection complete', colorama.Fore.RESET)

    while True:

        front_page_menu = ['1: Items', '2: Search', '3: Log in', '4: Sign up']
        for i in front_page_menu:
            print(colorama.Fore.BLUE, f'\t{i}', colorama.Fore.RESET)
        front_page_menu_choice = input('\tChoose: ')
        # ------------------------- items -----------------------------
        if front_page_menu_choice.strip() == '1':
            Funcs.show_items(session, conn)
        # ------------------------- search ----------------------------
        elif front_page_menu_choice.strip() == '2':
            Funcs.customer_search_item(conn, session)
        # ------------------------- log in -----------------------------
        elif front_page_menu_choice.strip() == '3':
            log_in_person = ['1: admin', '2: employee', '3: customer', '4: seller', 'E: exit']
            for i in log_in_person:
                print(colorama.Fore.BLUE, f'\t{i}', colorama.Fore.RESET)
            log_in_choice = input('\tChoose: ')
            if log_in_choice.strip() == '1':
                admin = Funcs.admin_check_access(conn)
                if admin:
                    Funcs.all_admin_actions(conn, admin)
                else:
                    print(colorama.Fore.RED, 'log in unsuccessful', colorama.Fore.RESET)
            elif log_in_choice.strip() == '2':
                employee = Funcs.employee_log_in(conn)
                if employee:
                    Funcs.all_employee_actions(conn, employee)
                else:
                    print(colorama.Fore.RED, 'log in unsuccessful', colorama.Fore.RESET)
            elif log_in_choice.strip() == '3':
                customer = Funcs.customer_log_in(conn, session)
                if customer:
                    Funcs.all_customer_actions(conn, customer, session)
                else:
                    print(colorama.Fore.RED, 'log in unsuccessful', colorama.Fore.RESET)
            elif log_in_choice.strip() == '4':
                seller = Funcs.seller_log_in(conn)
                if seller:
                    Funcs.all_seller_actions(conn, seller)
                else:
                    print(colorama.Fore.RED, 'log in unsuccessful', colorama.Fore.RESET)
            elif log_in_choice.lower() == 'e':
                break
            else:
                print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
        # ------------------------- sign up -----------------------------
        elif front_page_menu_choice.strip() == '4':
            choice = input('\t1: customer\n\t2: seller\n\tE: exit\n\tchoose: ')
            if choice.strip() == '1':
                Funcs.customer_sign_up(conn, session)
            elif choice.strip() == '2':
                Funcs.seller_sign_up(conn)
            elif choice.lower() == 'e':
                break
            else:
                print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)

        # ------------------------- wrong input -----------------------------
        else:
            print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
