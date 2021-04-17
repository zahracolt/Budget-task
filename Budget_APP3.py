"""
Budget App
Create a Budget class that can instantiate objects based on different budget categories like
food, clothing, and entertainment. These objects should allow for
1.  Depositing funds to each of the categories
2.  Withdrawing funds from each category
3.  Computing category balances
4.  Transferring balance amounts between categories
"""


database = {}


class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(amount, bal):
        bal += amount
        return bal

    def withdraw(user, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        valuue2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(valuue2) + amount
        return db


def init():
    print('=== **** Welcome to the Budget App**** ===')
    menu()


def menu():
    try:

        user = int(input(
            ' **** Select: **  1 (To create a new budget) 2 (To deposit) 3 (To withdraw) 4 (To check balance) 5 (To transfer money) 6 (To quit)\n'))
    except:
        print('Invalid input, please try again')
        menu()

    if user == 1:
        new_budget()
    elif user == 2:
        credit()
    elif user == 3:
        debit()
    elif user == 4:
        balance()
    elif user == 5:
        transfer()
    elif user == 6:
        out()
    else:
        print('Invalid option, please try again\n')
        menu()


def new_budget():
    print(" *** Creating a New Budget ****\n")
    budget_title = int(input("Select 1 (food) 2 (Clothing) 3 (Entertainment) \n"))
    if budget_title == 1:
        budget_title = 'Food'
    elif budget_title == 2:
        budget_title = 'Clothing'
    elif budget_title == 3:
        budget_title = 'Entertainment'
    else:
        print('Invalid option, please try again')
        new_budget()
    try:
        amount = int(input(f"Enter your {budget_title} budget amount \n$"))
    except:
        print('\nInvalid input, please try again')
        new_budget()
    budget = Budget(budget_title, amount)
    database[budget_title] = amount
    print('')
    print(f'Budget {budget_title} was setup with ${amount}')
    print("= " * 30)
    print("Do you need another transaction")
    select = int(input("Select 1 (Yes) 2 (NO)"))
    if select == 1:
        menu()
    elif select == 2:
        out()


def debit():
    print("=== **** Withdraw **** ===\n")
    print('**** Available Budgets ****')

    for key, value in database.items():
        print(f"-  {key}")

    pick = int(input('\nPress (1) To continue with your debit transaction\nPress (2) To stop debit transaction\n'))
    if pick == 1:
        user = input("\n**** Select one of budget ****\n")
        if user in database:
            print('Note: You can not withdraw all your budget, at least $1 must remain.')
            amt = int(input("Enter amount to withdraw \n$"))
            if amt < database[user]:
                balance = int(database[user])
                new_balance = Budget.withdraw(user, amt, balance)
                database[user] = new_balance
                print(f"${amt} has been debited from Budget-{user}\nBudget amount remaining ${new_balance}")
                menu()

            else:
                pick = int(input(
                    f'\nBudget {user} is insufficient of the ${amt} required\nThe actual balance {database[user]}\n\nPress (1) To deposit to the budget\nPress (2) To choose the right budget\n'))
                if pick == 1:
                    amt = int(input("Enter amount \n$"))
                    balance = int(database[user])
                    new_balance = Budget.deposit(amt, balance)
                    database[user] = new_balance
                    print('')
                    print(f"Budgets {user} has been credited with ${amt}\n")
                    debit()

                elif pick == 2:
                    debit()
                else:
                    print('Invalid option\n')
                    debit()
        else:
            pick = int(input(
                f'\n****  Budget {user} does not exist! ****\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
            if pick == 1:
                new_budget()
            elif pick == 2:
                debit()
            elif pick == 3:
                print('')
                menu()
            else:
                print('Invalid option\n')
                debit()
    elif pick == 2:
        print('\nYou have terminated the debit transaction ')
        menu()
    else:
        print('\nInvalid option')
        debit()


def credit():
    print("**** Deposit ****")

    pick = int(input('Select 1) To continue with your deposit transaction 2) To stop deposit transaction\n'))
    if pick == 1:
        print('**** Available Budgets ****')
        for key, value in database.items():
            print(f"-  {key}")
        user = input("Select one of the above budget \n")
        if user in database:
            amt = int(input("Enter amount to deposit \n$"))
            balance = int(database[user])
            new_balance = Budget.deposit(amt, balance)
            database[user] = new_balance
            print(f'You have deposited ${amt} to {user} budget\n Total Budget amount is now ${new_balance}')
            print("Do you need another transaction")
            select = int(input("Select 1 (Yes) 2 (NO)"))
            if select == 1:
                menu()
            elif select == 2:
                out()


        else:
            print('')
            pick = int(input(f'{user} budget does not exist!\n {menu()}\n'))
            if pick == 1:
                new_budget()
            elif pick == 2:
                credit()
            elif pick == 3:
                menu()
            else:
                print('Invalid option, please try again\n')
                credit()

    elif pick == 2:
        print('You terminated the deposit transaction')
        menu()
    else:
        print('\nInvalid option, please try again')
        menu()


def balance():
    print("*** Check Budget Balances ***")
    check_bal = Budget.balance(database)
    if check_bal == None:
        print('')
        menu()
    else:
        print(f'${check_bal}')
        menu()


def transfer():
    print('**** Available and Valid Budgets ****')
    for key, value in database.items():
        print(key)
    from_budget = input("Select one of the budget above you are transfering from \n")
    if from_budget in database:
        from_amount = int(input("Enter amount you want to transfer \n$"))
        if from_amount < database[from_budget]:
            to_budget = input("Enter destination of funds (Food) (Clothing) (Entertainment) \n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print("")
                print(f"You transfered ${from_amount} from {from_budget} to {to_budget} ")
                for key, value in db.items():
                    print(key, value)
                menu()
            else:
                print(f'\n{from_budget} Budget does not exist, please choose from the valid budget below\n')
                transfer()
        else:
            print(f'You do not have such amount-${from_amount} in {from_budget} budget')
            transfer()
    else:
        print(f'Budget {from_budget} does not exist\n')

        transfer()


def out():
    try:
        pick = int(input('Are you sure you want to quit? 1 to quit  2 to continue\n'))
    except:
        print('Invalid input, Please try again')
        out()

    if pick == 1:
        print("Thank you for choosing the budget app.")
        quit()
    elif pick == 2:
        menu()
    else:
        print('Invalid input, please try again')
        out()


init()
