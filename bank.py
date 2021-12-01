import functions as bank


transactions = []
database_data = bank.get_all()
transactions = database_data
print('Bem vindo ao banco... \n')
while True:
    option = bank.principal_menu()
    if(option == 1):
        bank.create_account(transactions)    
    elif(option == 2):
        bank.change_account_balance(transactions)
    elif(option == 3):
        bank.remove_account(transactions)
    elif(option == 4):
        manager_reports_option = bank.manager_reports_menu()
        if(manager_reports_option == 1):
            bank.select_negative_accounts(transactions)
        elif(manager_reports_option == 2):
            bank.select_accounts_by_min_balance(transactions)
        elif(manager_reports_option == 3):
            bank.select_all_accounts(transactions)
        else:
            pass
    else:
        print('Até logo...')
        bank.save_all(transactions)
        break
