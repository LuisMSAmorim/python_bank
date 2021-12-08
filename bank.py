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
        bank.manager_reports(transactions)
    else:
        print('Até logo...')
        bank.save_all(transactions)
        break
