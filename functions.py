from time import sleep


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
        option = enter_integer_number()
        if((option > 5) or (option < 1)):
            print('[ERRO] Opção inválida, tente novamente... \n')
            continue
        return option

def manager_reports_menu():
    while True:
        print('-----MENU DE RELATÓRIOS GERENCIAIS-----')
        print('[1] Listar clientes com saldo negativo')
        print('[2] Listar clientes a partir de determinado valor')
        print('[3] Listar todos os clientes')
        print('[4] Retornar ao menu principal')
        print('----------------------------------------- \n')
        option = enter_integer_number()
        if((option > 4) or (option < 1)):
            print('[ERRO] Opção inválida, tente novamente... \n')
            continue
        return option

# Primary Functions
def enter_integer_number():
    while True:
        try:
            number = int(input('Digite o número (inteiro) desejado: '))
        except ValueError:
            print('[ERRO] Número inválido... \n')
            continue
        else:
            return number

def enter_float_number():
    while True:
        try:
            number = float(input('Digite o número (real) desejado: '))
        except ValueError:
            print('[ERRO] Número inválido... \n')
            continue
        else:
            return number

def enter_account_number():
     while True:
        try:
            account_number = int(input('Digite o número (inteiro) desejado: '))
            if(account_number <= 0):
                print('[ERRO] O número deve ser maior que 0 (zero)...')
                new_try = try_again()
                if(new_try):
                    continue
                else:
                    break
            return account_number
        except ValueError:
            new_try = try_again()
            if(new_try):
                continue
            else:
                break

def enter_update_value():
    while True:
        try:
            update_value = float(input('Digite o valor (número real) da transação: '))
            if(update_value <= 0):
                print('[ERRO] Você deve digitar um valor positivo')
                continue
            return update_value
        except ValueError:
            print('[ERRO] Número inválido, tente novamente... \n')
            continue

def enter_balance_update_type():
    while True:
        try:
            update_type = int(input('Você deseja inserir ou remover fundos da sua conta? \n [1] Inserir \n [2] remover: \n'))
            if((update_type != 1) and (update_type != 2)):
                print('[ERRO] Opção inválida...')
                new_try = try_again()
                if(new_try):
                    continue
                else:
                    break
            return update_type
        except ValueError:
            print('[ERRO] Número Inválido...')
            new_try = try_again()
            if(new_try):
                continue
            else:
                break

def find_index(array, account_number):
    cont = 0
    for account in array:
        cont += 1
        if(account[0] == account_number):
            return (cont - 1)
    return (-1)

def try_again():
    while True:
        option = str(input('Deseja tentar novamente? [S/N]: '))
        if(option in ('S', 's')):
            return True
        elif(option in ('N', 'n')):
            return False
        else:
            print('[ERRO] Opção Inválida, tente novamente...')

def set_account_number(array):
    while True:
        print('Insira abaixo um número para sua conta')
        account_number = enter_account_number()
        if(not account_number):
            break
        account_numberExists = find_index(array, account_number)
        if(account_numberExists != -1):
            print('[ERRO] Este número de conta já está em uso, insira outro...')
            continue
        return account_number

def set_account_name():
    while True:
        account_user = str(input('Digite seu nome completo: '))
        name_split = account_user.split()
        if(len(name_split) < 2):
            print('[ERRO] Por favor, digite seu nome completo para prosseguir!')
            new_try = try_again()
            if(new_try):
                continue
            else:
                break
        return account_user

def set_initial_balance():
    while True:
        print('Digite abaixo a quantia que deseja depositar para abrir sua conta (número real): ')
        initial_balance = enter_float_number()
        if(initial_balance < 0):
            print('[ERRO] Valores negativos não são permitidos...')
            continue
        return initial_balance

# Secundary functions
def create_account(array):
    account_number = set_account_number(array) 
    if(not account_number):
        return
    account_name = set_account_name()
    if(not account_name):
        return
    initial_balance = set_initial_balance()
    print('Conta registrada...')
    account = [account_number, account_name, initial_balance]
    array.append(account)

def remove_account(array):
    while True:
        print('Digite abaixo o número da conta que deseja excluir: ')
        account_number = enter_account_number()
        index = find_index(array, account_number)
        if(index == -1):
            print('[ERRO] Não foi encontrada nenhuma conta com este número...')
            new_try = try_again()
            if(new_try):
                continue
            else:
                break
        if(array[index][2] != 0):
            print('[ERRO] Para realizar esta operação o saldo da conta deve ser igual a 0')
            return    
        array.pop(index)
        return

def change_account_balance(array):
    while True:
        print('Digite abaixo o número da conta que você deseja alterar o saldo:')
        account_number = enter_account_number()
        if(not account_number):
            break
        index = find_index(array, account_number)
        if(index == -1):
            print('[ERRO] Não foi encontrada nenhuma conta com este número...')
            new_try = try_again() 
            if(new_try):
                continue
            else:
                break 
        actual_value = array[index][2]
        update_type = enter_balance_update_type()
        if(not update_type):
            break
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
        sleep(1.5)
        return
    print('Contas com saldo negativo: ')
    for account in array:
        if(account[2] < 0):
            cont += 1
            print(f'{account} \n')
    sleep(1.5)
    if(cont == 0):
        print('Não foram encontradas contas com saldo negativo \n')
        sleep(1.5)
        return

def select_accounts_by_min_balance(array):
    cont = 0
    if(len(array) == 0):
        print('Não há contas cadastradas... \n')
        sleep(1.5)
        return
    print('Digite um valor e receba todas as contas com saldo acima do mesmo: ')
    min_value = enter_float_number()
    for account in array:
        if(account[2] > min_value):
            cont += 1
            print(f'{account} \n')
    sleep(1.5)
    if(cont == 0):
        print(f'Não foram encontradas contas com saldo acima de R${min_value} \n')
        sleep(1.5)
    
def select_all_accounts(array):
    if(len(array) == 0):
        print('Não há contas cadastradas... \n')
        sleep(1.5)
        return
    print('----------Contas registradas---------- \n')
    print('|N° da conta | Nome do correntista | Saldo da conta| \n')
    for account in array:
        print(f'{account} \n')
    print('-------------------------------------- \n')
    sleep(1.5)

# Finish boolean function
def finish(array):
    while True:
        option = str(input('Deseja realizar outra operação? [S/N]: '))
        if(option in ('S', 's')):
            return False
        elif(option in ('N', 'n')):
            print('Até logo...')
            save_all(array)
            return True
        else:
            print('[ERRO] Opção Inválida, tente novamente...')
