import Funcs
import json
import colorama
import OOP
session = {
    "logged_in": False,
    "user_index": None,
    "username": None,
}

while True:
    front_page_menu = ['1: Sign up', '2: Log in admin', '3: Log in employee', '4: Log in Customer', "5: items", "6: search"]
    for i in front_page_menu:
        print(colorama.Fore.BLUE, f'\t{i}', colorama.Fore.RESET)
    front_page_menu_choice = input('\tChoose: ')
# ------------------------- sign up -----------------------------
    if front_page_menu_choice.strip() == '1':
        Funcs.customer_sign_up()
# ------------------------- log in ------------------------------
# ------------------------- customer ----------------------------
    elif front_page_menu_choice.strip() == '4':
        ind = Funcs.customer_log_in(session)
        if ind is not None:
            Funcs.all_customer_actions(ind, session)
# ------------------------- employee -----------------------------
    elif front_page_menu_choice.strip() == '3':
        user_pass_check = Funcs.employee_log_in()
# ------------------------- admin -----------------------------
    elif front_page_menu_choice.strip() == '2':
        user_pass_check = Funcs.admin_check_access()
# -------------------------------------------------------------
# ------------------------- items -----------------------------
    elif front_page_menu_choice.strip() == '5':
        Funcs.show_items(session)

    elif front_page_menu_choice.strip() == '6':
        Funcs.customer_search_item(session)
# ------------------------- wrong input -----------------------------
    else:
        print(colorama.Fore.RED, 'wrong input', colorama.Fore.RESET)
