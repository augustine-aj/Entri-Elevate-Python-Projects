import csv  # Reading and writing CSV
import time  # Simulate loading and processing times
import os   # For database operations
from colorama import Fore, Style    # For colorful command line interface

# Main operations
'''
Depositing money, checking balance, changing account details and more.
'''

# Key features
'''
User authentication, account operations, data storing, colorful CLI.
'''

file_path = 'user_data.csv'

user_data = {}
login_data = {}
user_name = ''


def func_connecting():
    print(Style.BRIGHT + Fore.GREEN + 'Connecting to Bank server' + Style.RESET_ALL, end='')
    for i in range(3):
        print(Fore.GREEN + '.' + Fore.RESET, end='', flush=True)
        time.sleep(1)
    print('\n', end='')


def func_loading():
    print(Style.BRIGHT + Fore.GREEN + '\nLoading' + Style.RESET_ALL, end='')
    for i in range(3):
        print(Fore.GREEN + '.' + Fore.RESET, end='', flush=True)
        time.sleep(1)
    print('\n', end='')


def update_database():
    file_exists = os.path.exists(file_path)

    with open(file_path, 'w', newline='') as file:
        fieldnames = ['username', 'password', 'balance', 'email', 'fullname', 'mobile']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for user, data in user_data.items():
            writer.writerow({
                'username': user,
                'password': data['password'],
                'balance': data['balance'],
                'email': data['email'],
                'fullname': data['fullname'],
                'mobile': data['mobile']
            })


def update_balance():
    global user_name
    if user_name in user_data:
        update_database()

    else:
        print(Fore.YELLOW + "WARNING : Bank server is busy.")


def add_deposit():
    global login_data, user_name
    while True:
        print(Fore.MAGENTA + '\nEnter the amount to deposit : ' + Fore.RESET, end='', flush=True)
        try:
            deposit_amount = int(input())
        except ValueError:
            print(Fore.RED + 'ERROR : Enter a valid deposit amount.' + Fore.RESET)
            continue

        if deposit_amount > 100000:
            print(Fore.YELLOW + "WARNING : Can't deposit more than 100000."
                                "\nTo deposit more than 100000 visit our nearest branch." + Fore.RESET)
            continue
        elif deposit_amount <= 0:
            print(Fore.YELLOW + 'WARNING : Enter a valid amount.' + Fore.RESET)
            continue

        login_data['balance'] += deposit_amount
        # print(login_data)
        update_balance()

        inner_iteration = 0
        while True:
            if inner_iteration == 0:
                print(Fore.GREEN + 'You have deposited successfully. ' + Fore.RESET)

            print('-' * 40)
            print(Style.BRIGHT + Fore.MAGENTA + '\n\n1 - DEPOSIT MORE', ' ' * 10,
                  '2 - BALANCE ENQUIRY', ' ' * 10, '3 - MENU', ' ' * 10
                  + Style.RESET_ALL)
            userinput = 0

            try:
                userinput = int(input('\nChoose an option : '))
            except ValueError:
                print(Fore.RED + 'ERROR : Invalid input. Choose a valid number.' + Fore.RESET)
                inner_iteration += 1
                continue
            if userinput == 3:
                print('-' * 40)
                return
            elif userinput == 1:
                break
            elif userinput == 2:
                balance_enquiry()
                inner_iteration += 1
            else:
                print(Fore.RED + 'ERROR : Wrong input. Choose a valid number.' + Fore.RESET)
                inner_iteration += 1


def check_password():
    password_attempt = 3
    while True:
        if password_attempt == 0:
            print(Style.BRIGHT + Fore.RED + f'Dear {user_name}, YOUR ACCOUNT HAS BEEN RESTRICTED '
                                            f'FOR 24 HOURS.\nDUE TO TOO MANY UNSUCCESSFUL LOGIN ATTEMPTS.\n'
                                            f'CONTACT OUR CUSTOMER ASSISTANCE FOR ANY ASSISTANCE.'
                  + Style.RESET_ALL)
            quit()
        password_input = input(Fore.GREEN + 'Enter your password : ' + Fore.RESET)
        if password_input != login_data['password']:
            print(Fore.RED + '\nERROR : Wrong password. ' + Fore.RESET)
            print('current pass', login_data['password'])
            password_attempt -= 1
        else:
            return password_input


def update_username():
    global login_data, user_name
    iteration = 0
    while True:
        if iteration == 0:
            print('-' * 40)
        new_username = input(Fore.GREEN + '\nEnter new username : ' + Fore.RESET)
        if new_username == user_name:
            print(Fore.RED + 'ERROR : New username and old user name are same. Create a new one.' + Fore.RESET)
            iteration += 1
            continue
        confirm_username = input(Fore.GREEN + 'Confirm new username : ' + Fore.RESET)

        if new_username == confirm_username:
            check_password()
            user_data[new_username] = user_data.pop(user_name)
            user_name = new_username
            update_database()
            print(Fore.GREEN + 'Username changed successfully.' + Fore.RESET)
            print('-' * 40 + Style.RESET_ALL + '\n')

            return
        else:
            print(Fore.RED + 'ERROR : New username and confirm username must be same.' + Fore.RESET)
            iteration += 1
            continue


def update_password():
    global login_data, user_name
    print('username is ', user_name)
    iteration = 0
    while True:
        if iteration == 0:
            print('-' * 40)
        current_password = check_password()
        new_password = input(Fore.GREEN + '\nEnter new password : ' + Fore.RESET)
        if new_password == current_password:
            print(Fore.RED + 'ERROR : Current password and new password must be same. ' + Fore.RESET)
            iteration += 1
            continue
        confirm_password = input(Fore.GREEN + 'Confirm new password : ' + Fore.RESET)
        if new_password == confirm_password:
            user_data[user_name]['password'] = new_password
            update_database()
            print(Fore.GREEN + 'Password changed successfully.' + Fore.RESET)
            print('-' * 40 + Style.RESET_ALL + '\n')
            return
        else:
            print(Fore.RED + 'ERROR : New password and confirm password must be same.' + Fore.RESET)
            iteration += 1


def update_email():
    global login_data, user_name
    iteration = 0
    while True:
        if iteration == 0:
            print('-' * 40)
        if login_data['email'] is not None:
            current_email = input(Fore.GREEN + '\nCurrent Email : ' + Fore.RESET)
            if current_email != login_data['email']:
                print(Fore.RED + '\nERROR : Wrong email. ' + Fore.RESET)
                iteration += 1
                continue
            new_email = input(Fore.GREEN + '\nNew Email : ' + Fore.RESET)
            confirm_email = input(Fore.GREEN + 'Confirm Email : ' + Fore.RESET)
            if new_email == confirm_email:
                user_data[user_name]['email'] = new_email
                print(Fore.GREEN + '\nFor verification' + Fore.RESET)
                check_password()
                update_database()
                print(Fore.GREEN + 'Email changed successfully.' + Fore.RESET)
                print('-' * 40 + Style.RESET_ALL + '\n')
                return
            else:
                print(Fore.RED + 'ERROR : New email and confirm email must be same.' + Fore.RESET)
                iteration += 1


def update_mobile():
    global login_data, user_name
    iteration = 0
    while True:
        if iteration == 0:
            print('-' * 40)
        if login_data['mobile'] is not None:
            current_mobile = input(Fore.GREEN + '\nEnter mobile number : ' + Fore.RESET)
            if current_mobile != login_data['mobile']:
                print(Fore.RED + 'ERROR : Wrong mobile number. ' + Fore.RESET)
                iteration += 1
                continue
            new_mobile = input(Fore.GREEN + '\nNew mobile number : ' + Fore.RESET)
            confirm_mobile = input(Fore.GREEN + 'confirm mobile number : ' + Fore.RESET)
            if new_mobile == confirm_mobile:
                user_data[user_name]['mobile'] = new_mobile
                print(Fore.GREEN + 'For verification' + Fore.RESET)
                check_password()
                update_database()
                print(Fore.GREEN + 'Mobile number changed successfully.' + Fore.RESET)
                print('-' * 40 + Style.RESET_ALL + '\n')
                return
            else:
                print(Fore.RED + 'ERROR : New mobile and confirm mobile must be same.' + Fore.RESET)
                iteration += 1


def accountInfo_inputHandler(user_input, ):
    if user_input == 1:
        update_username()
    elif user_input == 2:
        update_password()
    elif user_input == 3:
        update_email()
    elif user_input == 4:
        update_mobile()
    return


def display_accountInfo():
    global login_data, user_name
    print(Style.BRIGHT + Fore.BLUE + '-' * 80)
    print(' ' * 32 + 'ACCOUNT DETAILS')
    print('-' * 80, '\n' + Style.RESET_ALL)
    print(Fore.MAGENTA + ' ' * 29, f"BALANCE = {login_data['balance']}\n" + Fore.RESET)
    print(Style.BRIGHT + Fore.YELLOW + f'USERNAME : {user_name}', ' ' * 38, Style.RESET_ALL,
          Fore.LIGHTGREEN_EX + '1 - Change username' + Fore.RESET)
    print(Style.BRIGHT + Fore.YELLOW + 'ACCOUNT NUMBER', ' ' * 40, Style.RESET_ALL,
          Fore.LIGHTGREEN_EX + '2 - Change password' + Fore.RESET)
    print(Style.BRIGHT + Fore.YELLOW + f"EMAIL ID : {login_data['email']}", ' ' * 26, Style.RESET_ALL,
          Fore.LIGHTGREEN_EX + '3 - Change email id' + Fore.RESET)
    print(Style.BRIGHT + Fore.YELLOW + f"FULL NAME: {login_data['fullname']}" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + f"MOBILE NUMBER : {login_data['mobile']}", ' ' * 28, Style.RESET_ALL,
          Fore.LIGHTGREEN_EX + '4 - Change mobile' + Fore.RESET)
    print()
    print('-' * 45 + Fore.RED + '0 - HOME' + Fore.RESET)
    print('\n')


def display_accountDetails():
    global login_data, user_name
    iteration = 0
    while True:
        if iteration == 0:
            display_accountInfo()
        try:
            user_input = int(input('\nChoose an option : '))
        except ValueError:
            print(Fore.RED + 'ERROR : Invalid input. Choose a valid number.' + Fore.RESET)
            iteration += 1
            continue

        if user_input == 0:
            print('-' * 40)
            return
        elif user_input < 0 or user_input > 4:
            print(Fore.RED + 'ERROR : Wrong input. Choose a valid number.' + Fore.RESET)
            iteration += 1
            continue
        else:
            accountInfo_inputHandler(user_input)
            iteration = 0


def balance_enquiry():
    global login_data
    print(Fore.YELLOW + f"\nYour current balance is : {login_data['balance']}" + Fore.RESET)
    time.sleep(3)
    return


def mini_statement():
    print('_' * 40, '\n')
    print(Fore.YELLOW + 'WARNING : We will update this soon...\n' + Fore.RESET)
    print('-' * 40)
    print()
    time.sleep(2)


def cash_withdrawal():
    global login_data, user_name
    daily_limit = 50000
    while True:
        print(Fore.MAGENTA + '\nEnter the amount to withdraw : ' + Fore.RESET, end='', flush=True)
        try:
            withdraw_amount = int(input())
        except ValueError:
            print(Fore.RED + 'ERROR : Enter a valid withdraw amount.' + Fore.RESET)
            continue

        if withdraw_amount > login_data['balance']:
            balance_enquiry()
            return
        elif withdraw_amount <= 0:
            print(Fore.YELLOW + 'WARNING : Enter a valid amount.' + Fore.RESET)
            continue
        elif withdraw_amount > 20000:
            print(Fore.YELLOW + "WARNING : Can't withdraw more than 20000 in a single transaction." + Fore.RESET)
            continue
        elif daily_limit <= 0:
            print(Fore.YELLOW + f'WARNING : Withdrawal limit is {withdraw_amount - daily_limit}.' + Fore.RESET)
            continue

        login_data['balance'] -= withdraw_amount
        daily_limit -= withdraw_amount
        update_balance()

        inner_iteration = 0
        while True:
            if inner_iteration == 0:
                print(Fore.GREEN + '\nTransaction completed. ' + Fore.RESET)

            print('-' * 40)
            print(Style.BRIGHT + Fore.MAGENTA + '\n\n1 - WITHDRAW MORE', ' ' * 10,
                  '2 - BALANCE ENQUIRY', ' ' * 10, '3 - HOME', ' ' * 10
                  + Style.RESET_ALL)
            userinput = 0
            try:
                userinput = int(input('\nChoose an option : '))
            except ValueError:
                print(Fore.RED + 'ERROR : Invalid input. Choose a valid number.' + Fore.RESET)
            if userinput == 3:
                return
            elif userinput == 1:
                break
            elif userinput == 2:
                balance_enquiry()
                inner_iteration += 1
            else:
                print(Fore.RED + 'ERROR : Wrong input. Choose a valid number.' + Fore.RESET)
                inner_iteration += 1


def menu_inputHandler(userInput):
    if userInput == 1:
        add_deposit()
    elif userInput == 2:
        display_accountDetails()
    elif userInput == 3:
        balance_enquiry()
    elif userInput == 4:
        mini_statement()
    elif userInput == 5:
        cash_withdrawal()


def account_menu():
    while True:
        print(Style.BRIGHT + Fore.BLUE + '-' * 80)
        print(Style.BRIGHT + Fore.GREEN + '\n1 - ADD DEPOSIT', ' ' * 24, '2 - ACCOUNT DETAILS',
              '\n3 - BALANCE ENQUIRY', ' ' * 20, '4 - MINI STATEMENT',
              '\n5 - CASH WITHDRAWAL', ' ' * 20, '6 - HOME'
              + Style.RESET_ALL)
        try:
            userinput = int(input('\nChoose an option : '))
        except ValueError:
            print(Fore.RED + 'ERROR : Invalid input. Choose a valid number.' + Fore.RESET)
            continue
        if userinput == 6:
            func_loading()
            print('-' * 40)
            return
        elif userinput <= 0 or userinput > 6:
            print(Fore.RED + 'ERROR : Wrong input. Choose a valid number.' + Fore.RESET)
            continue
        else:
            menu_inputHandler(userinput)


def login_check():
    global login_data, user_name
    while True:
        user_name = input(Style.BRIGHT + Fore.GREEN + 'USER NAME : ' + Style.RESET_ALL)
        if user_name in user_data:
            password_attempt = 3
            while True:
                password = input(Style.BRIGHT + Fore.GREEN + 'PASSWORD : ' + Style.RESET_ALL)
                if user_name in user_data and password == user_data[user_name]['password']:
                    login_data = user_data[user_name]
                    # print(login_data)
                    account_menu()
                    return
                else:
                    password_attempt -= 1
                    if password_attempt == 0:
                        print(Style.BRIGHT + Fore.RED + f'Dear {user_name}, YOUR ACCOUNT HAS BEEN RESTRICTED '
                                                        f'FOR 24 HOURS.\nDUE TO TOO MANY UNSUCCESSFUL LOGIN ATTEMPTS.\n'
                                                        f'CONTACT OUR CUSTOMER ASSISTANCE FOR ANY ASSISTANCE.'
                              + Style.RESET_ALL)
                        return
                    else:
                        print(
                            Fore.RED + f'ERROR : Invalid password. Available password attempt is {password_attempt}.'
                            + Fore.RED)
                        continue
        else:
            print(Fore.RED + 'ERROR : Invalid user name, Please try again..')


def load_userdata():
    with open(file_path, 'r') as file:
        read_file = csv.DictReader(file)
        for users in read_file:
            user_data[users['username']] = {'password': users['password'],
                                            'balance': float(users['balance']),
                                            'email': users['email'],
                                            'fullname': users['fullname'],
                                            'mobile': users['mobile']}
    return user_data


def home():
    global user_data
    home_iteration = 0
    while True:
        user_data = load_userdata()
        print(Style.BRIGHT + Fore.BLUE + '\n\n', '-' * 25, 'ABC BANK ONLINE', '-' * 25,
              '\n\n', 'HOME ', ' ' * 42, 'ESC key --> Quit\n'
              + Style.RESET_ALL, sep='')
        #print(user_data)
        if home_iteration == 0:
            func_connecting()

        print(Style.BRIGHT + Fore.GREEN + 'Connected to Bank server\n' + Style.RESET_ALL, end='')
        print('-' * 40)
        login_check()
        home_iteration += 1
        continue


if __name__ == '__main__':
    home()
