database = '/home/luis/Documentos/infnet/logicaComputacaoEAlgoritmos/assessment/contas.txt'

# "Database" get and save functions
def get_all():
    transaction = []
    with open(database, 'r') as accounts:
        line = accounts.readline()
        while(line != ''):
            line = line.strip('\n').split(';')
            account_number = int(line[0])
            account_user = line[1]
            account_balance = float(line[2])
            account = [account_number, account_user, account_balance]
            transaction.append(account)
            line = accounts.readline()
    return transaction

def save_all(array):
    with open(database, 'w') as accounts:
        for account in array:
            accounts.write(f'{int(account[0])};{account[1]};{float(account[2])}\n')

# Menu functions
def principal_menu():
    while True:
        print('-----MENU-----')
        print('[1] Inclusão de conta')
        print('[2] Alteração de saldo')
        print('[3] Exclusão de conta')
        print('[4] Relatórios gerenciais')
        print('[5] Encerrar programa')
        print('-------------- \n')
        option = enter_integer_number('Digite sua opção: ')
        if((option > 5) or (option < 1)):
            print('[ERRO] Opção inválida, tente novamente...')
        else:
            return option

def manager_reports_menu():
    while True:
        print('-----MENU DE RELATÓRIOS GERENCIAIS-----')
        print('[1] Listar clientes com saldo negativo')
        print('[2] Listar clientes a partir de determinado valor')
        print('[3] Listar todos os clientes')
        print('[4] Retornar ao menu principal')
        print('-----------------------------------------')
        option = enter_integer_number('Digite sua opção: ')
        if((option > 4) or (option < 1)):
            print('[ERRO] Opção inválida, tente novamente...')
        else:
            return option

# Primary Functions
def enter_integer_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('[ERRO] Número inválido...')

def enter_float_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print('[ERRO] Número inválido...')

# passar mensagem com parâmetro
def enter_account_number():
     while True:
        account_number = enter_integer_number('Digite o número desejado para sua conta: ')
        if(account_number <= 0):
            print('[ERRO] O número deve ser maior que 0 (zero)...')
        else:
            return account_number

def enter_update_value():
    while True:
        update_value = enter_float_number('Digite o valor da transação: ')
        if(update_value <= 0):
            print('[ERRO] Você deve digitar um valor positivo')
        else:
            return update_value

def enter_balance_update_type():
    while True:
        update_type = enter_integer_number('Você deseja inserir ou remover fundos da sua conta? \n [1] Inserir \n [2] remover: \n')
        if((update_type != 1) and (update_type != 2)):
            print('[ERRO] Opção inválida...')
        else:
            return update_type

def find_index(array, account_number):
    cont = 0
    for account in array:
        cont += 1
        if(account[0] == account_number):
            return (cont - 1)
    return (-1)

def set_account_number(array):
    while True:
        account_number = enter_account_number()
        account_number_exists = find_index(array, account_number)
        if(account_number_exists == -1):
            return account_number
        print('[ERRO] Este número de conta já está em uso, insira outro...')

def set_account_name():
    while True:
        account_user = str(input('Digite seu nome completo: '))
        name_split = account_user.split()
        if(len(name_split) < 2):
            print('[ERRO] Por favor, digite seu nome completo para prosseguir!')
        else:
            return account_user

def set_initial_balance():
    while True:
        initial_balance = enter_float_number('Digite o valor que você deseja depositar para abrir sua conta: ')
        if(initial_balance < 0):
            print('[ERRO] Valores negativos não são permitidos...')
        else:
            return initial_balance

# Secundary functions
def create_account(array):
    account_number = set_account_number(array) 
    account_name = set_account_name()
    initial_balance = set_initial_balance()
    account = [account_number, account_name, initial_balance]
    array.append(account)
    print('Conta registrada...')

def remove_account(array):
    while True:
        account_number = enter_account_number('Digite o número da conta que deseja excluir: ')
        index = find_index(array, account_number)
        if(index == -1):
            print('[ERRO] Não foi encontrada nenhuma conta com este número...')
        else:
            if(array[index][2] != 0):
                print('[ERRO] Para realizar esta operação o saldo da conta deve ser igual a 0')
                return    
            array.pop(index)
            return

def change_account_balance(array):
    while True:
        account_number = enter_account_number('Digite o número da conta que você deseja alterar o saldo:')
        index = find_index(array, account_number)
        if(index == -1):
            print('[ERRO] Não foi encontrada nenhuma conta com este número...')
        else:
            actual_value = array[index][2]
            update_type = enter_balance_update_type()
            update_value = enter_update_value()
            if(update_type == 1):
                new_balance = (actual_value + update_value)
            else:
                new_balance = (actual_value - update_value)
            array[index][2] = new_balance
            print('Saldo alterado...')
            return 

def select_negative_accounts(array):
    cont = 0
    if(len(array) == 0):
        print('Não há contas cadastradas... \n')
        return
    for account in array:
        if(account[2] < 0):
            cont += 1
            print(f'{account} \n')
    if(cont == 0):
        print('Não foram encontradas contas com saldo negativo \n')
        return

def select_accounts_by_min_balance(array):
    cont = 0
    if(len(array) == 0):
        print('Não há contas cadastradas... \n')
        return
    min_value = enter_float_number('Digite um valor e receba todas as contas com saldo acima do mesmo: ')
    for account in array:
        if(account[2] > min_value):
            cont += 1
            print(f'{account} \n')
    if(cont == 0):
        print(f'Não foram encontradas contas com saldo acima de R${min_value} \n')
        return
    
def select_all_accounts(array):
    if(len(array) == 0):
        print('Não há contas cadastradas... \n')
        return
    print('----------Contas registradas---------- \n')
    print('|N° da conta | Nome do correntista | Saldo da conta| \n')
    for account in array:
        print(f'{account} \n')
    print('-------------------------------------- \n')

def manager_reports(array):
    option = manager_reports_menu()
    if(option == 1):
        select_negative_accounts(array)
    elif(option == 2):
        select_accounts_by_min_balance(array)
    elif(option == 3):
        select_all_accounts(array)
    else:
        return