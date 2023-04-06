import sys, os, joblib
import bank_util as bu
# 계좌는 계좌번호, 소유주, 잔액으로 구성됨
# 계좌번호는 생성된 시점의 시간,분,초 6자리로 구성됨
filename = 'account.jl'
if os.path.exists(filename):
    account = joblib.load(filename)
else:
    account = [
        {'계좌번호':142601,'소유주':'홍길동','잔액':10000}
    ]


while True:
    try:
        menu = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4:출금, 5: 소유자 계좌확인, 6: 종료> '))
    except:
        print('잘못된 명령입니다.\n')
        continue
    if 0<menu<7:
        if menu == 6:
            joblib.dump(account, filename)
            sys.exit()
        if menu == 1:
            bu.create_account(account)
        elif menu == 2:
            for acc in account:
                for key, val in acc.items():
                    print(f'{key}: {val}',end='\t')
            print()
        elif menu == 3:
            bu.deposit(account)
        elif menu == 4:
            bu.withdraw(account)
        elif menu == 5:
            bu.check(account)
        print()
    else:
        print('잘못된 명령입니다.\n')
        continue