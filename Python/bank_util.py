import datetime as dt

# 이름과 금액을 입력으로 받아서 account에 새로운 항목을 추가
def create_account(account):
    try:
        cmd = input('이름 금액> ').split()
        if len(cmd) != 2:
            raise ValueError
        name, amount = cmd[0],int(cmd[1])
    except ValueError:
        print('올바른 입력 형식이 아닙니다.')
        return
    except Exception():
        print('입력이 잘못되었습니다.')
        return
    now = dt.datetime.now()
    ano = now.strftime('%H%M%S')
    account.append({'계좌번호':ano,'소유주':name,'잔액':amount})
        
    return
    
    

# 계좌번호 금액을 입력으로 받아서 계좌의 금액을 추가
def deposit(account):
    try:
        cmd = input('계좌 금액> ').split()
        if len(cmd) != 2:
            raise ValueError
        ano, amount = cmd[0],int(cmd[1])
    except:
        print('입력이 잘못되었습니다.')
        return
    for acc in account:
        if ano == acc['계좌번호']:
            acc['잔액'] += amount
            return


# 계좌번호 금액을 입력으로 받아서 계좌의 금액을 인출
def withdraw(account):
    try:
        cmd = input('계좌 금액> ').split()
        if len(cmd) != 2:
            raise ValueError
        ano, amount = cmd[0],int(cmd[1])
    except:
        print('입력이 잘못되었습니다.')
        return
    for acc in account:
        if ano == acc['계좌번호']:
            if acc['잔액'] >= amount:
                acc['잔액'] -= amount
            else:
                print('잔액이 부족합니다.')
            return

# 이름으로 검색해서 소유한 계좌 출력
def check(account):
    try:
        name = input('이름> ')
        check_owner = False
        for owner in account:
            if owner['소유주'] == name:
                print(f'{owner["소유주"]}: 계좌번호 : {owner["계좌번호"]} : 잔액 : {owner["잔액"]}')
                check_owner = True
        if not check_owner:         # check_owner 가 False 일때
            raise ValueError(f"'{name} 소유자가 보유한 계좌가 없습니다.'")
        return
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception():
        print(f'{name}이 가지고 있는 계좌가 없습니다.')
